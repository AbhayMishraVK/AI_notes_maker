import time
import base64
from io import BytesIO
import streamlit as st
import mammoth
from backend import process


def create_api_key_input():
    api_key = st.sidebar.text_input("GraQ API Key", type="password")
    return api_key


def create_playlist_input():
    playlist_link = st.text_input("YouTube Playlist Link")
    return playlist_link


def create_video_input():
    video_link = st.text_input("YouTube Video Link")
    return video_link


def create_text_area():
    text_area = st.text_area("Paste Topics (paste every new topic in new line)", placeholder=
    """What is computer network ? \nWhat is IP address ?\nWhat is computer science ? """)
    return text_area


def create_submit_button():
    submit_button = st.button("Submit")
    return submit_button


def display_loading_indicator():
    if st.session_state.get("loading", False):
        with st.spinner("Loading..."):
            pass


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
    # Decode the base64 encoded document
    docx_bytes = base64.b64decode(encoded_docx.encode())
    # Create a BytesIO object
    docx_file = BytesIO(docx_bytes)

    # Convert the document to HTML
    result = mammoth.convert_to_html(docx_file)
    html = result.value

    # Reset the BytesIO object cursor to the start
    docx_file.seek(0)

    # Create a container in Streamlit for displaying the HTML
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
        encoded_docx = process()
        display_docx(encoded_docx)


def main():
    st.session_state.setdefault("submit_disabled", True)
    api_key = create_api_key_input()
    playlist_link = create_playlist_input()
    video_link = create_video_input()
    text_area = create_text_area()
    submit_button = create_submit_button()
    display_loading_indicator()

    if api_key or (playlist_link or video_link or text_area):
        st.session_state["api_key"] = api_key
        st.session_state["playlist_link"] = playlist_link
        st.session_state["video_link"] = video_link
        st.session_state["text_area"] = text_area
    if submit_button:
        st.session_state["loading"] = True
        backend_function(st.session_state)


if __name__ == "__main__":
    main()
