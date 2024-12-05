
const userLocal = JSON.parse(localStorage.getItem("class")).user
const moneyLocal = JSON.parse(localStorage.getItem("class")).raha
const lainaLocal = JSON.parse(localStorage.getItem("class")).laina


//Navbar user info
const user = document.querySelector("#player").innerHTML = "Player: "+ userLocal
const money = document.querySelector("#money").innerHTML = "Money: "+ moneyLocal + "$"
const laina = document.querySelector("#loans").innerHTML = "Loans: "+ lainaLocal + "$"

async function haeLentokoneet() {
    const response = await fetch('/planes');
    const lentokoneLista = document.getElementById('planes');
    lentokoneLista.innerHTML = '';

    

    if (response.ok) {
        const planes = await response.json();
        planes.forEach(plane => {
            console.log("whatsup ", planes)

            const article = document.createElement('article');
            article.classList.add('planeCard');
           
            article.textContent = `ID: ${plane.id}, Tyyppi: ${plane.tyyppi}, Kapasiteetti: ${plane.kapasiteetti},
            Hinta: ${plane.hinta}, Efficiency: ${plane.efficiency}, Max fuel: ${plane.maxfuel}`;

            const ostaNappi = document.createElement('button');
            ostaNappi.textContent = 'Osta';
            ostaNappi.onclick = () => ostaLentokone(plane.id);
            article.appendChild(ostaNappi);
            lentokoneLista.appendChild(article);
            

        });
    
    } else {
        const error = await response.json();
        lentokoneLista.innerHTML = `<li>${error.message}</li>`;
    }
}


async function ostaLentokone(planeId) {
    const response = await fetch('/buy_plane', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ plane_id: planeId })
    });
    const data = await response.json();
    alert(data.message)
}