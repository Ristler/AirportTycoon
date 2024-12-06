/*uusi päivä -> tarkistalaina*/

async function newday(){
    const response = await fetch('/newday');
    if(response.ok){
        const vastaus = await response.json();
        console.log(vastaus);
    }
}