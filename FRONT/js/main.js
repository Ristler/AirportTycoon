
//Gets user id and name from localstorage. -> saved in auth.js
const userLocal = JSON.parse(localStorage.getItem("class")).user
const moneyLocal = JSON.parse(localStorage.getItem("class")).raha
const lainaLocal = JSON.parse(localStorage.getItem("class")).laina


//Audio
const flySound = new Audio("../audio/fly.mp3")

//Navbar user info
const user = document.querySelector("#player").innerHTML = "Player: "+ userLocal
const money = document.querySelector("#money").innerHTML = "Money: "+ moneyLocal + "$"
const laina = document.querySelector("#loans").innerHTML = "Loans: "+ lainaLocal + "$"

//Basic map
const map = L.map('map', { tap: false });
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60, 24], 7);


//This functions triggers the map animation
function fly(latid, long) {
  flySound.play();
  map.flyTo([latid, long], 12, {
    duration: 8.5,    
    easeLinearity: 0.9 
});
}

async function listaaLentokoneet() {
  const response = await fetch('/listaa_lentokoneet');

  const lentokoneLista = document.getElementById('planes');
  lentokoneLista.innerHTML = '';

  if (response.ok) {
      const planes = await response.json();

      planes.forEach(plane => {
          const article = document.createElement('article');
          article.classList.add('planeCard');

          article.textContent = `ID: ${plane.id}, Tyyppi: ${plane.tyyppi}, Kapasiteetti: ${plane.kapasiteetti},
          Hinta: ${plane.hinta}, Efficiency: ${plane.efficiency}, Max fuel: ${plane.maxfuel}`;
          const valitseNappi = document.createElement('button');
          valitseNappi.textContent = 'Valitse';
          valitseNappi.onclick = () => valitseLentokone(plane.id, lentokoneLista);
          article.appendChild(valitseNappi);

          lentokoneLista.appendChild(article);
      });
  } else {
      const error = await response.json();
      lentokoneLista.innerHTML = `<li>else lausekke help error:${error.message}</li>`;
  }
}

async function valitseLentokone(planeId, lentokoneLista) {
  lentokoneLista.innerHTML = '';

  const response = await fetch('/prepare', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ plane_id: planeId })
  });
  const data = await response.json();
  const latitude = data["latitude"];
  const longitude = data['longitude'];
  fly(latitude, longitude);
}


//Delete maybe no use for this anymore
async function xFunction(event) {
  event.preventDefault();

  try{
  const response = await fetch('http://127.0.0.1:5000/ListaaLentokoneet', {
    method: 'POST',
    body: localStorage.getItem("class").id
});
  const result = await JSON.parse(response.json());
  if(response.ok){

      console.log("LISTAALENTOKONE TESTI", result);
   } else {
          alert(result.message); 
      }
  } catch (error) {
      console.error('Error:', error);
      alert('An error occurred. Please try again later.');

  }
}

async function ostaLentokone(event) {
  event.preventDefault();
  
  try{
  const response = await fetch('http://127.0.0.1:5000/ListaaLentokoneet', {
    method: 'POST'
});
  const result = await JSON.parse(response.json());
  if(response.ok){

      console.log("LISTAALENTOKONE TESTI", result);
   } else {
          alert(result.message);
      }
  } catch (error) {
      console.error('Error:', error);
      alert('An error occurred. Please try again later.');
  }
}




