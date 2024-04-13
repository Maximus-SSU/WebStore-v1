from fastapi import FastAPI, Depends

import os
#For Swager
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.models import OpenAPI
from fastapi.responses import RedirectResponse


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()

############################################################
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError

from fastapi import Depends, FastAPI,HTTPException
from sqlalchemy import Column, Integer, String, Text,ForeignKey

from fastapi.middleware.cors import CORSMiddleware

# Разрешаем все источники и все методы и заголовки
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



SQLALCHEMY_DATABASE_URL = "postgresql://postgres:7237@localhost/WebSitev1"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Fish(Base):
    __tablename__ = 'fish'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    image_url = Column(String)
    desc= Column(Text)

# Определение модели для таблицы cart
class Cart(Base):
    __tablename__ = 'cart'

    id = Column(Integer, primary_key=True)
    fishid = Column(Integer)
    count = Column(Integer)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

###########################################################

        
# Функция для получения списка всех рыб
@app.get("/fish/all")
def get_fish(db: Session = Depends(get_db)):
    fishes = db.query(Fish).all()
    return fishes


# # Endpoint для получения информации о рыбе по ID
@app.get("/fish/{fish_id}")
async def get_fish_by_id(fish_id: int):
    db = SessionLocal()
    fish = db.query(Fish).filter(Fish.id == fish_id).first()
    db.close()
    if fish is None:
        raise HTTPException(status_code=404, detail="Fish not found")
    return fish



# Эндпоинт для добавления рыбы в корзину
@app.post("/cart/{fish_id}")
def add_to_cart(fish_id: int):
    db = SessionLocal()
    # Проверяем существует ли рыба с таким id
    fish = db.query(Fish).filter(Fish.id == fish_id).first()
    if not fish:
        raise HTTPException(status_code=404, detail="Fish not found")
    
    # Создаем новую запись в таблице cart
    cart_item = Cart(fishid=fish_id, count=1)
    db.add(cart_item)
    db.commit()
    
    return {"message": "Fish added to cart successfully"}

# Эндпоинт для удаления записи из таблицы cart по идентификатору
@app.delete("/cart/{cart_id}")
def delete_cart_item(cart_id: int, db: Session = Depends(get_db)):
    # Пытаемся найти запись в корзине с указанным идентификатором
    cart_item = db.query(Cart).filter(Cart.id == cart_id).first()
    if cart_item is None:
        raise HTTPException(status_code=404, detail="Cart item not found")
    try:
        # Удаляем запись из таблицы cart
        db.delete(cart_item)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred")
    
    return {"message": f"Cart item with ID {cart_id} has been deleted from the cart"}

# Эндпоинт для удаления всех записей из таблицы cart
@app.delete("/cart/all")
def delete_all_cart_items(db: Session = Depends(get_db)):
    try:
        # Удаляем все записи из таблицы cart
        db.query(Cart).delete()
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred")
    
    return {"message": "All items have been deleted from the cart"}
    
# Эндпоинт для получения данных из таблицы cart
@app.get("/cart/all")
def get_cart_items(db: Session = Depends(get_db)):
    cart_items = db.query(Cart).all()
    return cart_items

# Эндпоинт для получения одного элемента из таблицы cart по его ID
@app.get("/cart/{cart_id}")
def get_cart_item(cart_id: int, db: Session = Depends(get_db)):
    cart_item = db.query(Cart).filter(Cart.id == cart_id).first()
    if cart_item is None:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return cart_item

# Обработчик для корневого URL
@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

# Добавляем обработчик для получения HTML-страницы Swagger UI
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Swagger UI")
  
# Добавляем обработчик для получения схемы OpenAPI
@app.get("/openapi.json", include_in_schema=False)
async def get_openapi_endpoint():
    return app.openapi()
