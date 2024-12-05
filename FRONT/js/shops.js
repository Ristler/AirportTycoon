async function haeKaupat() {
    const response = await fetch('/kaupat');
    const kaupatLista = document.getElementById('kaupat');
    kaupatLista.innerHTML = '';

    if (response.ok) {
        const kaupat = await response.json();
        kaupat.forEach(kauppa => {
            const li = document.createElement('li');
            li.textContent = `ID: ${kauppa.id}, Tyyppi: ${kauppa.tyyppi}, Hinta: ${kauppa.hinta}, Teema: ${kauppa.teema}`;
            const ostaNappi = document.createElement('button');
            ostaNappi.textContent = 'Osta';
            ostaNappi.onclick = () => ostaKauppa(kauppa.id);
            li.appendChild(ostaNappi);
            kaupatLista.appendChild(li);
        });
    } else {
        const error = await response.json();
        kaupatLista.innerHTML = `<li>${error.message}</li>`;
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