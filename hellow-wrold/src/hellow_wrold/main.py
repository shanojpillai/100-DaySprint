from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env file

def main():
    # Access the environment variable
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    if openai_api_key:
        print("OpenAI API Key loaded successfully.")
    else:
        print("Failed to load OpenAI API Key.")

if __name__ == "__main__":
    main()
    