import os

from dotenv import load_dotenv

from google import genai

from langchain_google_genai import ChatGoogleGenerativeAI


class LLMService:

    def __init__(self):

        load_dotenv()

        self.api_key = os.getenv("GOOGLE_API_KEY")

        if not self.api_key:

            raise ValueError(
                "GOOGLE_API_KEY not found in .env file."
            )

        os.environ["GOOGLE_API_KEY"] = self.api_key

        try:

            self.client = genai.Client(
                api_key=self.api_key
            )

            self.llm = ChatGoogleGenerativeAI(

                model="gemini-3.1-flash-lite",

                temperature=0.3,

                max_output_tokens=1024

            )

        except Exception as e:

            raise RuntimeError(
                f"Unable to initialize Gemini.\n{e}"
            )

    # ---------------------------------

    def generate_response(self, messages):

        try:

            response = self.llm.invoke(messages)

            content = response.content

            if isinstance(content, str):
                return content.strip()

            if isinstance(content, list):

                final_text = ""

                for item in content:

                    if isinstance(item, dict):
                        final_text += item.get("text", "")

                    else:
                        final_text += str(item)

                return final_text.strip()

            return str(content)

        except Exception as e:

            error = str(e)

            if "API_KEY" in error.upper():

                return (
                    "❌ Invalid Google API Key.\n"
                    "Please check your .env file."
                )

            elif "429" in error:

                return "❌ API quota exceeded."

            elif "503" in error:

                return "❌ Gemini service temporarily unavailable."

            else:

                return f"❌ {error}"
    # ---------------------------------

    def check_connection(self):

        try:

            self.client.models.list()

            return True

        except Exception:

            return False