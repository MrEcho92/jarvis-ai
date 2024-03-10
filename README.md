# Typing assistant powered by AI 

Jarvis AI for notes is a project inspired by patrickloeber (https://github.com/patrickloeber/ai-typing-assistant/blob/main/README.md) which is a typing assistant powered by AI with Ollama. 

## Purpose of the script
As a user, I can type on Notepad and a copy of the typed sentence will fix any typos. 

This project uses Ollama (large language model), python packages and IDE. 

## Get Started

### 1. Install dependencies & setup local environment
- Set up locally, create virtual env `python -m venv .venv` and activate the env
- Install required python packages `pip install -r requirements.txt`
- Set up Ollama locally following instructions on https://github.com/ollama/ollama and run `ollama run mistral:7b-instruct-v0.2-q4_K_S`
- Run the script `python main.py`
- **Note** If you are on Mac, you need to add your IDE/ Terminal both on accessibility and input monitoring 