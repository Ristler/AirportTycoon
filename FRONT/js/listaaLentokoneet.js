async function listaaLentokoneet() {
    const response = await fetch('/listaa_lentokoneet');
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


            const valitseNappi = document.createElement('button');

            valitseNappi.textContent = 'Valitse';

            valitseNappi.onclick = () => valitseLentokone(plane.id);
            li.appendChild(valitseNappi);
            
            lentokoneLista.appendChild(li);
        });
    } else {
        const error = await response.json();
        lentokoneLista.innerHTML = `<li>else lausekke help error:${error.message}</li>`;
    }
}

async function valitseLentokone(planeId) {
    const response = await fetch('/valitse_lentokone', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ plane_id: planeId })
    });
    const viesti = document.getElementById('viesti');
    const data = await response.json();
    viesti.textContent = data.message;
}