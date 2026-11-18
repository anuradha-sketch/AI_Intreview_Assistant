import stremlit as st
from groq import Groq
st.set_page_config(page_title = "Placement Practice" , layout = "centered")
st.title("AI INTERVIEW ASSISTANT")
st.caption("Practice and prepare for your interview")
try:
  client = Groq(api_key = st.secrets("GROQ_API_KEY"))
except (keyerror, FileNoteFound):
  st.error("API Key is missing. Add it in Advanced settings")
