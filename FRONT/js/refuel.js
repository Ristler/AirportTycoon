async function haeLentokoneet() {
    const response = await fetch('/planes');
    const lentokoneLista = document.getElementById('planes');
    lentokoneLista.innerHTML = '';

    if (response.ok) {
        const planes = await response.json();
        planes.forEach(plane => {
            const article = document.createElement('article');
            article.classList.add('planeCard');
           
            article.textContent = `ID: ${plane.id}, Type: ${plane.tyyppi}, Capacity: ${plane.kapasiteetti},
            Price: ${plane.hinta}, Efficiency: ${plane.efficiency}, Max fuel: ${plane.maxfuel}`;

            const refuelNappi = document.createElement('button');
            refuelNappi.textContent = 'Osta';
            refuelNappi.onclick = () => refuel(plane.id);
            article.appendChild(refuelNappi);
            lentokoneLista.appendChild(article);
            

        });
    
    } else {
        const error = await response.json();
        lentokoneLista.innerHTML = `<li>${error.message}</li>`;
    }
}

async function refuel(planeId) {
    const response = await fetch('/refuel', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ plane_id: planeId })
    });
    const data = await response.json();
    alert(data.message)
    haeLentokoneet()
}

haeLentokoneet()