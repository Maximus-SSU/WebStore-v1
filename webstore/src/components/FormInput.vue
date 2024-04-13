<template>
    <input class=form-input type="text"  :name="name" :form="form" :placeholder="placeholder">
</template>

<script>
    export default {
    name: 'FormInput',
    props: {
        name: String,
        form: String,
        placeholder: String
    }
}
</script>

<style  lang="scss">
    .form-input {
        display:flex;
        font-family: Content;
        font-size: 25px;
        font-weight: 400;
        line-height: 46px;
        letter-spacing: 0em;
        text-align: left;
        max-width: 675px;
        width: 100%;
        height: 100px;
        border: 1px solid #E18383;
        border-radius: 15px;
        padding: 10px 30px;
        margin-top: 50px;

        &:focus {
            outline: none;
        }
    }
</style>