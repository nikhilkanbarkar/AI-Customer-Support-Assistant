class IntentClassifier:

    def __init__(self):

        self.intent_keywords = {
            "Product Inquiry": [
                "product", "products", "price", "cost", "buy", "purchase",
                "available", "stock", "laptop", "phone", "mobile",
                "headphone", "keyboard", "mouse", "smartwatch",
                "tablet", "brand", "specification"
            ],

            "Order Status": [
                "order", "track", "tracking", "delivery",
                "shipment", "shipping", "dispatch",
                "status", "parcel"
            ],

            "Returns & Refunds": [
                "return", "refund", "replace",
                "replacement", "exchange",
                "cancel", "money back"
            ],

            "Technical Support": [
                "issue", "problem", "error",
                "bug", "broken", "damage",
                "damaged", "repair",
                "not working", "warranty"
            ],

            "Payment": [
                "payment", "upi", "credit card",
                "debit card", "net banking",
                "cod", "cash on delivery",
                "invoice"
            ],

            "Shipping": [
                "shipping charges",
                "express delivery",
                "international shipping",
                "delivery area",
                "free shipping"
            ],

            "Account": [
                "login", "signup", "register",
                "registration", "password",
                "account", "profile"
            ]
        }

    def classify_intent(self, query):

        query = query.lower()

        for intent, keywords in self.intent_keywords.items():
            for keyword in keywords:
                if keyword in query:
                    return intent

        return "General Query"