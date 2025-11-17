#!/usr/bin/env python
import sys
import warnings
from ai_agent_chatbot.crew import AiAgentChatbot

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

EXIT_PHRASES = ["goodbye", "bye", "exit", "quit", "see you", "stop", "end", "farewell"]

def run():
    """
    Run the chatbot crew in continuous interactive mode.
    """
    print("🤖 Intelligent Chatbot is ready! Type 'Goodbye', 'Exit', or 'Stop' to end the chat.\n")

    crew_instance = AiAgentChatbot().crew()

    while True:
        user_input = input("You: ").strip()
        if any(phrase in user_input.lower() for phrase in EXIT_PHRASES):
            print("🤖 Chatbot: Goodbye! It was great chatting with you! Have a wonderful day!")
            break

        if not user_input:
            print("🤖 Chatbot: I didn't catch that. Could you please repeat or ask me something?")
            continue

        inputs = {'user_input': user_input}

        try:
            result = crew_instance.kickoff(inputs=inputs)
            
            # Enhanced response extraction
            if hasattr(result, 'raw') and result.raw:
                response = str(result.raw).strip()
            elif hasattr(result, 'result') and result.result:
                response = str(result.result).strip()
            elif isinstance(result, str):
                response = result.strip()
            elif hasattr(result, 'output') and result.output:
                response = str(result.output).strip()
            else:
                response = "I'm here to help you with any questions or topics you'd like to discuss. What would you like to know?"
            
            # Ensure we have a meaningful response
            if not response or response == "" or len(response) < 2:
                response = "That's an interesting question! Could you tell me more about what you'd like to know?"
                
            print(f"🤖 Chatbot: {response}")
            
        except Exception as e:
            print(f"🤖 Chatbot: I apologize for the technical issue. Let's continue our conversation. What else would you like to talk about?")
            print(f"Debug: {e}")

if __name__ == "__main__":
    run()