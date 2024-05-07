console.log("Popup script loaded");

document.addEventListener('DOMContentLoaded', function() {
    console.log("DOMContentLoaded event fired");
});

chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
    console.log("Message received from background script:", message);
    // Handle message and update UI
    if (message.low_count !== undefined) {
        updateAlertCounts(message);
    } else {
        console.log('Received response:', message);
    }
});

function updateAlertCounts(data) {
    if (data.error) {
        console.error('Error:', data.error);
    } else {
        console.log('Scan completed:', data);
        // Display alert counts
        document.getElementById('alertCounts').innerHTML = `
            <p>Low Level Alerts: ${data.low_count}</p>
            <p>Medium Level Alerts: ${data.medium_count}</p>
            <p>High Level Alerts: ${data.high_count}</p>
            <p>Total Alerts: ${data.total_count}</p>
        `;
    }
}
