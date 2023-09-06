from pymongo.collection import Collection

from .abstract_model import AbstractModel
from .db import db
import random


class MusicModel(AbstractModel):

    _collection: Collection = db["musics"]

    def __init__(self, json_data: dict):
        super().__init__(json_data)

    def to_dict(self):
        return {
            "_id": str(self.data["_id"]),
            "music": self.data["music"],
        }

    @classmethod
    def get_random(cls):
        data = cls.find()
        if not data:
            return random.choice(data)
