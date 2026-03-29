// Static script.js file

// Function to display current date and time in UTC
function displayDateTime() {
    const now = new Date();
    const utcDate = now.toISOString().slice(0, 19).replace('T', ' ');
    console.log('Current Date and Time (UTC): ' + utcDate);
}

displayDateTime();
