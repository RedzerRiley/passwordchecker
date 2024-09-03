from flask import Flask, render_template, request, jsonify
import re
import math

app = Flask(__name__)

def estimate_cracking_time(password):
    char_set_size = 0
    if re.search(r"[a-z]", password):
        char_set_size += 26
    if re.search(r"[A-Z]", password):
        char_set_size += 26
    if re.search(r"\d", password):
        char_set_size += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        char_set_size += 32

    if char_set_size == 0:
        return "Instant"

    possible_combinations = char_set_size ** len(password)
    guesses_per_second = 1000000000  # Assuming 1 billion guesses per second

    seconds = possible_combinations / guesses_per_second

    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.2f} days"
    else:
        return f"{seconds/31536000:.2f} years"


def check_password_strength(password):
    # Initialize score
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make the password at least 8 characters long.")

    # Check for uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Check for lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Check for digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # Determine strength based on score
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
        
    cracking_time = estimate_cracking_time(password)

    return strength, feedback, cracking_time

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_password', methods=['POST'])
def check_password():
    password = request.form['password']
    strength, feedback, cracking_time = check_password_strength(password)
    return jsonify({'strength': strength, 'feedback': feedback, 'cracking_time': cracking_time})

if __name__ == '__main__':
    app.run(debug=True)