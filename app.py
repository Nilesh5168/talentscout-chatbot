import streamlit as st
from prompts import generate_questions_prompt, get_llm_response
from utils import is_exit_command

st.set_page_config(page_title="TalentScout Hiring Assistant")


if "conversation" not in st.session_state:
    st.session_state["conversation"] = []

st.title("TalentScout Hiring Assistant")
st.markdown("Welcome! I will help screen your profile based on your tech stack.")


st.info("Hello! I’m your virtual hiring assistant. Let's get started.")


with st.form("candidate_info"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    experience = st.text_input("Years of Experience")
    position = st.text_input("Desired Position(s)")
    location = st.text_input("Current Location")
    tech_stack = st.text_input("Tech Stack (comma-separated: Python, React, MySQL...)")
    submitted = st.form_submit_button("Start Chat")

if submitted:
    st.session_state["info"] = {
        "name": name,
        "email": email,
        "phone": phone,
        "experience": experience,
        "position": position,
        "location": location,
        "tech_stack": tech_stack
    }

    st.success("Thank you! Generating your technical questions...")
    prompt = generate_questions_prompt(st.session_state["info"])
    response = get_llm_response(prompt)
    st.session_state["conversation"].append(("Assistant", response))


for role, msg in st.session_state["conversation"]:
    st.chat_message(role).write(msg)


if st.session_state.get("info"):
    user_input = st.chat_input("Ask something or type 'exit' to end")
    if user_input:
        if is_exit_command(user_input):
            st.success("Thank you! We'll be in touch.")
        else:
            response = get_llm_response(user_input)
            st.session_state["conversation"].append(("User", user_input))
            st.session_state["conversation"].append(("Assistant", response))
