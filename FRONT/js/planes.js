async function haeLentokoneet() {
    const response = await fetch('/planes');
    const lentokoneLista = document.getElementById('planes');
    lentokoneLista.innerHTML = '';

    if (response.ok) {
        const planes = await response.json();
        planes.forEach(plane => {
            const li = document.createElement('li');


            //{"id": lentokone[0], "tyyppi": lentokone[1], "kapasiteetti": lentokone[2],
            //"hinta": lentokone[3], "efficiency": lentokone[4], "maxfuel": lentokone[5] }

            //EDIT THIS TO MAKE WORK, CHECK DATABASE
            li.textContent = `ID: ${plane.id}, Tyyppi: ${plane.tyyppi}, Kapasiteetti: ${plane.kapasiteetti},
            Hinta: ${plane.hinta}, Efficiency: ${plane.efficiency}, Max fuel: ${plane.maxfuel}`;

            const ostaNappi = document.createElement('button');
            ostaNappi.textContent = 'Osta';
            ostaNappi.onclick = () => ostaLentokone(plane.id);
            li.appendChild(ostaNappi);
            lentokoneLista.appendChild(li);
        });
    } else {
        const error = await response.json();
        lentokoneLista.innerHTML = `<li>${error.message}</li>`;
    }
}

async function ostaKauppa(shopId) {
    const response = await fetch('/osta_kauppa', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ shop_id: shopId })
    });
    const viesti = document.getElementById('viesti');
    const data = await response.json();
    viesti.textContent = data.message;
}