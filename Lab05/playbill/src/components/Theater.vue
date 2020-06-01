<template>
    <div class="container">
        <h2>{{theater.name}}</h2>
        <div class="theater_info">
            <img class="theater_photo" :src="theater.photo_url" alt="">
            <div class="info">
                <p>Адреса: {{theater.address}}</p>
                <p>Телефон: {{theater.phone}}<br></p>
                <p>Email: {{theater.email}}</p>
                <p>Веб сайт: <a class="theater_site" :href="theater.schedule">{{theater.schedule}}</a></p>
            </div>
        </div>
        <div class="description">
            <p>{{theater.description}}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Theater",
        props: {
            theater: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style scoped>
    .theater_site {
        color: #424242;
    }

    .theater_info {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        max-width: 1150px;
        margin: 30px;
    }

    .theater_photo {
        width: 500px;
        box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
    }

    .info {
        min-width: 100px;
        color: #424242;
        font-size: 18px;
        margin-left: 30px;
        margin-right: 30px;
    }

    .description {
        font-size: 18px;
        text-align: center;
        margin-left: 100px;
        margin-right: 100px;
        color: #424242;
    }

    .container {
        margin-bottom: 100px;
        background: #ededed;
        box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
    }

    @media screen and (max-device-width: 480px) and (orientation: portrait) {
        .theater_photo {
            width: 90%;
        }

        .theater_info {
            justify-content: center;
        }

        .info {
            font-size: 32px;
        }
    }
</style>