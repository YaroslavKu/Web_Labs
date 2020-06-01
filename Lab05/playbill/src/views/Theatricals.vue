<template>
    <div>
        <div class="container">
            <div class="search">
                <input v-model="search" required type="text" class="searchTerm" placeholder="Пошук..">
                <button v-on:click="getTheatricals(search)" type="submit" class="searchButton">
                    Знайти
                </button>
            </div>
        </div>
        <template v-if="isLoading">
            <Preloader/>
        </template>
        <template v-if="!isLoading">
            <div class="container">
                <div class="theatricals">
                    <Poster
                    v-for="th of theatricals" :key="th.id"
                    v-bind:theatrical="th"
                    />
                </div>
            </div>
        </template>
    </div>
</template>

<script>
    import Poster from "../components/Poster";
    import Preloader from "../components/Preloader";

    export default {
        name: "Theatricals",
        components: {
            Poster,
            Preloader
        },

        data() {
            return {
                theatricals: [],
                search: "",
                isLoading: true
            }
        },

        methods: {
            getTheatricals (search) {
                fetch("http://127.0.0.1:8000/api/playbil/theatrical/all/?search=" + search)
                    .then(response => response.json())
                    .then((data) => {
                        this.theatricals = data;
                        this.isLoading = false;
                    })
            }
        },

        beforeMount(){
            this.getTheatricals("")
        },
    }
</script>

<style scoped>

</style>