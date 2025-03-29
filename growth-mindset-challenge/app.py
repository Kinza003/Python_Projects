import streamlit as st
import random
import time  # Import time module for delay

# App Title
st.title("🌱 Growth Mindset Challenge")

# Introduction
st.markdown("""### Welcome! 🚀  
This challenge will help you develop a **growth mindset**.  
Each day, you'll receive a new challenge to strengthen your resilience and learning ability! 🎯  
""")

# List of challenges
challenges = [
    "📝 Write about a time you overcame a difficult situation.",
    "🔄 List three things you learned from a past mistake.",
    "💬 Write a positive affirmation about yourself.",
    "🌟 Describe a time you stepped out of your comfort zone.",
    "🎯 Set a small goal for today and plan how to achieve it.",
    "📚 Read an article or book about growth mindset and summarize it.",
    "💡 Share a lesson you learned recently and how it changed your perspective.",
    "🚀 Try something new today and reflect on your experience."
]

# Motivational Messages
motivational_messages = [
    "✨ Great job! Every small effort counts. Keep pushing forward!",
    "🚀 Keep going! You're building a strong mindset every day.",
    "🔥 You did it! Keep challenging yourself to grow.",
    "💪 Growth takes time, but you're on the right path. Stay consistent!",
    "🍀 Every challenge makes you stronger. Believe in yourself!"
]

# Daily Motivational Quote
daily_quotes = [
    "💡 'Challenges are what make life interesting. Overcoming them is what makes life meaningful.'",
    "🌱 'The only way to grow is to step out of your comfort zone.'",
    "🎯 'Success is not final, failure is not fatal: It is the courage to continue that counts.'",
    "💪 'Your mindset determines your success. Keep pushing forward!'"
]

# Initialize session state for progress tracking
if "completed_challenges" not in st.session_state:
    st.session_state.completed_challenges = 0
if "current_challenge" not in st.session_state:
    st.session_state.current_challenge = random.choice(challenges)
if "next_challenge_unlocked" not in st.session_state:
    st.session_state.next_challenge_unlocked = False
if "progress" not in st.session_state:
    st.session_state.progress = 0                     # Progress starts at 0
if "last_completed_challenge" not in st.session_state:
    st.session_state.last_completed_challenge = None  # Track last challenge to prevent duplicate submission
if "user_response" not in st.session_state:
    st.session_state.user_response = ""                 # Store user response

# Display Challenge
st.subheader("📝 Today's Challenge:")
st.write(f"**{st.session_state.current_challenge}**")

# Show Daily Motivational Quote
st.markdown(f"💬 **Motivational Thought of the Day:**\n> {random.choice(daily_quotes)}")

# User Input Section
st.subheader("✍ Your Response:")
user_response = st.text_area("Write your thoughts here...", value=st.session_state.user_response)

# Submit Button
if st.button("✅ Submit Response"):
    if user_response.strip():
        # Check if the same challenge was already completed
        if st.session_state.last_completed_challenge != st.session_state.current_challenge:
            st.session_state.completed_challenges += 1       # Increment progress
            st.session_state.next_challenge_unlocked = True        # Unlock next challenge
            st.session_state.progress = st.session_state.completed_challenges / 5         # Update progress
            st.session_state.last_completed_challenge = st.session_state.current_challenge   # Prevent duplicate submission
            st.session_state.user_response = user_response      # Store user response

            st.success("🎉 Your response has been saved!")

            # Show Completed Challenges Count
            st.write(f"🎯 **Total Challenges Completed: {st.session_state.completed_challenges} / 3**")

            # Show Random Motivational Message
            st.markdown(f"💖 **{random.choice(motivational_messages)}**")

            # Check if 3 challenges are completed and show balloons
            if st.session_state.completed_challenges >= 3:
                st.balloons()  # Show celebration balloons
                st.success("🌟 Congratulations! You've completed 3 challenges! 🌟")
                
                # Delay before reloading the page
                time.sleep(8)       # Give time for balloons to be visible
                st.rerun()          # Reload the page
            
            # Encourage user to return tomorrow
            st.markdown("📢 **Come back tomorrow for a new challenge!**")

            # Refresh app to update UI
            st.rerun()
        else:
            st.warning("⚠ You have already submitted this challenge. Click 'Next Challenge' to continue.")
    else:
        st.warning("⚠ Please write something before submitting.")

# Progress Bar
st.progress(st.session_state.progress)

# Countdown Statement Below Progress Bar
st.write(f"⏳ **Challenges Completed: {st.session_state.completed_challenges} / 3**")

# "Next Challenge" Button - Only active after first challenge is completed
if st.session_state.next_challenge_unlocked:
    if st.button("➡ Get Next Challenge"):
        # Reset progress and refresh page after 5 challenges
        if st.session_state.completed_challenges >= 3:
            st.session_state.completed_challenges = 0  # Reset completed challenges count
            st.session_state.progress = 0  # Reset progress bar
            st.session_state.last_completed_challenge = None  # Reset last completed challenge
            st.session_state.user_response = ""  # Clear the text area
            st.session_state.next_challenge_unlocked = False  # Reset challenge state
            st.rerun()  # Reload the page
        else:
            st.session_state.current_challenge = random.choice(challenges)
            st.session_state.next_challenge_unlocked = False  # Lock the button again
            st.session_state.user_response = ""  # Clear the text area
            st.rerun()  # Refresh the app