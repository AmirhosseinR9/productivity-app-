from typing import Dict, Optional
from src.models import Category, Reward, Task

# قسمت تسک
def add_task(
    tasks: Dict[str, Task],
    categories: Dict[str, Category],
    category_key: str, 
    title: str, 
    time: int) -> bool:
    
    # اعتبار سنجی title
    if not title or title in tasks:
        return False
    
    # اعتبار سنجی category (جلو گیری از KeyError)
    cat_opj: Optional[Category] = categories.get(category_key)
    if cat_opj is None:
        return False
    
    # ساخت تسک
    tasks[title] = Task(category=cat_opj, title=title, done=False, time=time)
    return True

def remove_task(
    tasks: Dict[str, Task], 
    title: str) -> bool:
    
    if not title in tasks:
        return False
    
    del tasks[title]
    return True


def change_done(
    tasks: Dict[str, Task], 
    title: str, 
    done=False) -> bool:

    if not title or not title in tasks:
        return False

    tasks[title].done = done
    return True


def filter_tasks(
    tasks: Dict[str, Task], 
    filter_type: str) -> Optional[Dict[str, Task]]: # تابع یا None dict برمیکرداند یا مفدار
    
    if not tasks:
        return {}

    if filter_type == "all":
        return tasks
    
    if  filter_type not in ["done", "undone"]:
        return None
    
    predicate = (lambda t: t.done) if filter_type == "done" else (lambda t: not t.done) # بر اساس filter_type  یک تابع برمیگردونه
    return {title: task for title, task in tasks.items() if predicate(task)}

# قسمت ریوارد
def add_reward(
    rewards: Dict[str, Reward],
    activity: str,
    categories: Dict[str, Category],
    category_key: str,
    minutes: int) -> bool:
    
    if not activity or activity in rewards:
        return False

    cat_opj: Optional[Category] = categories.get(category_key)
    if cat_opj is None:
        return False
    
    rewards[activity] = Reward(category=cat_opj, activity=activity, minutes=minutes)
    return True

def remove_reward(
    rewards: Dict[str, Reward],
    activity: str) -> bool:

    if not activity in rewards:
        return False

    del rewards[activity]
    return True

def filter_rewards(
    rewards: Dict[str, Reward],
    total_score: int,
    filter_type: str) -> Optional[Dict[str, Reward]]:
    
    if not rewards:
        return {}
    
    if filter_type == "all":
        return rewards

    if filter_type not in ["canbuy", "canotbuy"]:
        return None
    
    predicate = (lambda r: r.reward_cost <= total_score) if filter_type == "canbuy" else (lambda r: r.reward_cost > total_score)
    return {activity: reward for activity, reward in rewards.items() if predicate(reward)}


def calculate_score(tasks: Dict[str, Task]) -> int:
    completed_score = 0.0
    for task in tasks.values():
        if task.done:
            completed_score += task.score
            task.done = False
    return completed_score

