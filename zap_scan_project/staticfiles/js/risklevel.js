// Function to update risk level
function updateRiskLevel(progress1, progress2) {
    // Get the risk level element
    const riskLevel = document.getElementById('riskLevel');
    
    // Define the conditions for each risk level
    if (progress1 < 10 && progress2 < 40) {
        // Low risk level
        riskLevel.textContent = 'Low';
        riskLevel.className = 'low';
    } else if (progress1 >= 10 && progress1 < 20 && progress2 >= 30 && progress2 < 50) {
        // Medium risk level
        riskLevel.textContent = 'Medium';
        riskLevel.className = 'medium';
    } else if (progress1 <= 10 && progress2 >= 40) {
        // High risk level
        riskLevel.textContent = 'Medium';
        riskLevel.className = 'medium'; 
    } else if (progress1 >= 20 || progress2 >= 40) {
        // High risk level
        riskLevel.textContent = 'High';
        riskLevel.className = 'high';
    } else {
        // Default case (unknown risk level)
        riskLevel.textContent = 'Unknown';
        riskLevel.className = '';
    }
}

// Function to get progress bar values from HTML elements
function getProgressBarValues() {
    // Select the containers for circular progress bars
    const progressBar1 = document.querySelector('.circularProgressBar1 .container');
    const progressBar2 = document.querySelector('.circularProgressBar2 .container');

    // Extract max values from data attributes
    const currentProgressBar1Value = parseInt(progressBar1.getAttribute('data-max-value'), 10);
    const currentProgressBar2Value = parseInt(progressBar2.getAttribute('data-max-value'), 10);

    // Get the values of the progress bars (assuming you have a method to get the current values)
    // This is a placeholder for the actual implementation, as you would need to update these values
    // according to how the progress bars are being used in your application.
    // const currentProgressBar1Value = 5; // Example value (you can replace this with actual value retrieval)
    // const currentProgressBar2Value = 5; // Example value (you can replace this with actual value retrieval)

    // Call the function to update the risk level based on the progress bar values
    updateRiskLevel(currentProgressBar1Value, currentProgressBar2Value);
}

// Call the function to get progress bar values and update risk level
getProgressBarValues();
