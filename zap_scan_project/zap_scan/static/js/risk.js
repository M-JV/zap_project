// Function to update risk level based on counts of vulnerabilities
function updateRiskLevel(highCount, mediumCount, lowCount) {
    // Get the risk level element
    const riskLevel = document.getElementById('riskLevel');
    
    // Calculate total count
    const totalCount = highCount + mediumCount + lowCount;

    // Define the conditions for each risk level based on counts
    if (highCount >= 5 || mediumCount >= 40) {
        // High risk level
        riskLevel.textContent = 'High';
        riskLevel.className = 'high';
    } else if (mediumCount > 10 || (highCount < 5 && mediumCount >= 30)) {
        // Medium risk level
        riskLevel.textContent = 'Medium';
        riskLevel.className = 'medium';
    } else {
        // Low risk level
        riskLevel.textContent = 'Low';
        riskLevel.className = 'low';
    }
}



// Function to get progress bar values from HTML elements
function getProgressBarValues() {
    // Select the containers for circular progress bars
    const progressBar1 = document.querySelector('.circularProgressBar1 .container');
    const progressBar2 = document.querySelector('.circularProgressBar2 .container');
    const progressBar3 = document.querySelector('.circularProgressBar3 .container');

    // Extract max values from data attributes
    const highCount = parseInt(progressBar1.getAttribute('data-max-value'), 10);
    const mediumCount = parseInt(progressBar2.getAttribute('data-max-value'), 10);
    const lowCount = parseInt(progressBar3.getAttribute('data-max-value'), 10);

    // Call the function to update the risk level based on the counts of vulnerabilities
    updateRiskLevel(highCount, mediumCount, lowCount);
}

// Call the function to get progress bar values and update risk level
getProgressBarValues();
