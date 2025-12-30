from datetime import datetime

class Movie:
    def __init__(self, id=None, title=None, language=None, url=None, image_url=None, release_date=None):
        self.id = id
        self.title = title
        self.language = language  # marathi, hindi, punjabi
        self.url = url
        self.image_url = image_url
        self.release_date = release_date or datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'language': self.language,
            'url': self.url,
            'image_url': self.image_url,
            'release_date': self.release_date.isoformat() if isinstance(self.release_date, datetime) else self.release_date
        }
