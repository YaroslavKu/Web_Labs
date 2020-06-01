<template>
    <header>
        <router-link to="/"><h1 id="header_logo">Театральна<br>Афіша</h1></router-link>
        <div class="nav_bar">
            <router-link class="nav_link" to="/theaters">Театри</router-link>
            <template v-if="!authenticated">
                <router-link class="nav_link" to="/login">Login</router-link>
            </template>
            <template v-if="authenticated">
                <a v-on:click.prevent="singOut"  v-if="authenticated" href="http://192.168.2.213:8080/" class="nav_link">Logout</a>
            </template>
        </div>
    </header>
</template>

<script>
    import { mapGetters, mapActions } from 'vuex'
    export default {
        name: "Header",
        computed: {
            ...mapGetters({
                authenticated: 'auth/authenticated',
            })
        },

        methods: {
            ...mapActions({
                singOutAction: 'auth/singOut'
            }),

            singOut() {
                this.singOutAction()
            }
        }
    }
</script>

<style scoped>
</style>