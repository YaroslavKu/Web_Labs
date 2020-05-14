
let htmlPlaybill = '';
var TheatricalIds = [];

fetch('http://127.0.0.1:8000/api/playbil/theatrical/all/')
    .then((response) => {
        return response.json();
    })
    .then((data) => {
    data.forEach((el) => {
        TheatricalIds.push(el.id)
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
    
    function getAttribute(locId) {
        localStorage.setItem('id', locId);
    }
    
    
    const theatricalLinks = document.querySelectorAll(".theatracal-link");
    console.log(theatricalLinks)
    
    for (let i = 0; i < theatricalLinks.length; i += 1) {
        theatricalLinks[i].onclick = function() {
            getAttribute(TheatricalIds[i]);
        }
    }

    console.log(TheatricalIds)
});