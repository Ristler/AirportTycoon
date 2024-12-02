'use strict';
async function handleLogin(event) {
    event.preventDefault();  // Prevent the default form submission

    // Get form data
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    // Basic validation
    if (!username || !password) {
        alert('Both username and password are required!');
        return;
    }

    // Create a form data object
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    console.log("wtf br", username);

    try {
        // Send the data via a POST request using Fetch API
        const response = await fetch('http://127.0.0.1:5000/login', {
            method: 'POST',
            body: formData,
        });

        // Handle response
        const result = await response.json();

        if (response.ok) {
            alert(`Login successful! Welcome, ${result.user}`);
            
            window.location.replace = 'http://127.0.0.1:5000/airporttycoon.html';

        } else {
            alert(result.message);  // Show the error message
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again later.');
    }
}