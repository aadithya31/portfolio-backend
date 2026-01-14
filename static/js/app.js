/**
 * Portfolio Application Frontend JavaScript
 * Handles counter functionality similar to React useState
 */

// Wait for DOM to be ready
document.addEventListener('DOMContentLoaded', function () {
    const counterButton = document.getElementById('counter-btn');
    const counterDisplay = document.getElementById('counter-display');

    // Fetch initial counter value
    fetchCounter();

    // Add click handler
    if (counterButton) {
        counterButton.addEventListener('click', incrementCounter);
    }
});

/**
 * Fetch current counter value from API
 */
async function fetchCounter() {
    try {
        const response = await fetch('/api/counter');
        const data = await response.json();
        updateCounterDisplay(data.count);
    } catch (error) {
        console.error('Error fetching counter:', error);
    }
}

/**
 * Increment counter via API POST request
 */
async function incrementCounter() {
    try {
        const response = await fetch('/api/counter', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ increment: 1 })
        });
        const data = await response.json();
        updateCounterDisplay(data.count);
    } catch (error) {
        console.error('Error incrementing counter:', error);
    }
}

/**
 * Update the counter display in the DOM
 * @param {number} count - The current count value
 */
function updateCounterDisplay(count) {
    const counterDisplay = document.getElementById('counter-display');
    if (counterDisplay) {
        counterDisplay.textContent = count;
    }
}
