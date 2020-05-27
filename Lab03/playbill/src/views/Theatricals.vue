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
        <div class="container">
            <div class="theatricals">
                <Poster
                v-for="th of theatricals" :key="th.id"
                v-bind:theatrical="th"
                />
            </div>
        </div>
    </div>
</template>

<script>
    import Poster from "../components/Poster";

    export default {
        name: "Theatricals",
        components: {Poster},

        data() {
            return {
                theatricals: [],
                search: ""
            }
        },

        methods: {
            getTheatricals (search) {
                fetch("http://127.0.0.1:8000/api/playbil/theatrical/all/?search=" + search)
                    .then(response => response.json())
                    .then((data) => {
                        this.theatricals = data;
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