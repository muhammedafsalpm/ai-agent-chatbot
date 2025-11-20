import logging
from ai_agent_chatbot.crew import ChatbotCrew

# Logging setup
logging.basicConfig(
    filename="chatbot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run():
    chatbot = ChatbotCrew().crew()
    print("🤖 Hello! I’m your AI Chatbot. Type 'exit', 'stop', or 'goodbye' to end the chat.\n")

    while True:
        user_input = input("You: ").strip()
        logging.info(f"User: {user_input}")

        if user_input.lower() in ["exit", "stop", "goodbye"]:
            print("🤖 Chatbot: Goodbye! Have a great day! 👋")
            logging.info("Chat ended by user.")
            break

        try:
            # The key change — pass query (not topic)
            response = chatbot.kickoff(inputs={"query": user_input})
            print(f"🤖 Chatbot: {response}")
            logging.info(f"Chatbot: {response}\n")

        except Exception as e:
            print("⚠️ Something went wrong. Check logs for details.")
            logging.error(f"Error: {e}")

if __name__ == "__main__":
    run()
