import streamlit as st
import whisper
import os
from groq import Groq


os.environ["GROQ_API_KEY"] = "............................................."  

client = Groq(api_key=os.environ["GROQ_API_KEY"])

whisper_model = whisper.load_model("base")

# TRANSCRIBE + SUMMARIZE FUNCTION 
def transcribe_and_summarize(audio_path):
    st.info("Transcribing audio...")
    result = whisper_model.transcribe(audio_path)
    transcript = result["text"]

    st.success("Transcription complete!")

    st.info("Summarizing text...")
    prompt = f"Summarize this text:\n{transcript}"

    response = client.chat.completions.create(
     model="llama3-70b-8192",  
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    summary = response.choices[0].message.content.strip()
    return transcript, summary

# STREAMLIT UI 
st.set_page_config(page_title="🎧 AutoTranscript AI", layout="centered")

st.title("🎙️ AutoTranscript AI")
st.markdown("Upload an audio file and get a transcript with a smart summary using **Whisper** + **Groq LLMs**.")

uploaded_file = st.file_uploader("Upload your audio file (mp3/wav)", type=["mp3", "wav"])

if uploaded_file is not None:
    with open("temp_audio.mp3", "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Transcribing and summarizing..."):
        transcript, summary = transcribe_and_summarize("temp_audio.mp3")

    st.success("Done... ")

    st.subheader("📝 Transcript")
    st.markdown(f"<div style='background-color:#efff9c4; padding:15px; border-radius:8px'>{transcript}</div>", unsafe_allow_html=True)

    st.subheader("🧠 Summary")
    st.markdown(f"<div style='background-color:#efff9c4; padding:15px; border-radius:8px'>{summary}</div>", unsafe_allow_html=True)

else:
    st.info("👆 Upload a file to get started.")