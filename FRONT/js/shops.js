
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

async function haeKaupat() {
    const response = await fetch('/kaupat');
    const kaupatLista = document.getElementById('kaupat');
    kaupatLista.innerHTML = '';

    if (response.ok) {
        const kaupat = await response.json();
        kaupat.forEach(kauppa => {
            const article = document.createElement('article');
            article.classList.add('planeCard');
            article.textContent = `ID: ${kauppa.id}, Tyyppi: ${kauppa.tyyppi}, Hinta: ${kauppa.hinta}, Teema: ${kauppa.teema}`;
            const ostaNappi = document.createElement('button');
            ostaNappi.textContent = 'Osta';
            ostaNappi.onclick = () => ostaKauppa(kauppa.id);
            article.appendChild(ostaNappi);
            kaupatLista.appendChild(article);
        });
    } else {
        const error = await response.json();
        kaupatLista.innerHTML = `<li>${error.message}</li>`;
    }
}

async function ostaKauppa(shopId) {
    const response = await fetch('/osta_kauppa', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ shop_id: shopId })
    });
    const data = await response.json();
    alert(data.message)
    haeKaupat()
}
haeKaupat()