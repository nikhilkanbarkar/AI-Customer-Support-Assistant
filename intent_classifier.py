from langchain_core.prompts import ChatPromptTemplate


class IntentClassifier:

    def __init__(self, llm):

        self.llm = llm

        self.prompt = ChatPromptTemplate.from_template(
            """
You are an AI Intent Classifier.

Classify the user's query into ONLY ONE of these categories.

Categories:
- Product Inquiry
- Order Status
- Returns & Refunds
- Technical Support
- General Query

Rules:
- Return ONLY the category name.
- Do not explain.
- Do not add punctuation.
- If unsure, return General Query.

Customer Query:
{query}
"""
        )

    def classify_intent(self, query):

        messages = self.prompt.format_messages(query=query)

        response = self.llm.generate_response(messages)

        valid_intents = [
            "Product Inquiry",
            "Order Status",
            "Returns & Refunds",
            "Technical Support",
            "General Query"
        ]

        response = response.strip()

        if response in valid_intents:
            return response

        return "General Query"