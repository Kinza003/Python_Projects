import streamlit as st  # importing the streamlit library for creating web app
import random   # importing the random library for generationg random characters
import string   # importing the string library for using string characters
import re  # importing the re library for using regular expressions

# Set tab title and icon
st.set_page_config(page_title="Password Tool", page_icon="🔑")

# Applying custom css for styling
st.markdown("""
    <style>
        /* Centering Content */
            div.block-container {
            padding-top: 50px !important;
            }

        /* Customizing the generated password */
            .stText {
            font-size: 20px;
            font-weight: bold;
            color: #ff4b4b;
            }

        /* Adjusting slider width */
            div[data-testid="stSlider"] {
            width: 60%;
            }

        /* Styling Button */ 
            div.stButton > button {
            background-color: #52c9f9 !important;
            color: white !important; 
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 8px !important;
            border: none !important; 
            cursor: pointer !important; 
            transition: 0.3s !important; 
            }

            div.stButton > button:hover {
            background-color: red !important; 
    </style>
""", unsafe_allow_html=True)


# Sidebar with radio buttons
st.sidebar.title("🔧 Select Tool")
tool = st.sidebar.radio("Choose an option", ["Password Strength Meter", "Password Generator"], index=0)

                        # Password Strength Meter

# function to check password strength
def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("🔴 Password should be at least 8 characters long.")

    # Uppercase and Lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("🔴 Include both uppercase and lowercase letters.")

    # Digits check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("🔴 Include at least one number (0-9).")

    # Check special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("🔴 Include at least one special character.")

    # Score Classification
    if score == 4:
        return "🟢 Strong Password!", suggestions
    elif score == 3:
        return "🟡 Moderate Password - Consider adding more security features.", suggestions
    else:
        return "🔴 Weak Password - Improve it using the suggestions below.", suggestions
    

# Displaying Password Strength Meter
if tool == "Password Strength Meter":
    st.title("🔍 Password Strength Meter")

    # User Input
    password_input = st.text_input("Enter a password to check its strength", type= "password")

    if st.button("Check Strength"):
        if password_input:
            strength, feedback = check_password_strength(password_input)
            st.markdown(f"**Password Strength:** {strength}")

            if feedback: 
                st.write("### 🔹 Suggestions to Improve:")
                for tip in feedback:
                    st.markdown(f"-{tip}")

        else:
            st.warning("❗ Please enter password first.")


                        # Password Generator

# elif tool == "Password Generator":
else:
    # app title
    st.title("🔑 Password Generator")

    # Slider for selecting password length
    length = st.slider("Select Password Length", value= 8, min_value= 6, max_value=20)

    # Checkboxes for password
    use_digits = st.checkbox("Include Digits")
    use_special = st.checkbox("Include Special Characters")

    # Function to generate password based on length provided by user
    def generate_password(length, use_digits, use_special):
        characters = string.ascii_letters

        if use_digits:
            characters += string.digits     # Add digits (0-9)

        if use_special:
            characters += "!@#$%^&*"        # Add special characters (!@#$%^&*)

        return "".join(random.choice(characters) for _ in range(length))

    # Generate password button
    if st.button("Generate Password"):
        password = generate_password(length, use_digits, use_special)
        st.markdown(f"**Generated Password:** <span style='color:green; font-weight:bold;'>{password}</span>", unsafe_allow_html=True)

st.write("-----------------------------------")

st.write("Build with ♥ by [Kinza](https://github.com/Kinza003)")