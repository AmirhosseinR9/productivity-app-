from typing import Dict
from src.models import  Category, Reward, Task
from src.storage import load_reward, load_tasks, save_rewards, save_tasks, load_score, save_score
from src.services import add_reward, add_task, filter_rewards, remove_task, filter_tasks, change_done, remove_reward, calculate_score

categories = {
    "exercise": Category.EXERCISE,
    "work": Category.WORK,
    "reading": Category.READING,
    "study": Category.STUDY,
    "phone": Category.PHONE,
    "game": Category.GAME
}

def show_categores(categories: Dict[str, Category]):
    for i, key in enumerate(categories.keys(), 1):
        print(f"{i}. {key}")

def menu_main():
    print("1.Task menu")
    print("2.Reward menu")
    print("3.Scorer menu")
    print("0.Exit app")


def menu_task(tasks: Dict[str,Task], categories: Dict[str, Category]):
    while True:
        print("1.Add task")
        print("2.Remove task")
        print("3.Change done")
        print("4.Show tasks")
        print("0.Exit task menu")

        try:
            choice = int(input("Enter : "))
        except ValueError:
            print("Invalid input!")
            continue


        if choice == 0:
            break

        if choice == 1:
            while True:
                show_categores(categories)
                
                category_key = input("Enter category : ").strip().lower()
                if category_key not in categories.keys():
                    print("There is no category !")
                    continue
                title = input("Enter title : ").strip().lower()
                if not title:
                    print("Title cannot be empty!")
                    continue
                try:
                    time = int(input("Enter time in minutes : "))
                    if time <= 0 or time > 1000:
                        print("Time must be between 1 and 999.")
                        continue
                except ValueError:
                    print("Invalid input!")
                    continue

                if add_task(tasks, categories, category_key, title, time):
                    save_tasks(tasks)
                    print("Operation completed.")
                    break
                else:
                    print("Invalid inputs !")
                    continue

        elif choice == 2:
            while True:
                
                title = str(input("Enter title: ")).strip().lower()
                if not title:
                    print("Title cannot be empty!")
                    continue

                if remove_task(tasks, title):
                    save_tasks(tasks)
                    print("Operation completed.")
                    break
                else:
                    print("Title not found.")
                    continue

        elif choice == 3:
            while True:
                
                title = str(input("Enter title: ")).strip().lower()
                done = str(input("Is the task done or not? true or false: ")).strip().lower()
                
                if not done:
                    print("done cannot be empty!")
                    continue
                if done == "true":
                    done = True
                elif done == "false":
                    done = False
                else:
                    print("Invalid option.")
                    continue
                if change_done(tasks, title, done):
                    save_tasks(tasks)
                    print("Operation completed.")
                    break

        elif choice == 4:
            while True:
                filter_type = str(input("Tupe filter |all|done|undone|: ")).strip().lower()
                f_tasks = filter_tasks(tasks, filter_type) # دیکشنری فیتر شده یا None بر میگردونه
                if f_tasks is None:
                    print("Filter type is invalid.")
                    continue
                show_task(f_tasks)
                break
               
        else:
            print("Invalid option!")

def menu_reward(rewards: Dict[str, Reward], categories: Dict[str, Category], total_score: int):
    while True:
        print("1.Add reward")
        print("2.Remove reward")
        print("3.Show reward")
        print("0.Exit reward menu")
        
        try:
            choice = int(input("Enter : "))
        except ValueError:
            print("Invalid input!")
            continue
        
        if choice == 0:
            break

        if choice == 1:
            while True:
                show_categores(categories)
            
                category_key = input("Enter category : ").strip().lower()
                if category_key not in categories.keys():
                    print("There is no category !")
                    continue
                activity = input("Enter activity : ").strip().lower()
                if not activity:
                    print("Title cannot be empty!")
                    continue
                minutes = int(input("Enter time in minutes : "))
                if minutes <= 0 or minutes > 1000:
                    print("Time must be between 1 and 999.")
                    continue

                if add_reward(rewards, activity, categories, category_key, minutes):
                    save_rewards(rewards)
                    print("Operation completed.")
                else:
                    print("Invalid input")
                    continue

        elif choice == 2:
             while True:
                
                activity = str(input("Enter activity: ")).strip().lower()
                if not activity:
                    print("Title cannot be empty!")
                    continue

                if remove_reward(rewards, activity):
                    save_rewards(rewards)
                    print("Operation completed.")
                    break
                else:
                    print("Activity not found.")
                    continue

        elif choice == 3:
            while True:
                filter_type = input("Tupe filter |all|canbuy|canotbuy|: ").strip().lower()
                f_rewards = filter_rewards(rewards, total_score, filter_type)
                if f_rewards is None:
                    print("Filter type is invalid.")
                    continue
                show_reward(f_rewards)
                break
        else:
            print("Invalid option!")

