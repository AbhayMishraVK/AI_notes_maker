from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()


def read_file_content(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def call_llm():
    open_ai_api_key = os.getenv('GRAQ_API_KEY')
    open_ai_base = os.getenv('GRAQ_BASE_URL')
    model = "llama3-70b-8192"
    print(open_ai_api_key)
    print(open_ai_base)
    llm = ChatOpenAI(openai_api_base=open_ai_base, openai_api_key=open_ai_api_key,
                               model_name=model)
    return llm


def save_summary_to_file(summary, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(summary)


def prompt_format(prompt_filename):
    prompt_content = read_file_content(prompt_filename)
    prompt = PromptTemplate.from_template(prompt_content)
    return prompt


def main():
    try:
        transcribed_filename = "youtube_content.txt"
        prompt_filename = os.path.join("agent_prompts", "summary_prompt.txt")
        summary_filename = "summary.txt"

        transcribed_content = read_file_content(transcribed_filename)
        prompt = prompt_format(prompt_filename)
        llm = call_llm()
        summary = llm.invoke(prompt.format_prompt(transcribed_content=transcribed_content))
        save_summary_to_file(summary.content, summary_filename)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
