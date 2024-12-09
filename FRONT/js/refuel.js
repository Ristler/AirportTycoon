
//Gets user id and name from localstorage. -> saved in auth.js
const userLocal = JSON.parse(localStorage.getItem("class")).user
const moneyLocal = JSON.parse(localStorage.getItem("class")).raha
const lainaLocal = JSON.parse(localStorage.getItem("class")).laina
const daysLocal = JSON.parse(localStorage.getItem("class")).Päivä
const loanexpirationLocal = JSON.parse(localStorage.getItem("class")).Eräpäivä


//Navbar user info
const user = document.querySelector("#player").innerHTML = "Player: "+ userLocal
const money = document.querySelector("#money").innerHTML = "Money: "+ moneyLocal + "$"
const laina = document.querySelector("#loans").innerHTML = "Loans: "+ lainaLocal + "$"
const days = document.querySelector("#days").innerHTML = "Days: "+ daysLocal 
const loansexpiration = document.querySelector("#loanexpiration").innerHTML = "Loan expiration: "+ loanexpirationLocal


async function haeLentokoneet() {
    const response = await fetch('/listaa_lentokoneet');
    const lentokoneLista = document.getElementById('refuel');
    lentokoneLista.innerHTML = '';

    if (response.ok) {
        const planes = await response.json();
        planes.forEach(plane => {
            const article = document.createElement('article');
            article.classList.add('planeCard');
           
            article.textContent = `ID: ${plane.id}, Type: ${plane.tyyppi}, Capacity: ${plane.kapasiteetti},
            Price: ${plane.hinta}, Efficiency: ${plane.efficiency}, Max fuel: ${plane.maxfuel}`;

            const repairNappi = document.createElement('button');
            repairNappi.textContent = 'Repair';
            repairNappi.onclick = () => repair(plane.id);
            article.appendChild(repairNappi);

            const refuelNappi = document.createElement('button');
            refuelNappi.textContent = 'Refuel';
            refuelNappi.onclick = () => refuel(plane.id);
            article.appendChild(refuelNappi);
            
            
            lentokoneLista.appendChild(article);
            

        });
    
    } else {
        const error = await response.json();
        lentokoneLista.innerHTML = `<li>${error.message}</li>`;
    }
}

async function refuel(planeId) {
    const response = await fetch('/refuel', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ plane_id: planeId })
    });
    const data = await response.json();
    alert(data.message)
    haeLentokoneet()
}


async function repair(planeId) {
    const response = await fetch('/repair', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ plane_id: planeId })
    });
    const data = await response.json();
    alert(data.message)
    haeLentokoneet()
}
haeLentokoneet()