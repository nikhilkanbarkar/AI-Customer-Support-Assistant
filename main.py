import subprocess
import sys


def main():

    print("=" * 55)
    print("🤖 AI Customer Support Assistant")
    print("=" * 55)

    print("\nStarting Streamlit application...\n")

    try:
        subprocess.run(
            [sys.executable, "-m", "streamlit", "run", "app.py"],
            check=True
        )

    except FileNotFoundError:
        print("❌ Streamlit is not installed.")
        print("Run: pip install streamlit")

    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to start application.\n{e}")

    except KeyboardInterrupt:
        print("\nApplication closed.")

    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()