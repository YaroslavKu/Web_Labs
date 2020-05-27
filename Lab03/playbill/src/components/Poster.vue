<template>
    <div class="theatrical">
        <router-link :to="'/theatrical/'+ theatrical.id + '/'">
            <img class="poster_img" :src="theatrical.poster_url" alt="">
            <p class="theatrical_name">{{theatrical.name}}</p>
        </router-link>

    </div>
</template>

<script>
    export default {
        name: "Poster",

        props: {
            theatrical: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style scoped>
</style>