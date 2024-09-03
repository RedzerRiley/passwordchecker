# Real-Time Password Strength Checker

This project is a web-based password strength checker that provides real-time feedback on password strength, including an estimation of how long it would take to crack the password using a brute force attack.

## Features

- Real-time password strength evaluation
- Visual strength meter
- Detailed feedback on how to improve password strength
- Estimated time to crack the password
- Dark-themed, responsive user interface

## How It Works

### Backend (app.py)

The backend is built using Flask, a lightweight Python web framework. Here's how it functions:

1. **Password Strength Checking**: 
   - The `check_password_strength()` function evaluates the password based on several criteria:
     - Length
     - Presence of uppercase letters
     - Presence of lowercase letters
     - Presence of numbers
     - Presence of special characters
   - It assigns a strength rating (Very Weak, Weak, Moderate, Strong, Very Strong) based on these criteria.
   - It also generates feedback on how to improve the password.

2. **Cracking Time Estimation**:
   - The `estimate_cracking_time()` function calculates an estimated time to crack the password using a brute force attack.
   - It considers the character set used in the password and the password length.
   - The estimation assumes a rate of 1 billion guesses per second.

3. **API Endpoint**:
   - The `/check_password` route accepts POST requests with the password.
   - It returns a JSON response with the strength rating, feedback, and estimated cracking time.

### Frontend (index.html and style.css)

The frontend is built with HTML, CSS, and JavaScript. Here's how it works:

1. **User Interface**:
   - A single input field for the password.
   - A strength meter that visually represents the password strength.
   - Displays the strength rating and estimated cracking time.
   - Lists feedback on how to improve the password.

2. **Real-Time Updates**:
   - JavaScript listens for input events on the password field.
   - It uses a debounce function to wait for a short pause in typing before sending a request to the server.
   - This prevents overwhelming the server with requests while the user is actively typing.

3. **API Interaction**:
   - When the password changes, a POST request is sent to the `/check_password` endpoint.
   - The response updates the UI elements: strength meter, strength rating, cracking time, and feedback list.

4. **Styling**:
   - The interface uses a dark theme for better visibility of the strength meter.
   - The strength meter changes color based on the password strength.
   - Responsive design ensures usability on various device sizes.

## Setup and Running

1. Install the required Python packages:
