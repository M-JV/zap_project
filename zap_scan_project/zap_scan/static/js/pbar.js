// Array of progress bar containers and value containers
const progressBarContainers = document.querySelectorAll('.container .circular-progress');
const valueContainers = document.querySelectorAll('.container .value-container');

// Function to start progress bar animation
function startProgressBar(index, color, maxValue) {
    let progressValue = 0;
    const speed = 90; // Speed of the animation in milliseconds

    // Set an interval to update the progress bar
    const progress = setInterval(() => {
        progressValue++;
        // Update the value container with the current progress percentage
        valueContainers[index].textContent = `${progressValue}`;

        // Update the circular progress bar's background
        progressBarContainers[index].style.background = `conic-gradient(${color} ${progressValue * 3.6}deg, #cadcff ${progressValue * 3.6}deg)`;

        // Clear the interval when the progress reaches the max value
        if (progressValue === maxValue) {
            clearInterval(progress);
        }
    }, speed);
}

// Start progress bar animations for all circular progress bars
progressBarContainers.forEach((_, index) => {
    const container = progressBarContainers[index].closest('.container');
    const color = container.getAttribute('data-color');
    const maxValue = parseInt(container.getAttribute('data-max-value'), 10);
    
    // Start progress bar with the specified color and max value
    startProgressBar(index, color, maxValue);
});
