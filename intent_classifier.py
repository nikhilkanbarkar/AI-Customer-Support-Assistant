class IntentClassifier:
    def __init__(self):
        self.intent_keywords = {
            "Product Inquiry": [
                "product",
                "products",
                "price",
                "cost",
                "buy",
                "purchase",
                "available",
                "stock",
                "laptop",
                "phone",
                "mobile",
                "headphones",
                "keyboard",
                "mouse",
                "smartwatch"
            ],

            "Order Status": [
                "order",
                "track",
                "tracking",
                "delivery",
                "delivered",
                "shipping",
                "shipment",
                "status",
                "dispatch"
            ],

            "Returns & Refunds": [
                "return",
                "refund",
                "replace",
                "replacement",
                "exchange",
                "cancel",
                "money back"
            ],

            "Technical Support": [
                "issue",
                "problem",
                "error",
                "broken",
                "damage",
                "damaged",
                "repair",
                "not working",
                "bug",
                "technical"
            ]
        }

    def classify_intent(self, user_query):
        """
        Classify user intent based on keyword matching.
        """

        user_query = user_query.lower()

        for intent, keywords in self.intent_keywords.items():
            for keyword in keywords:
                if keyword in user_query:
                    return intent

        return "General Query"