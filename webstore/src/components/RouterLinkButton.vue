<template>
    <router-link :to="link" class="link-button">{{ title }}</router-link>
</template>

<script>
export default {
    name: 'LinkButton',
    props: {
        link: String,
        title: String
    }
}
</script>

<style scoped>
    .link-button {
        font-family:'Times New Roman', Times, serif;
        font-weight: 400;
        font-size: 40px;
        text-decoration: none;
        color: rgb(0, 0, 0);
        background-color: rgb(165, 176, 159);
        border-radius: 7px;
        padding: 5px 20px;
    }
</style>