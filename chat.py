from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from intent_classifier import IntentClassifier
from knowledge_base import KnowledgeBase
from prompts import build_prompt
from llm import LLMService


class CustomerSupportChat:

    def __init__(self):
        self.console = Console()

        self.classifier = IntentClassifier()
        self.knowledge = KnowledgeBase()
        self.prompt_template = build_prompt()
        self.llm = LLMService()

    def welcome(self):
        self.console.print(
            Panel.fit(
                "[bold cyan]🤖 AI Customer Support Assistant[/bold cyan]\n\n"
                "Ask any customer support question.\n\n"
                "[yellow]Type 'exit', 'quit', or 'bye' to end the chat.[/yellow]",
                title="Welcome",
                border_style="green"
            )
        )

    def goodbye(self):
        self.console.print(
            "\n[bold green]Thank you for using AI Customer Support Assistant![/bold green]"
        )

    def process_query(self, user_query):

        intent = self.classifier.classify_intent(user_query)

        knowledge = self.knowledge.get_information(intent)

        prompt = self.prompt_template.format_messages(
            intent=intent,
            knowledge=knowledge,
            question=user_query
        )

        response = self.llm.generate_response(prompt)

        return intent, response

    def start_chat(self):

        self.welcome()

        while True:

            try:

                user_query = Prompt.ask(
                    "\n[bold blue]You[/bold blue]"
                ).strip()

                if not user_query:
                    self.console.print(
                        "[red]Please enter a valid question.[/red]"
                    )
                    continue

                if user_query.lower() in ["exit", "quit", "bye"]:

                    self.goodbye()
                    break

                intent, response = self.process_query(user_query)

                self.console.print(
                    f"\n[bold magenta]Detected Intent:[/bold magenta] {intent}"
                )

                self.console.print(
                    f"\n[bold green]Assistant:[/bold green]\n{response}"
                )

            except KeyboardInterrupt:

                self.goodbye()
                break

            except Exception as e:

                self.console.print(
                    f"[bold red]Error:[/bold red] {e}"
                )