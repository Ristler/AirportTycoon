
//Gets user id and name from localstorage. -> saved in auth.js


//UserLocal IS NOT WORKING ITS NULL MIKSI????
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
map.flyTo([40.7128, -74.0060], 12, {
  duration: 20,      // Fly duration in seconds
  easeLinearity: 0.9 // Smoothness of the fly animation
});


//Navbar user info
const user = document.querySelector("#player").innerHTML = "Player: "+ userLocal
const money = document.querySelector("#money").innerHTML = "Money: "+ moneyLocal + "$"
const laina = document.querySelector("#loans").innerHTML = "Loans: "+ lainaLocal + "$"


async function xFunction(event) {
  event.preventDefault();
  
  // Prevent the default form submission
  lentokoneet = new formData();
  lentokoneet.append("id", id )
  try{
  const response = await fetch('http://127.0.0.1:5000/ListaaLentokoneet', {
    method: 'POST',
    body: lentokoneet,
});
  if(response.ok){
      const result = await response.json();
      console.log("LISTAALENTOKONE TESTI", result);
   } else {
          alert(result.message);  // Show the error message
      }
  } catch (error) {
      console.error('Error:', error);
      alert('An error occurred. Please try again later.');
  }
}


