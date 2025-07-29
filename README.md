# 🎙️ AutoTranscript AI

AutoTranscript AI is a powerful Streamlit-based tool that transcribes audio files and summarizes the content using **Groq's large language models (LLMs)**. It supports **Urdu and English** audio and provides a clean, minimal UI for seamless interaction.

---

## 🚀 Features

- 🎧 Upload and transcribe `.mp3` or `.wav` audio files
- 🌐 Supports **multilingual audio**, including **Urdu**
- 🧠 Summarizes the transcribed text using **Groq LLMs**
- ⚡ Clean, responsive UI with **Streamlit**
- 🔐 Secure API key integration using `.env`

---

## 📸 Demo

![screenshot](assets/demo.png)  
*Transcribe and summarize audio in one click.*

---

## 🛠️ Tech Stack

| Tool        | Purpose                                  |
|-------------|-------------------------------------------|
| `Streamlit` | Frontend for the web interface            |
| `Whisper`   | OpenAI's ASR model for transcription      |
| `Groq`      | LLMs (like LLaMA3 or Gemma) for summary   |
| `Python`    | Core programming language                 |
| `.env`      | For securely storing API keys             |

---

## 🔧 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/autotranscript-ai.git
cd autotranscript-ai

# Create and activate a virtual environment (if using conda or venv)
conda create -n mypro python=3.11
conda activate mypro


