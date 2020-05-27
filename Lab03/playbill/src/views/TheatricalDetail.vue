<template>
    <div id="theatrical_detail">
        <div class="container">
            <h1 class="theatrical_name">{{theatricalDetail.name}}</h1>
        </div>
        <div class="theatricl_info">
            <img class="poster" :src="theatricalDetail.poster_url" alt="">
            <div class="info">
                <p>Організатор:<br>{{theatricalDetail.theater.name}}</p>
                <p>Місце проведення:<br>{{theatricalDetail.theater.address}}</p>
                <p>Подія відбудеться: {{theatricalDetail.time.slice(0, 10)}}<br>
                    Початок: {{theatricalDetail.time.slice(11, 16)}}</p>
                <a :href="theatricalDetail.tickets_url">
                    <button>Купити квиток</button>
                </a>
            </div>
        </div>
        <div class="description">
            <p>{{theatricalDetail.description}}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Theatrical",
        data () {
            return {
                id: this.$route.params.id,
                theatricalDetail: {}
            }
        },

        methods: {
            getTheatricalInfo () {
                fetch("http://127.0.0.1:8000/api/playbil/theatrical/" + this.id + "/")
                    .then(response => response.json())
                    .then((data) => {
                        this.theatricalDetail = data;
                    })
            }
        },

        beforeMount(){
            this.getTheatricalInfo()
        },
    }
</script>

<style scoped>
    .theatricl_info {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        max-width: 1150px;
    }

    .theatrical_name {
        font-size: 42px;
    }

    .poster {
        margin: 30px;
        width: 300px;
        height: auto;
        box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
    }

    .info {
        margin-top: 10px;
        min-width: 200px;
        color: #ffffff;
        font-size: 18px;
    }

    .description {
        margin: 30px;
        font-size: 18px;
        color: #ffffff;
    }

    button {
        font-family: "Roboto", sans-serif;
        text-transform: uppercase;
        outline: 0;
        background: #ffffff;
        width: 300px;
        border: 0;
        padding: 15px;
        color: #292929;
        font-size: 18px;
        cursor: pointer;
        box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
    }

    button:hover {
        background: #ededed;
    }

    @media screen and (max-device-width: 480px) and (orientation: portrait) {
        .theatrical_name {
            font-size: 72px;
        }

        .poster {
            width: 100%;
        }

        .theatricl_info {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }

        .info {
            font-size: 42px;
        }

        button {
            font-size: 42px;
            width: 100%;
            padding: 30px;
        }
    }
</style>