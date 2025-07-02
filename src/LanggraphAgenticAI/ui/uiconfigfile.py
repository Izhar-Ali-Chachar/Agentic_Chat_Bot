from configparser import ConfigParser
import os

class Config:
    def __init__(self, config_file="./src/LanggraphAgenticAI/ui/uiconfigfile.ini"):
        if not os.path.isfile(config_file):
            raise FileNotFoundError(f"❌ Config file not found at: {config_file}")

        self.config = ConfigParser()
        files_read = self.config.read(config_file)

        if not files_read:
            raise ValueError(f"⚠️ Failed to read config file at: {config_file}")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE", "Agentic Chatbot")

    def get_llm_options(self):
        return self._parse_list(self.config["DEFAULT"].get("LLM_OPTIONS", ""))

    def get_usecase_options(self):
        return self._parse_list(self.config["DEFAULT"].get("USECASE_OPTIONS", ""))

    def get_groq_model_options(self):
        return self._parse_list(self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS", ""))

    def _parse_list(self, raw_string):
        # Converts "a, b, c" → ["a", "b", "c"]
        return [item.strip() for item in raw_string.split(",") if item.strip()]
