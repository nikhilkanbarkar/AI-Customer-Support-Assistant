class IntentClassifier:

    def __init__(self):

        self.intent_keywords = {

            "Product Inquiry": [

                "product",
                "products",
                "item",
                "items",
                "buy",
                "purchase",
                "available",
                "availability",
                "stock",
                "price",
                "cost",
                "offer",
                "discount",
                "laptop",
                "phone",
                "mobile",
                "tablet",
                "headphone",
                "keyboard",
                "mouse",
                "smartwatch",
                "brand",
                "model",
                "specification",
                "specifications"

            ],

            "Order Status": [

                "order",
                "ordered",
                "track",
                "tracking",
                "shipment",
                "shipping",
                "dispatch",
                "delivered",
                "delivery",
                "parcel",
                "package",
                "where is my order",
                "where is my package",
                "status"

            ],

            "Returns & Refunds": [

                "return",
                "refund",
                "replace",
                "replacement",
                "exchange",
                "cancel",
                "cancellation",
                "money back",
                "refund status"

            ],

            "Technical Support": [

                "issue",
                "problem",
                "error",
                "bug",
                "crash",
                "broken",
                "damage",
                "damaged",
                "repair",
                "fix",
                "not working",
                "warranty",
                "support"

            ],

            "Payment": [

                "payment",
                "pay",
                "upi",
                "credit card",
                "debit card",
                "visa",
                "mastercard",
                "net banking",
                "cash on delivery",
                "cod",
                "invoice",
                "billing"

            ],

            "Shipping": [

                "shipping charges",
                "shipping cost",
                "delivery charges",
                "international shipping",
                "express delivery",
                "same day delivery",
                "delivery location",
                "deliver to",
                "free shipping"

            ],

            "Account": [

                "login",
                "log in",
                "signup",
                "sign up",
                "register",
                "registration",
                "account",
                "profile",
                "password",
                "reset password",
                "forgot password",
                "username"

            ]

        }

    # -----------------------------------------------------

    def classify_intent(self, query):

        query = query.lower().strip()

        scores = {}

        for intent, keywords in self.intent_keywords.items():

            score = 0

            for keyword in keywords:

                if keyword in query:

                    score += 1

            scores[intent] = score

        best_intent = max(
            scores,
            key=scores.get
        )

        if scores[best_intent] == 0:

            return "General Query"

        return best_intent

    # -----------------------------------------------------

    def available_intents(self):

        return list(
            self.intent_keywords.keys()
        ) + ["General Query"]