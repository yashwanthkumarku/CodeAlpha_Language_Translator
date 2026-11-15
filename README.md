# 🌍 AI Language Translator

An interactive language translation application built using Python and Streamlit. It uses the MyMemory Translation API to translate text between multiple languages.

## 🚀 Features

- Translate text between multiple languages.
- Select source and target languages.
- Swap source and target languages.
- Copy translated text.
- Listen to translated text using Text-to-Speech.
- View recent translation history.
- Clear translation history.
- Input validation and error handling.
- Simple and user-friendly interface.

## 🛠️ Technologies Used

- Python
- Streamlit
- Requests
- MyMemory Translation API
- gTTS (Google Text-to-Speech)

## 📁 Project Structure

```text
CodeAlpha_Language_Translator/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd CodeAlpha_Language_Translator
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment (Windows)

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal.

## 🔌 Translation API

This project uses the MyMemory Translation API.

API endpoint:

`https://api.mymemory.translated.net/get`

The free service has usage limits and requires an internet connection. Availability and translation quality may vary.

## 🔊 Text-to-Speech

The application uses gTTS to generate speech from translated text. An internet connection is required.

## 🎯 Project Objective

The objective of this project is to develop a practical language translation application that makes communication across different languages easier.

## 👨‍💻 Internship Project

Developed as part of the CodeAlpha Artificial Intelligence Internship.

## 📌 Future Improvements

- Add more supported languages.
- Improve translation history management.
- Add voice input.
- Improve responsive UI.
- Explore additional translation API providers.