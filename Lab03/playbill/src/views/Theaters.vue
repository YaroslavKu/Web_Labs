<template>
    <div>
        <Theater
            v-for="th of theaters" :key="th.id"
            v-bind:theater="th"
        />
    </div>
</template>

<script>
    import Theater from "../components/Theater";

    export default {
        name: "Theaters",
        components: {Theater},

        data() {
            return {
                theaters: []
            }
        },

        methods: {
            getTheaters () {
                fetch("http://127.0.0.1:8000/api/playbil/theater/all/")
                    .then(response => response.json())
                    .then((data) => {
                        this.theaters = data;
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