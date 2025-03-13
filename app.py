import streamlit as st
import re
import random

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", feedback, "green"
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", feedback, "orange"
    else:
        return "❌ Weak Password - Improve it using the suggestions above.", feedback, "red"

# Function to generate a strong password
def suggest_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.sample(characters, 12))  # Generate a 12-character password

# Streamlit UI
st.title("🔐 Password Strength Meter")

# Input field for password
password = st.text_input("Enter your password:", type="password")

if st.button("Check Password Strength"):
    if password:
        strength, suggestions, color = check_password_strength(password)
        st.markdown(f"<h3 style='color:{color};'>{strength}</h3>", unsafe_allow_html=True)
        
        for suggestion in suggestions:
            st.write(suggestion)
        
        if "Weak" in strength:
            st.write("🔑 Suggested Strong Password: **" + suggest_password() + "**")
    else:
        st.warning("⚠️ Please enter a password to check!")

# Footer
st.markdown("---")
st.write("🔹 Developed with ❤️ using Streamlit")
