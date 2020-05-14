let htmlTheaters = ""

fetch('http://127.0.0.1:8000/api/playbil/theater/all/')
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log(data)
        data.forEach((el) => {
            htmlTheaters += `
            <div class="container">
                <h2>${el.name}</h2>
                <div class="theater_info">
                    <img class="theater_photo" src="${el.photo_url}" alt="">
                    <div class="info">
                        <p>Адреса: ${el.address}</p>
                        <p>Телефон: ${el.phone}<br></p>
                        <p>Email: ${el.email}</p>
                        <p>Веб сайт: <a class="theater_site" href="${el.schedule}">${el.schedule}</a></p>
                    </div> 
                </div>
                <div class="description">
                    <p>${el.description}</p>
                </div>
            </div>
            `;
    }); 
    
    document.getElementById('theaters').innerHTML = htmlTheaters;  
});