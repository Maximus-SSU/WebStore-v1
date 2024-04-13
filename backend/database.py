# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session

# from fastapi import Depends, FastAPI
# from sqlalchemy import Column, Integer, String
# # class FishModel(BaseModel):
# #     id: int
# #     name: str
# #     price: int
# #     image_url: str
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:7237@localhost/WebSitev1"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# class Fish(Base):
#     __tablename__ = 'fish'

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     price = Column(Integer)
#     image_url = Column(String)


# Base.metadata.create_all(bind=engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()