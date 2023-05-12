import os

class MongoDB:
    def __init__(self) -> None:
        self.uri = os.getenv('MONGO_URI')