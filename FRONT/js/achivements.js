// Load user data from localStorage
const userData = JSON.parse(localStorage.getItem("class"));
const userLocal = userData.user;
const moneyLocal = userData.raha;
const lainaLocal = userData.laina;

// Navbar user info
document.querySelector("#player").innerHTML = `Player: ${userLocal}`;
document.querySelector("#money").innerHTML = `Money: ${moneyLocal}$`;
document.querySelector("#loans").innerHTML = `Loans: ${lainaLocal}$`;

/**
 * Fetch achievements for a specific player.
 * @param {number} playerId - The ID of the player.
 */
async function fetchAchievements(playerId) {
    try {
        const response = await fetch(`/achievements?id=${playerId}`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
        });

        if (!response.ok) {
            const error = await response.json();
            console.error("Error fetching achievements:", error.message);
            return;
        }

        const achievements = await response.json();
        console.log("Achievements:", achievements);
    } catch (error) {
        console.error("Failed to fetch achievements:", error);
    }
}

/**
 * Trigger the "First Flight" achievement.
 * @param {number} playerId - The ID of the player.
 */
async function firstFlight(playerId) {
    try {
        const response = await fetch('/first_flight', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id: playerId }),
        });

        const result = await response.json();
        console.log("First Flight Result:", result);
    } catch (error) {
        console.error("Failed to trigger First Flight achievement:", error);
    }
}

/**
 * Update or check the "Frequent Flyer" achievement.
 * @param {number} playerId - The ID of the player.
 * @param {boolean} lennetty - Indicates whether the player has flown recently.
 */
async function frequentFlyer(playerId, lennetty) {
    try {
        const response = await fetch('/frequent_flyer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id: playerId, lennetty }),
        });

        const result = await response.json();
        console.log("Frequent Flyer Result:", result);
    } catch (error) {
        console.error("Failed to update Frequent Flyer achievement:", error);
    }
}

/**
 * Trigger the "Packed Planes" achievement.
 * @param {number} playerId - The ID of the player.
 * @param {number} matkustajat - Number of passengers.
 * @param {number} kapasiteetti - Plane capacity.
 */
async function packedPlanes(playerId, matkustajat, kapasiteetti) {
    try {
        const response = await fetch('/packed_planes', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id: playerId, matkustajat, kapasiteetti }),
        });

        const result = await response.json();
        console.log("Packed Planes Result:", result);
    } catch (error) {
        console.error("Failed to trigger Packed Planes achievement:", error);
    }
}

/**
 * Check if the "Millionaire" achievement has been reached.
 * @param {number} playerId - The ID of the player.
 */
async function millionaire(playerId) {
    try {
        const response = await fetch('/millionares', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id: playerId }),
        });

        const result = await response.json();
        console.log("Millionaire Achievement Result:", result);
    } catch (error) {
        console.error("Failed to check Millionaire achievement:", error);
    }
}

/**
 * Increment progress for the "Smooth Operation" achievement.
 * @param {number} playerId - The ID of the player.
 */
async function smoothOperation(playerId) {
    try {
        const response = await fetch('/smooth_operation', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id: playerId }),
        });

        const result = await response.json();
        console.log("Smooth Operation Achievement Result:", result);
    } catch (error) {
        console.error("Failed to update Smooth Operation achievement:", error);
    }
}

/**
 * Trigger the "Debt Free" achievement.
 * @param {number} playerId - The ID of the player.
 */
async function debtFree(playerId) {
    try {
        const response = await fetch('/debt_free', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id: playerId }),
        });

        const result = await response.json();
        console.log("Debt Free Achievement Result:", result);
    } catch (error) {
        console.error("Failed to trigger Debt Free achievement:", error);
    }
}

/**
 * Trigger the "Airport Tycoon" achievement.
 * @param {number} playerId - The ID of the player.
 */
async function airportTycoon(playerId) {
    try {
        const response = await fetch('/airport_tycoon', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id: playerId }),
        });

        const result = await response.json();
        console.log("Airport Tycoon Achievement Result:", result);
    } catch (error) {
        console.error("Failed to trigger Airport Tycoon achievement:", error);
    }
}

// Example usage
const playerId = 1; // Replace with the actual player ID
fetchAchievements(playerId);
firstFlight(playerId);
frequentFlyer(playerId, true);
packedPlanes(playerId, 150, 150);
millionaire(playerId);
smoothOperation(playerId);
debtFree(playerId);
airportTycoon(playerId);