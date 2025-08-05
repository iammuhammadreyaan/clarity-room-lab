import streamlit as st
from textblob import TextBlob
import random

st.set_page_config(page_title="🧠 Clarity Room", layout="wide")

# ----------------- EMOTION THEMES -----------------
moods = {
    "happy":    {"emoji": "😄", "bg": "#e6f9f0", "accent": "#2ecc71"},
    "sad":      {"emoji": "😢", "bg": "#e8f1fc", "accent": "#3498db"},
    "angry":    {"emoji": "😡", "bg": "#fdecea", "accent": "#e74c3c"},
    "anxious":  {"emoji": "😰", "bg": "#fff5e6", "accent": "#f39c12"},
    "neutral":  {"emoji": "😐", "bg": "#f9f9f9", "accent": "#95a5a6"}
}

prompts = {
    "happy": [
        "What's bringing you joy today?",
        "Who made you smile recently?",
        "How can you spread this feeling?"
    ],
    "sad": [
        "What’s been heavy on your heart?",
        "Is there something you wish could change?",
        "What small comfort can you give yourself today?"
    ],
    "angry": [
        "What’s fueling your anger right now?",
        "Is there a boundary being crossed?",
        "How can you release this safely?"
    ],
    "anxious": [
        "What are you worrying about?",
        "What’s one calming thing you can do?",
        "Can you reframe your current fear?"
    ],
    "neutral": [
        "What thoughts are passing by today?",
        "What can make this day meaningful?",
        "What are you grateful for right now?"
    ]
}

# ----------------- SENTIMENT -----------------
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

def get_feedback(polarity):
    if polarity > 0.2:
        return "🌈 You're radiating light and positivity."
    elif polarity < -0.2:
        return "💙 It's okay to feel low. You're safe here."
    else:
        return "🧘 You're holding space for yourself — that matters."

# ----------------- CSS STYLING -----------------
st.markdown("""
<style>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700&display=swap');

html, body {
    font-family: 'Inter', sans-serif;
    background-color: transparent;
}

h1, h2, h3, p, label, div, textarea {
    font-family: 'Inter', sans-serif;
}

header {visibility: hidden;}

/* Container */
.card {
    background-color: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.1);
    margin: 2rem auto;
    max-width: 750px;
}

/* Emotion Tab Scroll */
.scroll-box {
    display: flex;
    overflow-x: auto;
    gap: 12px;
    padding: 10px;
    margin-top: 20px;
    margin-bottom: 10px;
}

.scroll-box::-webkit-scrollbar {
    height: 8px;
}
.scroll-box::-webkit-scrollbar-thumb {
    background: #ccc;
    border-radius: 4px;
}

/* Emotion Button */
.mood-btn {
    flex: 0 0 auto;
    border: none;
    padding: 10px 20px;
    border-radius: 50px;
    font-size: 15px;
    cursor: pointer;
    background: #fff;
    box-shadow: 0 2px 5px rgba(0,0,0,0.08);
    transition: 0.3s;
}
.mood-btn:hover {
    background: #eee;
    transform: scale(1.03);
}

/* Buttons */
.stButton > button {
    border-radius: 25px;
    padding: 10px 30px;
    background-color: #000;
    color: white;
    font-size: 16px;
    font-weight: bold;
    border: none;
    transition: 0.3s;
}
.stButton > button:hover {
    background-color: #222;
    transform: scale(1.02);
}

/* Text Area */
textarea {
    border-radius: 16px !important;
    padding: 12px !important;
    font-size: 16px !important;
}
</style>
""", unsafe_allow_html=True)

# ----------------- SESSION -----------------
if "selected_mood" not in st.session_state:
    st.session_state.selected_mood = "neutral"
if "prompts" not in st.session_state:
    st.session_state.prompts = []

mood = st.session_state.selected_mood
theme = moods[mood]
bg = theme["bg"]
accent = theme["accent"]

# ----------------- BACKGROUND -----------------
st.markdown(f"""
    <style>
        .stApp {{
            background-color: {bg};
        }}
    </style>
""", unsafe_allow_html=True)

# ----------------- HEADER -----------------
st.markdown(f"""
<div style='text-align:center; padding-top: 30px;'>
    <h1 style='font-size: 2.6em;'>{theme['emoji']} Clarity Room</h1>
    <p style='font-size: 1.1em; color: #555;'>A clean, calm space to reflect</p>
</div>
""", unsafe_allow_html=True)

# ----------------- EMOTION BUTTON BAR -----------------
st.markdown(f"<div class='scroll-box'>", unsafe_allow_html=True)
for key, data in moods.items():
    clicked = st.button(f"{data['emoji']} {key.capitalize()}", key=key)
    if clicked:
        st.session_state.selected_mood = key
        st.session_state.prompts = random.sample(prompts[key], 2)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------- JOURNAL CARD -----------------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    if st.session_state.prompts:
        st.markdown("### ✍️ Prompts for You:")
        for p in st.session_state.prompts:
            st.write(f"• {p}")

        journal = st.text_area("Your Journal Entry", height=220)

        if st.button("Analyze My Reflection"):
            if journal.strip():
                polarity, subjectivity = analyze_sentiment(journal)
                st.markdown("---")
                st.markdown("#### 📊 Sentiment Analysis")
                st.write(f"**Polarity:** `{polarity:.2f}` | **Subjectivity:** `{subjectivity:.2f}`")
                st.success(get_feedback(polarity))
            else:
                st.warning("Please write something to analyze.")
    else:
        st.info("Choose an emotion to begin journaling.")

    st.markdown("</div>", unsafe_allow_html=True)
