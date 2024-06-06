import time
import base64
from io import BytesIO
import streamlit as st
import mammoth
from backend import process


def write_in_sidebar():
    with st.sidebar:
        string = """
        ## Steps to take Groq API key:

        1. **Go to this URL**: [https://console.groq.com/keys](https://console.groq.com/keys)
        2. Complete the login or register process.
        3. Create your API key.
        """
        st.markdown(string)


def write_app_knowledge():
    with st.sidebar:
        string = """
        ## Important Knowledge to Use This App:

        1. If you enter text in the text area, then YouTube video and playlist will not process.
        2. If you enter a YouTube video link, then YouTube playlist will not process.
        """
        st.markdown(string)


def create_api_key_input():
    api_key = st.sidebar.text_input("Graq API Key", type="password")
    write_in_sidebar()
    write_app_knowledge()
    return api_key


def create_playlist_input():
    playlist_link = st.text_input("YouTube Playlist Link")
    return playlist_link


def create_video_input():
    video_link = st.text_input("YouTube Video Link")
    return video_link

def create_video_range_input():
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        start_video = st.number_input("Start Video", min_value=1, step=1, help="Enter the starting video number.")
    with col2:
        end_video = st.number_input("End Video", min_value=1, step=1, help="Enter the ending video number.")
    with col3:
        process_entire_playlist = st.checkbox("Process Entire Playlist", help="Check this box to process the entire playlist.")

    if process_entire_playlist:
        video_range = "all"
    else:
        if start_video > end_video:
            st.error("Start video number cannot be greater than end video number.")
            video_range = None
        else:
            video_range = (start_video, end_video)

    return video_range


def create_text_area():
    text_area = st.text_area("Paste Topics (paste every new topic in new line)", placeholder=
    """What is computer network ? \nWhat is IP address ?\nWhat is computer science ? """)
    return text_area


def create_submit_button():
    submit_button = st.button("Submit")
    return submit_button


def check_before_passing(api_key, text_area, video_link, playlist_link):
    if api_key == '':
        st.error("API key is not available, please put it")
        return None
    if text_area != '':
        st.session_state['video_link'] = None
        st.session_state['playlist_link'] = None
        return True
    elif video_link != '':
        st.session_state['playlist_link'] = None
        return True
    if text_area == '' and video_link == '' and playlist_link == '':
        st.error("Put any of the values")
        return None


def display_docx(encoded_docx, filename='document.docx'):
    docx_bytes = base64.b64decode(encoded_docx.encode())
    docx_file = BytesIO(docx_bytes)
    result = mammoth.convert_to_html(docx_file)
    html = result.value
    docx_file.seek(0)
    html_container = st.container()
    with html_container:
        st.markdown(
            f"""
            <div style="max-width: 800px; height: 600px; overflow: scroll; margin: 0 auto; padding: 20px; background-color: #f5f5f5; border: 1px solid #ddd; border-radius: 5px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.5; }}
                    h1, h2, h3, h4, h5, h6 {{ font-weight: bold; margin-top: 1.5em; margin-bottom: 0.5em; }}
                    p {{ margin-top: 0; margin-bottom: 1em; }}
                    ul, ol {{ margin-top: 0; margin-bottom: 1em; padding-left: 2em; }}
                    pre {{ background-color: #f8f8f8; padding: 10px; border-radius: 5px; }}
                </style>
                {html}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.download_button(
            label=f"Download {filename}",
            data=docx_file.getvalue(),
            file_name=filename,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )


def backend_function(state):
    api_key = state.get("api_key")
    playlist_link = state.get("playlist_link")
    video_link = state.get("video_link")
    text_area = state.get("text_area")
    pass_to_backend = check_before_passing(api_key, text_area, video_link, playlist_link)
    if pass_to_backend is None:
        return None
    else:
        with st.spinner("Processing..."):
            encoded_docx = process()
        display_docx(encoded_docx)




def main():
    st.session_state.setdefault("submit_disabled", True)
    api_key = create_api_key_input()
    playlist_link = create_playlist_input()
    video_range = create_video_range_input()
    video_link = create_video_input()
    text_area = create_text_area()
    submit_button = create_submit_button()

    if api_key or (playlist_link or video_link or text_area):
        st.session_state["api_key"] = api_key
        st.session_state["playlist_link"] = playlist_link
        st.session_state["video_link"] = video_link
        st.session_state["text_area"] = text_area
        st.session_state["video_range"] = video_range
    if submit_button:
        st.session_state["loading"] = True
        backend_function(st.session_state)


if __name__ == "__main__":
    main()
