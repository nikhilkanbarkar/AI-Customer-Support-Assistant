# from knowledge_base import KnowledgeBase

# kb = KnowledgeBase()

# print(kb.get_information("Order Status"))



# from intent_classifier import IntentClassifier

# classifier = IntentClassifier()

# queries = [
#     "Where is my order?",
#     "I want refund",
#     "My laptop is not working",
#     "Do you sell smartwatches?",
#     "Hello"
# ]

# for query in queries:
#     intent = classifier.classify_intent(query)
#     print(f"{query} --> {intent}")





# from prompts import build_prompt

# prompt = build_prompt()

# formatted_prompt = prompt.format_messages(
#     intent="Order Status",
#     knowledge="Orders are delivered within 3-5 business days.",
#     question="Where is my order?"
# )

# print(formatted_prompt)


from llm import LLMService

llm = LLMService()

response = llm.generate_response(
    "Say Hello in one sentence."
)

print(response)