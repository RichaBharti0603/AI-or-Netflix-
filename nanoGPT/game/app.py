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
if "difficulty" not in st.session_state: st.session_state.difficulty = "Easy"

# ---------------- Difficulty (do NOT assign to session_state directly) ----------------
difficulty = st.radio(
    "Select difficulty",
    ["Easy", "Medium", "Hard"],
    index=["Easy", "Medium", "Hard"].index(st.session_state.difficulty),
    key="difficulty"  # key links the widget to session_state
)
# Update session state only if changed
st.session_state.difficulty = difficulty

# ---------------- Initialize First Round ----------------
if st.session_state.current_round is None:
    st.session_state.current_round = get_round(st.session_state.difficulty)

# ---------------- Display Dialogue ----------------
st.markdown(f"**Dialogue:** {st.session_state.current_round['dialogue']}")

# ---------------- Choice Buttons ----------------
col1, col2 = st.columns(2)
with col1:
    if st.button("Netflix"):
        st.session_state.user_choice = "Netflix"
with col2:
    if st.button("AI"):
        st.session_state.user_choice = "AI"

# ---------------- Evaluate Choice ----------------
if st.session_state.user_choice:
    correct = st.session_state.user_choice == st.session_state.current_round["source"]
    if correct:
        st.success("Correct! You get the point.")
        st.session_state.score_user += 1
    else:
        st.error(f"Wrong! GPT gets the point. Correct: {st.session_state.current_round['source']}")
        st.session_state.score_gpt += 1

    # Prepare next round
    st.session_state.current_round = get_round(st.session_state.difficulty)
    st.session_state.user_choice = None

# ---------------- Score ----------------
st.markdown(f"**Score → You: {st.session_state.score_user} | GPT: {st.session_state.score_gpt}**")
