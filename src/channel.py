import os
from pprint import pprint

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    YT_API_KEY = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=self.YT_API_KEY)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        pprint(self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute())