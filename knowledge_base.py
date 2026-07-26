import json
from pathlib import Path


class KnowledgeBase:
    def __init__(self):
        self.file_path = Path("knowledge/customer_data.json")
        self.knowledge = self.load_knowledge()

    def load_knowledge(self):
        """
        Load the knowledge base from the JSON file.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)

        except FileNotFoundError:
            print("Error: customer_data.json not found.")
            return {}

        except json.JSONDecodeError:
            print("Error: Invalid JSON format in customer_data.json.")
            return {}

        except Exception as e:
            print(f"Unexpected Error: {e}")
            return {}

    def get_information(self, intent):
        """
        Return knowledge for the given intent.
        """
        return self.knowledge.get(
            intent,
            self.knowledge.get("General Query", {})
        )