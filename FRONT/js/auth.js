'use strict';

function isNew() {
    return true
}

async function handleLogin(event) {
    event.preventDefault();  


    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
 
    if (!username || !password) {
        alert('Both username and password are required!');
        return;
    }

    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    


    try {
    
        const response = await fetch('http://127.0.0.1:5000/login', {
            method: 'POST',
            body: formData,
        });

    
        const result = await response.json();
        console.log(result)
        


        if (response.ok) {
            

            localStorage.setItem("class", JSON.stringify(result));
            console.log(localStorage.getItem("class"));
            //kun haluat hakea classii (localstorage.getitem) muista käyttää json.parsee
            /*localStorage.setItem("userId", result.id)
            localStorage.setItem("username", result.user)
            localStorage.setItem("raha", result.raha)
            localStorage.setItem("laina", result.laina)
            localStorage.setItem("Eräpäivä", result.erapaiva)
            localStorage.setItem("Päivä", result.paiva)
            localStorage.setItem("rating", result.rating)*/
            
            alert(`Login successful! Welcome, ${result.user}`);
           
            window.location.replace('airporttycoon.html');
            

        } else {
            alert(result.message);  
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again later.');
    }
}





async function handleRegister(event) {
    event.preventDefault();  


    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    console.log("userrrr", username)
    console.log("userrrr", password)
    

    if (!username || !password) {
        alert('Both username and password are required!');
        return;
    }


   
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    


    try {
      
        const response = await fetch('http://127.0.0.1:5000/createplayer', {
            method: 'POST',
            body: formData,
        });

        const result = await response.json();
        console.log(result)
        


        if (response.ok) {
            localStorage.setItem("class", JSON.stringify(result));
            
            //kun haluat hakea classii (localstorage.getitem) muista käyttää json.parsee
            /*localStorage.setItem("userId", result.id)
            localStorage.setItem("username", result.user)
            localStorage.setItem("raha", result.raha)
            localStorage.setItem("laina", result.laina)
            localStorage.setItem("Eräpäivä", result.erapaiva)
            localStorage.setItem("Päivä", result.paiva)
            localStorage.setItem("rating", result.rating)*/
            
            alert(`Register successful! Welcome, ${result.user}`);
           
            window.location.replace('airporttycoon.html');
            
            

        } else {
            alert(result.message);  // Show the error message
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again later.');
    }
}


