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



async function fetchAchievements() {
    const response = await fetch('/achivs');
    console.log(response);  
    const achlist = document.getElementById('achievements-list');
    achlist.innerHTML = '';

    if (response.ok) {
        const achievements= await response.json();
        achievements.forEach(achievement => {
            const article = document.createElement('article');
           
            article.textContent = `${achievement.description}`;

            achlist.appendChild(article);
        });
    
    } else {
        const error = await response.json();
        achlist.innerHTML = `<li>${error.message}</li>`;
    }
}
fetchAchievements();