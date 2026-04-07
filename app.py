import ollama
import streamlit as st

def get_explanation(topic, mode):
    if mode == "eli5":
        prompt = f"""Explain '{topic}' to a 5 year old.
Use a simple real-life analogy.
No jargon. Max 5 bullet points. Short sentences."""
    else:
        prompt = f"""Explain '{topic}' to a senior software engineer.
Be technical and precise. No fluff.
Use structured bullet points."""

    response = ollama.chat(
        model="gemma4:e4b",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content']


st.title("Explain Like I'm 5")
st.caption("Gemma 4:e4b running locally using Ollama")

topic = st.text_input("Enter a topic:", placeholder="e.g. API, Kubernetes, Neural Network")

mode = st.radio("Choose explanation mode:", ["ELI5 (Like I'm 5)", "Senior Engineer"])

if st.button("Explain"):
    if topic.strip() == "":
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Thinking..."):
            selected_mode = "eli5" if "ELI5" in mode else "senior"
            result = get_explanation(topic, selected_mode)
        st.markdown(result)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: grey; font-size: 0.85em;'>DiptoVerse · Building AI . One project at a time<br>©2026</p>",
    unsafe_allow_html=True
)
