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
            
            
            alert(`Loan accepted.`);
           
            window.location.replace('airporttycoon.html');

        } else {
            alert(result.message);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again later.');
    }
}
