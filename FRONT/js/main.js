
//Gets user id and name from localstorage. -> saved in auth.js
const userId = localStorage.getItem("userId")
const user = localStorage.getItem("username")


const map = L.map('map', { tap: false });
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60, 24], 7);


//ONLY USED FOR TESTING 
username = document.querySelector("#name").innerHTML = user


