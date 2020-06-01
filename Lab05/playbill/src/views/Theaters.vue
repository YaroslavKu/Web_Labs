<template>
    <div>
        <template v-if="isLoading">
            <Preloader/>
        </template>

        <template v-if="!isLoading">
            <Theater
                v-for="th of theaters" :key="th.id"
                v-bind:theater="th"
            />
        </template>
    </div>
</template>

<script>
    import Theater from "../components/Theater";
    import Preloader from "../components/Preloader";

    export default {
        name: "Theaters",
        components: {
            Theater,
            Preloader
        },

        data() {
            return {
                theaters: [],
                isLoading: true
            }
        },

        methods: {
            getTheaters () {
                fetch("http://127.0.0.1:8000/api/playbil/theater/all/")
                    .then(response => response.json())
                    .then((data) => {
                        this.theaters = data;
                        this.isLoading = false
                    })
            }
        },

        beforeMount(){
            this.getTheaters()
        },
    }


</script>

<style scoped>
</style>