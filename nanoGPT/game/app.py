import streamlit as st
from game_engine import get_round

st.set_page_config(page_title="Netflix vs AI", page_icon="🎬")
st.title("🎬 Netflix vs AI")
st.write("Guess correctly before time runs out!")

# ---------------- Session State ----------------
if "score_user" not in st.session_state: st.session_state.score_user = 0
if "score_gpt" not in st.session_state: st.session_state.score_gpt = 0
if "current_round" not in st.session_state: st.session_state.current_round = None
if "user_choice" not in st.session_state: st.session_state.user_choice = None
if "result" not in st.session_state: st.session_state.result = None

# ---------------- Difficulty ----------------
# Use the widget's value directly; do NOT assign to session_state
difficulty = st.radio(
    "Select difficulty",
    ["Easy", "Medium", "Hard"],
    index=0,
    key="difficulty"
)

# ---------------- Start / Next Round ----------------
if st.button("Start / Next Round") or st.session_state.current_round is None:
    st.session_state.current_round = get_round(difficulty)
    st.session_state.user_choice = None
    st.session_state.result = None

# ---------------- Display Dialogue ----------------
if st.session_state.current_round:
    st.markdown(f"**Dialogue:** {st.session_state.current_round['dialogue']}")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Netflix"):
            st.session_state.user_choice = "Netflix"
    with col2:
        if st.button("AI"):
            st.session_state.user_choice = "AI"

# ---------------- Evaluate Choice ----------------
if st.session_state.user_choice and st.session_state.result is None:
    correct = st.session_state.user_choice == st.session_state.current_round["source"]
    if correct:
        st.success("Correct! You get the point.")
        st.session_state.score_user += 1
    else:
        st.error(f"Wrong! GPT gets the point. Correct: {st.session_state.current_round['source']}")
        st.session_state.score_gpt += 1
    st.session_state.result = True

# ---------------- Score ----------------
st.markdown(f"**Score → You: {st.session_state.score_user} | GPT: {st.session_state.score_gpt}**")
