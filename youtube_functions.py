import youtube_dl


def get_playlist_video_urls(playlist_url):
    """
    Given a YouTube playlist URL, returns a list of video URLs ID in the playlist.
    """
    try:
        ydl_opts = {
            'quiet': True,
            'extract_flat': True,
            'force_generic_extractor': True,
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(playlist_url, download=False)

        video_urls = [entry['url'] for entry in info_dict['entries']]
        video_urls = get_complete_video_urls(video_urls)
        return video_urls

    except Exception as e:
        print(f"Error fetching playlist: {e}")
        return []


def get_complete_video_urls(video_ids):
    """
    Given a list of YouTube video IDs, constructs and returns complete video URLs.
    """
    base_url = "https://www.youtube.com/watch?v="
    complete_urls = [base_url + video_id for video_id in video_ids]
    return complete_urls


