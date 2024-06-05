import streamlit as st
from graph import final_graph
from graph_for_videos import final_graph_for_videos
from youtube_functions import get_playlist_video_urls
import os
import base64


def get_docx_path():
    cwd = os.getcwd()
    docx_path = os.path.join(cwd, "final_output.docx")
    return docx_path


def read_docx(docx_path):
    with open(docx_path, "rb") as docx_file:
        docx_bytes = docx_file.read()
    return docx_bytes


def encode_docx(docx_bytes):
    encoded_docx = base64.b64encode(docx_bytes).decode()
    return encoded_docx


def delete_file_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


def process():
    file_path = r"final_output.docx"
    delete_file_if_exists(file_path)

    if st.session_state.get("playlist_link") is not None:
        playlist_link = st.session_state.get("playlist_link")
        playlist_video_url = get_playlist_video_urls(playlist_link)
        final_result = final_graph_for_videos.invoke({'list_of_url': playlist_video_url}, {"recursion_limit": 1000})
    elif st.session_state.get("video_link") is not None:
        video_url = [st.session_state.get("video_link")]
        final_result = final_graph_for_videos.invoke({'list_of_url': video_url}, {"recursion_limit": 1000})
    elif st.session_state.get("text_area") != '':
        unstructured_question = st.session_state.get("text_area")
        print(unstructured_question)
        final_result = final_graph.invoke({'user_question': unstructured_question}, {"recursion_limit": 1000})

    docx_path = get_docx_path()
    docx_bytes = read_docx(docx_path)
    encoded_docx = encode_docx(docx_bytes)
    return encoded_docx
