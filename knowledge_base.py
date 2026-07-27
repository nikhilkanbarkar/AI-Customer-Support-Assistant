import json
from pathlib import Path


class KnowledgeBase:

    def __init__(self):

        self.file_path = (
            Path(__file__).parent
            / "knowledge"
            / "customer_data.json"
        )

        self.data = self.load_data()

    # --------------------------------------------

    def load_data(self):

        try:

            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        except FileNotFoundError:

            print(
                "Knowledge Base file not found."
            )

            return {}

        except json.JSONDecodeError:

            print(
                "Invalid JSON format."
            )

            return {}

        except Exception as e:

            print(e)

            return {}

    # --------------------------------------------

    def get_information(self, intent):

        if intent in self.data:

            info = self.data[intent]

            if isinstance(info, dict):

                text = ""

                for key, value in info.items():

                    if isinstance(value, list):

                        value = ", ".join(
                            str(v) for v in value
                        )

                    text += (
                        f"{key.replace('_',' ').title()}: "
                        f"{value}\n"
                    )

                return text

            return str(info)

        return (
            "No relevant information found "
            "for this query."
        )

    # --------------------------------------------

    def reload(self):

        self.data = self.load_data()

    # --------------------------------------------

    def available_categories(self):

        return list(self.data.keys())

    # --------------------------------------------

    def has_category(self, category):

        return category in self.data

    # --------------------------------------------

    def get_all_data(self):

        return self.data