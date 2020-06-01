<template>
    <div class="container">
        <div class="loader"></div>
    </div>
</template>

<script>
    export default {
        name: "Preloader"
    }
</script>

<style scoped>
    .loader {
        border: 10px solid #FFFFFF;
        border-radius: 50%;
        border-top: 10px solid #489b1b;
        width: 50px;
        height: 50px;
        -webkit-animation: spin 2s linear infinite; /* Safari */
        animation: spin 2s linear infinite;
        margin-top: 100px;
    }

    /* Safari */
    @-webkit-keyframes spin {
        0% { -webkit-transform: rotate(0deg); }
        100% { -webkit-transform: rotate(360deg); }
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
</style>