from dataclasses import dataclass, field
from enum import Enum, auto


class Category(Enum):
    EXERCISE = auto() # ورزش کردن
    WORK = auto() # کار های روزانه 
    READING = auto() # خواندن/مطالعه
    STUDY = auto() # یادگیی 
    PHONE = auto() # استفاده از گوشی
    GAME = auto() # بازی

BASE_SCORE = {
    # امتیاز زیاد_ کار های سخت
    Category.EXERCISE: 1,
    Category.READING: 1,
    Category.WORK: 1.2,
    Category.STUDY: 1.5,
    # امتیاز کم_ کار های اسان
    Category.GAME: 0.3,
    Category.PHONE: 0.4
}

BASE_REWARD_COST = {
    # مقدار کسر امتیاز کم_کار های مفید
    Category.EXERCISE: 0.6,
    Category.READING: 0.4,
    Category.WORK: 0.5,
    # امتیاز زیاد_پاداش و سرگرمی
    Category.GAME: 1.2,
    Category.PHONE: 1

}

@dataclass
class Task:
    category: Category
    title: str
    done: bool
    time: int
    score: float = field(init = False) # امتیاز که یدست می اورد
    
    def __post_init__(self):
        self.score = BASE_SCORE[self.category] * self.time

    def to_dict(self):
        return {
            "category": self.category.name,
            "title": self.title,
            "done": self.done,
            "time": self.time,
            "score": self.score
        }
    @classmethod
    def from_dict(cls, data):
        category_enum = Category[data["category"]]
        opj = cls(
            category_enum,
            data["title"],
            data["done"],
            data["time"]
            )
        opj.score = data["score"]
        return opj

@dataclass
class Reward:
    category: Category
    activity: str
    minutes: int
    reward_cost: float = field(init = False) # امتیازی که باید پرداخت شود

    def __post_init__(self):
        self.reward_cost = BASE_REWARD_COST[self.category] * self.minutes

    def to_dict(self):
        return {
            "category": self.category.name,
            "activity": self.activity,
            "minutes": self.minutes,
            "reward_cost": self.reward_cost
        }
    @classmethod
    def from_dict(cls, data):
        category_enum = Category[data["category"]]
        opj = cls(
            category_enum,
            data["activity"],
            data["minutes"],
            )
        opj.reward_cost = data["reward_cost"]
        return opj