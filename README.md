# 🤖 AiAgentChatbot Crew

Welcome to the AiAgentChatbot Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up an intelligent conversational AI chatbot system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your chatbot agent to engage in natural, context-aware conversations with users.

## 🚀 Features

- **Continuous Interactive Chat**: Natural conversation flow until user decides to exit
- **Intelligent Responses**: Powered by CrewAI agents with LLM capabilities  
- **Context-Aware**: Maintains conversation context and provides relevant replies
- **Easy Exit**: Simple exit phrases like "Goodbye", "Exit", "Bye" to end conversation

## 📋 Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

### 🔑 Environment Setup

**Add your `OPENAI_API_KEY` into the `.env` file**

```bash
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

## 🛠 Customizing

- Modify `src/ai_agent_chatbot/config/agents.yaml` to define your agents
- Modify `src/ai_agent_chatbot/config/tasks.yaml` to define your tasks  
- Modify `src/ai_agent_chatbot/crew.py` to add your own logic, tools and specific args
- Modify `src/ai_agent_chatbot/main.py` to add custom inputs for your agents and tasks

## 🎯 Running the Project

To kickstart your crew of AI agents and begin the interactive chatbot session, run this from the root folder of your project:

```bash
crewai run
```

This command initializes the AiAgentChatbot Crew, starting an interactive chat session where you can converse with the AI chatbot.

### Example Conversation:
```
🤖 Chatbot is ready! Type 'Goodbye' or 'Exit' to end the chat.

You: Hello!
🤖 Chatbot: Hello! How can I assist you today?

You: What can you help me with?
🤖 Chatbot: I can answer questions, have conversations, help with ideas, and much more! What's on your mind?

You: Goodbye
🤖 Chatbot: Goodbye! Have a great day!
```

## 🏗 Understanding Your Crew

The AiAgentChatbot Crew features an intelligent conversational agent designed to:

- Engage in natural, flowing conversations
- Provide helpful and context-aware responses
- Maintain conversation continuity
- Handle various conversation topics gracefully
- Respect user's desire to end the conversation with appropriate exit phrases

The agent configuration is defined in `config/agents.yaml` and its conversational tasks are outlined in `config/tasks.yaml`.

## 🎮 Usage Tips

- The chatbot will continue conversations until you type exit phrases like: "goodbye", "exit", "quit", "bye"
- You can ask questions, seek advice, or just chat naturally
- The agent maintains context within each conversation session


