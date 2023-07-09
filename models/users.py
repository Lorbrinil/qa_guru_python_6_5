import dataclasses
import datetime
from enum import Enum


class Hobby(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_number: str
    date_of_birth: datetime.date
    subjects: str
    hobbies: Hobby
    image: str
    current_address: str
    state: str
    city: str
