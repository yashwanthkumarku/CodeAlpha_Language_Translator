
import streamlit as st  # If unresolved, run: pip install streamlit
import requests  # If unresolved, run: pip install requests
from gtts import gTTS
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

st.markdown("""
<style>
    .main {
        background-color: #f5f7fb;
    }

    h1 {
        color: #1f4e79;
        text-align: center;
    }

    .stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 45px;
        font-weight: bold;
    }

    .stTextArea textarea {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌍 AI Language Translator")

st.markdown(
    "<h4 style='text-align:center;'>"
    "Break Language Barriers with AI"
    "</h4>",
    unsafe_allow_html=True
)

st.write(
    "Translate text between multiple languages "
    "with instant results and speech playback."
)

st.divider()

# Language dictionary
languages = {
    "English": "en",
    "Kannada": "kn",
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja"
}

if "history" not in st.session_state:
    st.session_state.history = []

st.divider()
st.subheader("📜 Translation History")

if st.session_state.history:
    for item in reversed(st.session_state.history[-5:]):
        with st.expander(
            f"{item['source']} → {item['target']}"
        ):
            st.write("Original:")
            st.write(item["original"])

            st.write("Translated:")
            st.write(item["translated"])

    if st.button("Clear History"):
        st.session_state.history = []
        st.rerun()
else:
    st.info("No translation history yet.")
    
# Set default language selections
if "source_language" not in st.session_state:
    st.session_state.source_language = "English"

if "target_language" not in st.session_state:
    st.session_state.target_language = "Kannada"


# Swap selected languages
def swap_languages():
    source = st.session_state.source_language
    target = st.session_state.target_language

    st.session_state.source_language = target
    st.session_state.target_language = source

# Translation function
@st.cache_data(ttl=3600)
def translate_text(text, source, target):

    url = "https://api.mymemory.translated.net/get"

    params = {
        "q": text,
        "langpair": f"{source}|{target}"
    }

    response = requests.get(
        url,
        params=params,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    if data.get("responseStatus") != 200:
        raise ValueError(
            data.get("responseDetails", "Translation failed")
        )

    translated_text = data["responseData"]["translatedText"]

    return translated_text


# User input
text = st.text_area(
    "Enter your text:",
    placeholder="Type something here..."
)

# Language selection
col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "Source Language",
        list(languages.keys()),
        key="source_language"
    )

with col2:
    target = st.selectbox(
        "Target Language",
        list(languages.keys()),
        key="target_language"
    )

st.button(
    "⇄ Swap Languages",
    on_click=swap_languages
)

# Translation button
if st.button("Translate", type="primary"):

    if not text.strip():
        st.warning("Please enter some text.")

    elif len(text.encode("utf-8")) > 500:
        st.warning("Please enter shorter text (maximum 500 bytes).")

    elif source == target:
        st.warning("Select two different languages.")

    else:
        try:
            with st.spinner("Translating..."):

                result = translate_text(
                    text,
                    languages[source],
                    languages[target]
                )

            st.success("Translation completed!")
            st.session_state.history.append({
                "source": source,
                "target": target,
                "original": text,
                "translated": result
            })

            st.subheader("Translated Text")
            st.write(result)

            st.code(result)
            # Text-to-Speech
            st.subheader("🔊 Listen to Translation")

            try:
                audio_buffer = BytesIO()

                speech = gTTS(
                    text=result,
                    lang=languages[target]
                )

                speech.write_to_fp(audio_buffer)

                st.audio(
                    audio_buffer.getvalue(),
                    format="audio/mp3"
                )

            except Exception as error:
                st.warning(f"Audio generation failed: {error}")

        except requests.exceptions.Timeout:
            st.error("Translation service timed out. Try again.")

        except requests.exceptions.RequestException as error:
            st.error(f"Network/API error: {error}")

        except (ValueError, KeyError) as error:
            st.error(f"Translation error: {error}")
