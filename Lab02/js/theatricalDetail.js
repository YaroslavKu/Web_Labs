const theatricalId = localStorage.getItem('id');
const getRequest = "http://127.0.0.1:8000/api/playbil/theatrical/" + theatricalId + "/";
let htmlTheatrical = '';

console.log(getRequest);

fetch(getRequest)
    .then((response) => {
        return response.json();
    })
    .then((data) => { 
        console.log(data);

        htmlTheatrical += `
            <div class="container">
                <h1 class="theatrical_name">${data.name}</h1>
            </div>

            <div class="theatricl_info">
                <img class="poster" src="${data.poster_url}" alt="">
                <div class="info">
                    <p>Організатор:<br>${data.theater.name}</p>
                    <p>Місце проведення:<br>${data.theater.address}</p>
                    <p>Подія відбудеться: ${data.time.slice(0, 10)}<br>
                    Початок: ${data.time.slice(11, 16)}</p>
                    <a href="${data.tickets_url}">
                        <button>Купити квиток</button>
                    </a>
                </div>
            </div>
            <div class="description">
                <p>${data.description}</p>
            </div>
        `;

        document.getElementById('theatrical_detail').innerHTML = htmlTheatrical; 
    });