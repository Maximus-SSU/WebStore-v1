<template>
    <div class="menu-button-section">
        <img 
        class="menu-dotpoint"
        src="../assets/ModalMenuDot.svg"
        />
    <router-link :to="link" class="link-button-menu">{{ title }}</router-link>
</div>
</template>

<script>
export default {
    name: 'LinkButtonMenu',
    props: {
        link: String,
        title: String
    }
}
</script>

<style  scoped>
    .menu-button-section{
         display:flex;
         margin-top: 10px;
        }
    .menu-dotpoint{
        display: flex;
        margin-left: 10px;
        margin-right: 10px;
    }
        
    .link-button-menu {
        font-family: "Cormorant Infant";
        font-size: 35px;
        font-weight: 400;
        line-height: 42px;
        letter-spacing: 0em;
        text-align: left;

        a {
            font-size: 35px;
            color: black;
            &.router-link-exact-active {
                font-weight: bold;
            }
        }
        a:link {
            text-decoration: none;
            color:black
        }
        a:visited{
            text-decoration: none;
            color:black;
        }
    }
</style>