from langchain_core.messages import HumanMessage, AIMessage

from llm import LLMService
from intent_classifier import IntentClassifier
from knowledge_base import KnowledgeBase
from prompts import build_prompt


class CustomerSupportChat:

    def __init__(self):

        self.llm = LLMService()

        self.classifier = IntentClassifier()

        self.knowledge = KnowledgeBase()

        self.prompt_template = build_prompt()

        self.chat_history = []

    def process_query(self, user_query):

        user_query = user_query.strip()

        if not user_query:

            return (
                "General Query",
                "Please enter a valid question."
            )

        # -----------------------------
        # Detect Intent
        # -----------------------------

        intent = self.classifier.classify_intent(
            user_query
        )

        # -----------------------------
        # Retrieve Knowledge
        # -----------------------------

        knowledge = self.knowledge.get_information(
            intent
        )

        # -----------------------------
        # Build Prompt
        # -----------------------------

        messages = self.prompt_template.format_messages(

            intent=intent,

            knowledge=knowledge,

            question=user_query

        )

        # -----------------------------
        # Add Conversation Memory
        # -----------------------------

        final_messages = []

        final_messages.extend(self.chat_history)

        final_messages.extend(messages)

        # -----------------------------
        # Generate Response
        # -----------------------------

        response = self.llm.generate_response(
            final_messages
        )

        # -----------------------------
        # Save Memory
        # -----------------------------

        self.chat_history.append(

            HumanMessage(content=user_query)

        )

        self.chat_history.append(

            AIMessage(content=response)

        )

        # Keep only recent conversations

        if len(self.chat_history) > 20:

            self.chat_history = self.chat_history[-20:]

        return intent, response

    def clear_history(self):

        self.chat_history = []