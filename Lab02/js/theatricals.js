let htmlPlaybill = '';
const TheatricalIds = [];

fetch('http://127.0.0.1:8000/api/playbil/theatrical/all/')
    .then(function(response){ 
        return response.json();
    })
    .then((data) => {
        data.forEach((el) => {
            TheatricalIds.push(el.id);
            htmlPlaybill += `
                <div class="theatrical">
                    <a class="theatracal-link" href="theatrical.html">
                    <img class="poster_img" src="${el.poster_url}" alt="">
                        <p class="theatrical_name">${el.name}</p>
                    </a>
                </div>
            `;
        });

        document.getElementById('theatrical').innerHTML = htmlPlaybill;

        const theatricalLinks = document.querySelectorAll('.theatracal-link');

        for (let i = 0; i < theatricalLinks.length; i += 1) {
            theatricalLinks[i].onclick = function () {
                localStorage.setItem('id', TheatricalIds[i]);
            };
        }
    });
