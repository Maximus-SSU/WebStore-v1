<template>
    <a :href="link" class="link-button">{{ title }}</a>
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

<style scoped lang="scss">
    .link-button {
        font-family: "Sofia Sans";
        font-weight: 400;
        font-size: 40px;
        text-decoration: none;
        color: white;
        background-color: rgb(165, 176, 159);
        border-radius: 7px;
        padding: 5px 20px;
        
    }
</style>