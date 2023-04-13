import re


def embed_url(video_url):
        regex = r"(?:https:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?(.+)"
        return re.sub(regex, r"https://www.youtube.com/embed/\1",video_url)