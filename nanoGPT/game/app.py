import streamlit as st
from ai_generator import load_model
from game_engine import get_round

st.set_page_config(page_title="AI or Human?", layout="centered")

st.title("🤔 AI or Human?")
st.subheader("Would you read this?")

@st.cache_resource
def init_model():
    return load_model()

model, meta = init_model()

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.rounds = 0
    st.session_state.current = None

if st.session_state.current is None:
    st.session_state.current = get_round(model, meta)

text, answer = st.session_state.current

st.markdown(f"> {text}")

col1, col2 = st.columns(2)

if col1.button("✍️ Human"):
    guess = "HUMAN"
elif col2.button("🤖 AI"):
    guess = "AI"
else:
    guess = None

if guess:
    st.session_state.rounds += 1
    if guess == answer:
        st.session_state.score += 1
        st.success("Correct!")
    else:
        st.error(f"Wrong! This was written by {answer}.")
    st.session_state.current = None

st.markdown("---")
st.write(f"**Score:** {st.session_state.score} / {st.session_state.rounds}")
