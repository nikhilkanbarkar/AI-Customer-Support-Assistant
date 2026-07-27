import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


class LLMService:
    def __init__(self):
        load_dotenv()

        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError(
                "GOOGLE_API_KEY not found. Please check your .env file."
            )

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3.1-flash-lite",
            google_api_key=api_key,
            temperature=0.3,
        )

    def generate_response(self, prompt):
        """
        Generate a response from Gemini.
        """
        try:
            response = self.llm.invoke(prompt)

            if isinstance(response.content, list):
                for item in response.content:
                    if isinstance(item, dict) and item.get("type") == "text":
                        return item.get("text", "")

            return response.content

        except Exception as e:
            return f"Error: {e}"