def menu_score(tasks: Dict[str, Task], rewards: Dict[str, Reward], total_score: int) -> int:
    while True:
        print("1.Show total score")
        print("2.Score collection")
        print("3.Gatting a reward")
        print("0.Exit score menu")

        try:
            choice = int(input("Enter : "))
        except ValueError:
            print("Invalid input")
            continue

        if choice == 0:
            break

        if choice == 1:
            print(f"Your total score: {total_score}")

        elif choice == 2:
            completed_score = calculate_score(tasks)
            total_score += completed_score
            save_tasks(tasks)
            save_score(total_score)
            print(f"Total score: {total_score} \nOperation completed")

        elif choice == 3:
            total_score = getting_reward(rewards=rewards, total_score=total_score)  # دریافت امتیاز جدید
            return total_score  #  بازگرداندن امتیاز
                
def show_task(filter_tasks: Dict[str, Task],)-> None:
    if filter_tasks:
        for i, task in enumerate(filter_tasks.values(), 1):
            print(f"\n   Task {i}.   Title: {task.title} - Category: {task.category.name.lower()}")
            print(f"             Time: {task.time} - Score: {task.score} - Done : {'done' if task.done else 'not done'}")
    else:
        print("The task is empty")




def show_reward(filter_rewards: Dict[str,Reward]) -> None:
    
    if filter_rewards:    
        for i, reward in enumerate(filter_rewards.values(),1):
            print(f"\n    Reward {i}. Activity: {reward.activity} - Category: {reward.category.name.lower()}")
            print(f"                Minutes {reward.minutes} - Reward cost {reward.reward_cost}")
    else:
        print("The reward is empty")


def getting_reward(rewards: Dict[str, Reward], total_score: int) -> int:
    
    while True:
        # ایجاد دیکشنری از فعالیت‌های قابل خرید
        affordable: Dict[str, Reward] = {}
        for activity, reward in rewards.items():
            if reward.reward_cost <= total_score:
                print(f"Activity: {reward.activity} Time: {reward.minutes} Reward cost: {reward.reward_cost}")
                affordable[activity] = reward
        
        if not affordable:
            print("You don't have enough score for any reward!")
            return total_score
    
        choice = input("Choose one of the rewards above: ").strip().lower()

        if not choice:
            print("Choice cannot be empty")
            continue
        
        if choice in affordable:
            total_score -= affordable[choice].reward_cost
            print("After a lot of effort, go enjoy it!")
            print(f"New total score: {total_score}")
            save_score(total_score)
            return total_score

        else:
            print("Invalid choice or not affordable!")



tasks: Dict[str, Task] = {}
rewards: Dict[str, Reward] = {}
total_score = 0

def main():
    tasks = load_tasks()
    rewards = load_reward()
    total_score = load_score()
    while True:
        menu_main()
        
        try:
            choice = int(input(" Enter : "))
        except ValueError:
            print(" Invalid input! \n Enter again")
            continue

        if choice == 0:
            break

        elif choice == 1:
            menu_task(tasks, categories)

        elif choice == 2:
            menu_reward(rewards, categories, total_score)
        
        elif choice == 3:
            total_score = menu_score(tasks, rewards, total_score) # دریافت امتیاز جدید 

        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()

