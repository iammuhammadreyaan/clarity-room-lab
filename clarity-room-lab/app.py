import streamlit as st
from textblob import TextBlob
import random

st.set_page_config(page_title="🧠 Clarity Room", layout="wide")

# ----------------- Emotion Themes -----------------
moods = {
    "happy":    {"emoji": "😄", "bg": "#e8fdf5", "accent": "#2ecc71"},
    "sad":      {"emoji": "😢", "bg": "#f0f4ff", "accent": "#2980b9"},
    "angry":    {"emoji": "😡", "bg": "#ffecec", "accent": "#e74c3c"},
    "anxious":  {"emoji": "😰", "bg": "#fffaf0", "accent": "#f39c12"},
    "neutral":  {"emoji": "😐", "bg": "#f5f5f5", "accent": "#95a5a6"}
}

prompts = {
    "happy": [
        "What’s something that made you smile recently?"
    ],
    "sad": [
        "You’re safe here. Want to share what’s been weighing on your heart?"
    ],
    "angry": [
        "It’s okay to feel anger. Can you describe what caused it?"
    ],
    "anxious": [
        "Let’s slow down. What are you feeling anxious about right now?"
    ],
    "neutral": [
        "Take a moment. What’s on your mind today?"
    ]
}

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

def get_feedback(polarity):
    if polarity > 0.2:
        return "🌟 You’re shining through with something beautiful."
    elif polarity < -0.2:
        return "💙 These feelings are valid. Thank you for sharing them."
    else:
        return "🧘‍♂️ Your reflection holds calm and balance."

# ----------------- CSS Styling -----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
}

.stApp {
    padding: 0 !important;
}

.header-container {
    text-align: center;
    padding: 2rem 1rem 1rem;
}

.big-emoji {
    font-size: 3.5rem;
}

.emotion-card {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin: 2rem 0;
    flex-wrap: wrap;
}

.card-btn {
    background-color: white;
    border-radius: 1rem;
    border: none;
    padding: 1.5rem 2rem;
    font-size: 1.2rem;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transition: 0.3s;
    min-width: 120px;
    text-align: center;
}
.card-btn:hover {
    transform: scale(1.05);
    background-color: #f1f1f1;
}

textarea {
    font-size: 16px !important;
    border-radius: 14px !important;
    padding: 15px !important;
    background: white !important;
    box-shadow: 0 3px 10px rgba(0,0,0,0.05);
}

.stButton>button {
    border-radius: 25px;
    padding: 0.6rem 2rem;
    font-size: 16px;
    font-weight: bold;
    background-color: black;
    color: white;
    border: none;
    margin-top: 1rem;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #222;
    transform: scale(1.02);
}
</style>
""", unsafe_allow_html=True)

# ----------------- Session Setup -----------------
if "selected_mood" not in st.session_state:
    st.session_state.selected_mood = None

# ----------------- Main UI -----------------
mood = st.session_state.selected_mood
bg = moods[mood]["bg"] if mood else "#ffffff"

st.markdown(f"""
    <style>
        .stApp {{
            background-color: {bg};
        }}
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='header-container'>", unsafe_allow_html=True)
st.markdown("<h1>🧠 Clarity Room</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#555; font-size:1.1rem;'>Your private emotional reflection space</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------- Emotion Selection -----------------
st.markdown("#### 💬 How are you feeling right now?")
st.markdown("<div class='emotion-card'>", unsafe_allow_html=True)

for key, data in moods.items():
    if st.button(f"{data['emoji']} {key.capitalize()}"):
        st.session_state.selected_mood = key

st.markdown("</div>", unsafe_allow_html=True)

# ----------------- Journaling Area -----------------
if st.session_state.selected_mood:
    mood = st.session_state.selected_mood
    prompt = prompts[mood][0]
    accent = moods[mood]["accent"]

    st.markdown(f"<h3 style='color:{accent};'>{prompt}</h3>", unsafe_allow_html=True)
    journal = st.text_area("Type here...", height=250)

    if st.button("🧠 Analyze My Reflection"):
        if journal.strip():
            polarity, subjectivity = analyze_sentiment(journal)
            st.markdown("----")
            st.markdown("### 📊 Insight")
            st.write(f"**Polarity:** `{polarity:.2f}` | **Subjectivity:** `{subjectivity:.2f}`")
            st.success(get_feedback(polarity))
        else:
            st.warning("Your heart has something to say. Try writing something.")
