import os
from langchain_community.document_loaders import YoutubeLoader


def load_youtube_content(url):
    loader = YoutubeLoader.from_youtube_url(url, add_video_info=False, language=["en", "hi"], translation="en")
    return loader.load()


def extract_page_content(loader_output):
    return loader_output.page_content


def save_to_text_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def youtube_video_transcript(url_of_video):
    try:
        loader_output = load_youtube_content(url_of_video)
        content = extract_page_content(loader_output[0])
        return content
    except Exception as e:
        print(f"An error occurred: {e}")


