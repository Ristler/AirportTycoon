
//Gets user id and name from localstorage. -> saved in auth.js
const userLocal = JSON.parse(localStorage.getItem("class")).user
const moneyLocal = JSON.parse(localStorage.getItem("class")).raha
const lainaLocal = JSON.parse(localStorage.getItem("class")).laina


const map = L.map('map', { tap: false });
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60, 24], 7);


//ONLY USED FOR TESTING NOW
map.flyTo([39.019444, 125.738052], 12, {
  duration: 10,      // Fly duration in seconds
  easeLinearity: 0.9 // Smoothness of the fly animation
});


//Navbar user info
const user = document.querySelector("#player").innerHTML = "Player: "+ userLocal
const money = document.querySelector("#money").innerHTML = "Money: "+ moneyLocal + "$"
const laina = document.querySelector("#loans").innerHTML = "Loans: "+ lainaLocal + "$"




async function listaaLentokoneet() {
  const response = await fetch('/listaa_lentokoneet');

  const lentokoneLista = document.getElementById('planes');
  lentokoneLista.innerHTML = '';

  if (response.ok) {
      const planes = await response.json();

      planes.forEach(plane => {
          const li = document.createElement('li');

          li.textContent = `ID: ${plane.id}, Tyyppi: ${plane.tyyppi}, Kapasiteetti: ${plane.kapasiteetti},
          Hinta: ${plane.hinta}, Efficiency: ${plane.efficiency}, Max fuel: ${plane.maxfuel}`;


          const valitseNappi = document.createElement('button');

          valitseNappi.textContent = 'Valitse';

          valitseNappi.onclick = () => valitseLentokone(plane.id);
          li.appendChild(valitseNappi);
          
          lentokoneLista.appendChild(li);
      });
  } else {
      const error = await response.json();
      lentokoneLista.innerHTML = `<li>else lausekke help error:${error.message}</li>`;
  }
}



async function valitseLentokone(planeId) {

  const response = await fetch('/prepare', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ plane_id: planeId })
  });
  //const viesti = document.getElementById('viesti');
  const data = await response.json();
  return 

  //viesti.textContent = data.message;
}


async function xFunction(event) {
  event.preventDefault();
  
  // Prevent the default form submission
  try{
  const response = await fetch('http://127.0.0.1:5000/ListaaLentokoneet', {
    method: 'POST',
    body: localStorage.getItem("class").id
});
  const result = await JSON.parse(response.json());
  if(response.ok){

      console.log("LISTAALENTOKONE TESTI", result);
   } else {
          alert(result.message);  // Show the error message
      }
  } catch (error) {
      console.error('Error:', error);
      alert('An error occurred. Please try again later.');

  }
}


async function ostaLentokone(event) {
  event.preventDefault();
  
  // Prevent the default form submission

  try{
  const response = await fetch('http://127.0.0.1:5000/ListaaLentokoneet', {
    method: 'POST'
});
  const result = await JSON.parse(response.json());
  if(response.ok){

      console.log("LISTAALENTOKONE TESTI", result);
   } else {
          alert(result.message);  // Show the error message
      }
  } catch (error) {
      console.error('Error:', error);
      alert('An error occurred. Please try again later.');
  }
}




