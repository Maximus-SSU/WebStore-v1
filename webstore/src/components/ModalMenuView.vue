
<template>
  <div class="modal-backdrop">
    <div class="modal">
      <header class="modal-header">
        <slot name="header">
          <button
            type="button"
            class="btn-close"
            @click="closeMenu"
          >
            x
          </button>
        </slot>
      </header>
      <section class="modal-body">
        <RouterLinkMenuButton link="/" title="Главная"> </RouterLinkMenuButton>
        <RouterLinkMenuButton 
        v-show="$route.name!=='userRegistration' && $route.name!=='userAuthorization'
        && $route.name!=='home'" 
        link="/UserProfile"
        title="Профиль"> </RouterLinkMenuButton>
        <RouterLinkMenuButton
        v-show="$route.name!=='userRegistration' && $route.name!=='userAuthorization'
        && $route.name!=='home'" 
         link="/UserPets" 
         title="Мои Питомцы">
         </RouterLinkMenuButton>
        <RouterLinkMenuButton 
        v-show="$route.name!=='userRegistration' && $route.name!=='userAuthorization'
        && $route.name!=='home'" 
        link="/UserServices"
         title="Услуги"> 
        </RouterLinkMenuButton>
        <RouterLinkMenuButton
        v-show="$route.name=='home'"
         link="/userAuthorization" 
         title="Войти">
         </RouterLinkMenuButton>
        <RouterLinkMenuButton
         link="/about" 
         title="О нас">
         </RouterLinkMenuButton>
       </section>
       <footer class="modal-footer">
      </footer>
    </div>
  </div>
</template>
<script>
import RouterLinkMenuButton from './RouterLinkMenuButton.vue';

  export default {
    name: "ModalMenu",
    data() {
        return {};
    },
    methods: {
        closeMenu() {
            this.$emit("closeMenu");
        },
        PageStatus(){ //тут как раз должен был быть условный блок для определения ссылок в модальном окне (в разработке)
            // if ( Route== "/") return 0
            if (this.$route.name=='userRegistration' || this.$route.name=='userAuthorization' )
             return 2
             else if(this.$route.name=='ForgotPassword') 
                return 1
                else 
                    return 0 
        }
    },
    components: 
    { RouterLinkMenuButton 
    }

};
</script>

<style>
  .modal-backdrop {
    z-index: 9999;
    margin-top: 18px;
    margin-left: auto;
    display: flex;
    justify-content: center;
    align-items: center;
    

  }

  .modal {
    max-height: 349px;
    max-width: 349px;
    border-radius: 35px;
    background: #FFFFFF;
    overflow-x: auto;
    display: flex;
    margin-right:100px;
    flex-direction: column;
  }


  .modal-header {
    display: flex;
    align-content: center;
    color: #FFFFFF;
    justify-content: flex-end;
  }

  .modal-footer {
    justify-content: flex-end;
  }

  .modal-body {
    display: flex;
    flex-direction: column;
    position: relative;
    padding: 10px 10px;
  }

  .btn-close {

    border: none;
    font-size: 36px;
    padding-right: 15px;
    cursor: pointer;
    font-weight:1000;
    font-family:"Sofia Sans";
    color: #424242;
    background: #FFFFFF;
  }
  a:link {
  text-decoration: none;
  color:black
}
a:visited{
    text-decoration: none;
    color:black 
}

</style>