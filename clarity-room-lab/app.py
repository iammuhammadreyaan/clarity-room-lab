import streamlit as st
from textblob import TextBlob
import random

# 🎨 Mood color themes
mood_themes = {
    "happy":    {"color": "#DFFFD6", "accent": "#66BB6A"},
    "sad":      {"color": "#E3F2FD", "accent": "#42A5F5"},
    "angry":    {"color": "#FFEBEE", "accent": "#EF5350"},
    "anxious":  {"color": "#FFF3E0", "accent": "#FFA726"},
    "neutral":  {"color": "#FFFDE7", "accent": "#FDD835"}
}

# 🧠 Prompts
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

# 🔍 Sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment

# 💬 Feedback
def generate_insight(polarity):
    if polarity > 0.2:
        return "🌟 You're in a positive space. Embrace it."
    elif polarity < -0.2:
        return "💙 It's okay to feel low. This space is here for you."
    else:
        return "🧘 You're opening up space for clarity. That matters."

# 🌐 Streamlit UI
def main():
    st.set_page_config(page_title="🧠 Clarity Room", layout="centered")

    # 👇 CSS for circular buttons and minimal feel
    st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
        }
        .stButton > button {
            border-radius: 30px;
            padding: 0.5em 2em;
            font-size: 16px;
            background-color: #ffffff;
            border: 2px solid #888888;
        }
        .stSelectbox > div {
            border-radius: 30px !important;
        }
        .stTextArea > div > textarea {
            border-radius: 20px;
            font-size: 15px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.title("🧠 Clarity Room — Emotional Reflection Lab")
    st.caption("Your personal space for emotional journaling & reflection.")

    mood = st.selectbox("How are you feeling right now?", list(mood_themes.keys()), index=4)

    # 🌈 Theme background color change
    bg_color = mood_themes[mood]["color"]
    accent_color = mood_themes[mood]["accent"]

    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background-color: {bg_color};
        }}
        </style>
        """, unsafe_allow_html=True
    )

    if st.button("✨ Generate Prompts"):
        st.session_state.prompts = random.sample(get_prompt_themes()[mood], 2)

    if "prompts" in st.session_state:
        st.subheader("📝 Reflection Prompts")
        for p in st.session_state.prompts:
            st.write(f"• {p}")

        journal = st.text_area("💬 Your Journal Entry", height=200)

        if st.button("🔍 Analyze My Reflection") and journal:
            sentiment = analyze_sentiment(journal)
            insight = generate_insight(sentiment.polarity)

            st.markdown("---")
            st.markdown("#### 🔍 Sentiment Analysis")
            st.write(f"**Polarity**: `{sentiment.polarity:.2f}`  |  **Subjectivity**: `{sentiment.subjectivity:.2f}`")

            st.markdown("#### 🤖 AI Insight")
            st.success(insight)

if __name__ == "__main__":
    main()
