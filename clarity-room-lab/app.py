
import streamlit as st
from textblob import TextBlob
import random

# 🧠 Define prompt themes
def get_prompt_themes():
    return {
        "sad": [
            "What are you feeling right now, and why?",
            "What do you wish someone understood about your feelings?",
            "What can help you feel slightly better in this moment?"
        ],
        "happy": [
            "What's bringing you joy today?",
            "Who or what made you smile recently?",
            "How can you spread this positivity forward?"
        ],
        "angry": [
            "What triggered this anger?",
            "Is this reaction protecting something important to you?",
            "What would help release this anger safely?"
        ],
        "anxious": [
            "What thoughts are making you uneasy?",
            "What's one small thing you can control today?",
            "Can you reframe this thought with kindness?"
        ],
        "neutral": [
            "How do you feel in your body right now?",
            "What would make this day feel more meaningful?",
            "What are you grateful for today?"
        ]
    }

# 📊 Sentiment analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment

# 💬 AI reflection
def generate_insight(polarity):
    if polarity > 0.2:
        return "🌟 It sounds like you're in a positive place. Hold on to this energy."
    elif polarity < -0.2:
        return "💙 It's okay to feel this way. You've done well by opening up."
    else:
        return "🧘 Thank you for sharing. You're creating space for clarity."

# 🌐 Streamlit UI
def main():
    st.set_page_config(page_title="🧠 Clarity Room", layout="centered")
    st.title("🧠 Clarity Room — Emotional Reflection Lab")
    st.write("Welcome to your private space for guided emotional journaling.")

    mood = st.selectbox("How are you feeling right now?", ["happy", "sad", "angry", "anxious", "neutral"])
    if st.button("Generate Prompts"):
        prompts = random.sample(get_prompt_themes()[mood], 2)
        st.session_state.prompts = prompts

    if "prompts" in st.session_state:
        st.subheader("📝 Reflection Prompts")
        for p in st.session_state.prompts:
            st.write(f"- {p}")

        journal_entry = st.text_area("💬 Your Journal Entry", height=200)
        if st.button("Analyze My Reflection") and journal_entry:
            sentiment = analyze_sentiment(journal_entry)
            insight = generate_insight(sentiment.polarity)

            st.subheader("🔍 Sentiment Analysis")
            st.write(f"Polarity: `{sentiment.polarity:.2f}` | Subjectivity: `{sentiment.subjectivity:.2f}`")

            st.subheader("🤖 AI Insight")
            st.success(insight)

if __name__ == "__main__":
    main()
