
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




