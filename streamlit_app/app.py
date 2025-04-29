import streamlit as st
import requests
import time

# Page setup
st.set_page_config(page_title="What Beats Rock?", layout="centered")
st.title("What Beats Rock?")

# Seed state management
if "next_seed" in st.session_state:
    st.session_state["seed"] = st.session_state.pop("next_seed")
if "seed" not in st.session_state:
    st.session_state["seed"] = "rock"

# Restart button
if st.button("Restart"):
    st.session_state["seed"] = "rock"

# Guess form
with st.form("guess_form"):
    session_id = st.text_input("Player Name", value="player1")
    seed = st.text_input("Seed Word", value=st.session_state["seed"], key="seed")
    guess = st.text_input("Your Guess")
    submitted = st.form_submit_button("Submit Guess")

# Handle guess
if submitted:
    if not all([session_id, seed, guess]):
        st.warning("Please fill in all fields.")
    else:
        try:
            res = requests.post(
                "http://localhost:8000/guess",
                json={"session_id": session_id, "seed": seed, "guess": guess}
            ).json()

            st.subheader("Result")
            st.markdown(f"{res['verdict']}")

            st.subheader("Current Score")
            st.markdown(f"{res['score']}")

            if res["history"]:
                st.subheader("Guess History")
                st.write(res["history"])

            # 🎯 Feedback based on verdict
            if "beats" in res["verdict"]:
                st.success("Nice move! Keep going!")
                st.balloons()
            elif "does not beat" in res["verdict"]:
                st.error("Wrong guess. Try something else!")
            elif "Game Over" in res["verdict"]:
                st.error("Game Over. Restart to try again.")
            elif "inappropriate" in res["verdict"].lower():
                st.warning("Please use clean language.")

            if "next_seed" in res:
                time.sleep(3)
                st.session_state["next_seed"] = res["next_seed"]
                st.rerun()

        except Exception as e:
            st.error(f"Backend error: {e}")
