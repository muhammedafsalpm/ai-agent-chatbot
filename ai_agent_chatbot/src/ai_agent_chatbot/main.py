#!/usr/bin/env python
import sys
import warnings
from ai_agent_chatbot.crew import AiAgentChatbot

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

EXIT_PHRASES = ["goodbye", "bye", "exit", "quit", "see you"]

def run():
    """
    Run the chatbot crew in continuous interactive mode.
    """
    print("🤖 Chatbot is ready! Type 'Goodbye' or 'Exit' to end the chat.\n")

    crew_instance = AiAgentChatbot().crew()

    while True:
        user_input = input("You: ").strip()
        if any(user_input.lower() == phrase for phrase in EXIT_PHRASES):
            print("🤖 Chatbot: Goodbye! Have a great day!")
            break

        inputs = {'user_input': user_input}

        try:
            result = crew_instance.kickoff(inputs=inputs)
            # Assuming CrewAI returns the final output in "result" dictionary
            if isinstance(result, dict):
                print(f"🤖 Chatbot: {result.get('final_output', '...')}")
            else:
                print(f"🤖 Chatbot: {result}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    run()
