from dotenv import load_dotenv
import os

load_dotenv()

gemini_api = os.getenv('GEMINI_API_KEY')


def main():
    print('Hello from langchain-course !')

if __name__ == "__main__":
    main()