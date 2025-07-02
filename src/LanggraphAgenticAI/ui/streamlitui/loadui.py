import streamlit as st
from src.LanggraphAgenticAI.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        # Safely get page title with fallback
        page_title = self.config.get_page_title() or "Agentic Chatbot"

        st.set_page_config(page_title="🤖 " + page_title, layout="wide")
        st.header("🤖 " + page_title)

        with st.sidebar:
            # Load options from config with safe fallbacks
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM Selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            # Groq-specific inputs
            if self.user_controls["selected_llm"] == "Groq":
                model_options = self.config.get_groq_model_options()

                if model_options:
                    self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                else:
                    st.error("No Groq models available. Check your config.")

                # API Key Input (Stored in session state)
                groq_api_key = st.text_input("API Key", type="password")
                st.session_state["GROQ_API_KEY"] = groq_api_key
                self.user_controls["GROQ_API_KEY"] = groq_api_key

                if not groq_api_key:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have one? Visit: https://console.groq.com/keys")

            # Usecase Selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecase", usecase_options)

        return self.user_controls
