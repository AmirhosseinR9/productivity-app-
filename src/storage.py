from .models import Task
from .models import Reward
import os
import json 

DATA_TASK = "datas/tasks.json"
DATA_REWARD = "datas/rewards.json"
DATA_SCORE = "datas/total_score.txt"

def load_tasks():

    if not os.path.exists(DATA_TASK):
        return {}

    data = {}
    with open(DATA_TASK, "r", encoding="utf-8") as f:
        data = json.load(f)

    tasks = {title: Task.from_dict(value) for title, value in data.items()}
    
    return tasks

def save_tasks(tasks):
    
    data = {title: value.to_dict() for title, value in tasks.items()}

    with open(DATA_TASK, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_reward():

    if not os.path.exists(DATA_REWARD):
        return {}

    data = {}
    with open(DATA_REWARD, "r", encoding="utf-8") as f:
        data = json.load(f)

    rewards = {activity: Reward.from_dict(value) for activity, value in data.items()}
    
    return rewards

def save_rewards(rewards):
    
    data = {title: value.to_dict() for title, value in rewards.items()}

    with open(DATA_REWARD, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_score():
     
    if not os.path.exists(DATA_SCORE):
        return 0.0
    
    score = 0
    with open(DATA_SCORE, "r") as f:
        score = f.read().strip()
        if score:
            return float(score)
        else:
            return 0.0

def save_score(score: float):

    with open(DATA_SCORE, "w") as f:
        f.write(str(score))