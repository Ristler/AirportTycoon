function local_info_update(){
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
    }
    local_info_update();

async function bank() {
    event.preventDefault();
    const amount = document.getElementById('loan').value;
    console.log("LOAN AMOUNT", amount)

    if (!amount) {
        alert('Loan amount is required.');
        return;
    }
    const formData = new FormData();

    formData.append('loan', amount);

    try {
        // Send the data via a POST request using Fetch API
        const response = await fetch('http://127.0.0.1:5000/otalainaa', {
            method: 'POST',
            body: formData,
        });

        // Handle response
        const result = await response.json();
        console.log(result)
        

        if (response.ok) {
            //localStorage.setItem("loan")
            
            const LocalClass = JSON.parse(localStorage.getItem("class"));
            LocalClass.raha =  result.rahanmaara;
            LocalClass.laina = result.lainanmaara;
            LocalClass.Eräpäivä = result.erapaiva;
            localStorage.setItem("class", JSON.stringify(LocalClass));
            console.log("testiiiii", result)
            alert(result.message);
            

        } else {
            alert(result.message);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again later.');
    }
}

async function paybackLoan() {
    event.preventDefault();
    const amount = document.getElementById('payment').value;
    console.log("PAYMENT AMOUNT", amount)

    if (!amount) {
        alert('Payment amount is required.');
        return;
    }
    const formData = new FormData();

    formData.append('payment', amount);

    try {
        // Send the data via a POST request using Fetch API
        const response = await fetch('http://127.0.0.1:5000/tarkistalaina', {
            method: 'POST',
            body: formData,
        });

        // Handle response
        const result = await response.json();
        console.log(result)
        

        if (response.ok) {
            //localStorage.setItem("loan")
            
            
            alert(result.message);
            const LocalClass = JSON.parse(localStorage.getItem("class"));
            LocalClass.raha = result["rahanmaara"];
            LocalClass.laina = result["lainanmaara"];
            localStorage.setItem("class", JSON.stringify(LocalClass));
            window.location.replace('airporttycoon.html');

        } else {
            alert(result.message);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again later.');
    }
}

