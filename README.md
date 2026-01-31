# Productivity & Reward Management System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)

A command-line productivity application that helps you manage tasks, track progress, and reward yourself for accomplishments using a gamified point system.

## ✨ Features

### 📝 Task Management
- Create tasks with categories (Exercise, Work, Reading, Study, Phone, Game)
- Track task completion status
- Automatic score calculation based on category difficulty and time
- Filter tasks by status (all/done/undone)
- Persistent storage using JSON

### 🏆 Reward System
- Create custom rewards for activities
- Set reward costs based on category and duration
- Filter rewards by affordability (canbuy/cannotbuy)
- Purchase rewards using earned points

### ⚡ Smart Scoring
- Automatic point calculation:
  - Hard tasks (Study): 1.5 points per minute
  - Medium tasks (Work): 1.2 points per minute  
  - Easy tasks (Game): 0.3 points per minute
- Score persistence across sessions
- Reward cost calculation based on activity type

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher

### Installation
1. Clone or download the project
2. No external dependencies required!

### Running the Application
```bash
python main.py
```

## 📁 Project Structure

```
productivity_app/
├── src/
│   ├── models.py        # Data models (Task, Reward, Category)
│   ├── storage.py       # File I/O operations
│   ├── services.py      # Business logic
│   ├── stats.py         # Statistics and reporting
│   └── __init__.py
├── datas/               # Data storage directory
│   ├── tasks.json       # Tasks database
│   ├── rewards.json     # Rewards database
│   └── total_score.txt  # Current score
├── main.py              # Main application entry point
├── README.md            # This file

```

## 🎮 Usage Guide

### Main Menu
```
1. Task menu      - Manage your tasks
2. Reward menu    - Create and view rewards  
3. Scorer menu    - Track points and redeem rewards
0. Exit app
```

### Adding a Task
1. Select "Task menu" → "Add task"
2. Choose a category from the list
3. Enter task title and duration in minutes
4. Tasks automatically calculate points based on:
   - Category difficulty
   - Time spent

### Earning Points
1. Mark tasks as completed (change status to "done")
2. Go to "Scorer menu" → "Score collection"
3. Points from completed tasks are added to your total
4. Completed tasks reset to "undone" for reuse

### Creating Rewards
1. Select "Reward menu" → "Add reward"
2. Choose a category (different costs apply)
3. Enter activity name and duration
4. Reward cost is calculated automatically

### Redeeming Rewards
1. Check available rewards in "Reward menu" → "Show reward"
2. Filter by "canbuy" to see affordable rewards
3. Go to "Scorer menu" → "Getting a reward"
4. Select and enjoy your earned reward!

## 📈 Scoring System

### Task Points (Earned)
| Category | Points/Minute | Description |
|----------|--------------|-------------|
| STUDY    | 1.5          | Learning activities |
| WORK     | 1.2          | Daily chores/work |
| EXERCISE | 1.0          | Physical activity |
| READING  | 1.0          | Reading/studying |
| PHONE    | 0.4          | Phone usage |
| GAME     | 0.3          | Gaming |

### Reward Costs (Spent)
| Category | Cost/Minute | Description |
|----------|-------------|-------------|
| GAME     | 1.2         | Entertainment |
| PHONE    | 1.0         | Leisure |
| WORK     | 0.5         | Productive |
| EXERCISE | 0.6         | Health |
| READING  | 0.4         | Educational |

## 🔧 Advanced Features

### Task Filtering
- View all tasks
- View only completed tasks
- View only pending tasks

### Reward Filtering  
- View all rewards
- View affordable rewards (can buy)
- View expensive rewards (cannot buy yet)

### Data Persistence
- All data automatically saves to JSON files
- No risk of data loss between sessions
- Human-readable data format

## 📊 Statistics Module

The statistics module provides insights into:
- Overall completion rate
- Points earned by category
- Reward redemption history
- Productivity trends
- Goal progress tracking

## 🛠️ Development

### Adding New Categories
Edit `BASE_SCORE` and `BASE_REWARD_COST` in `models.py`:
```python
BASE_SCORE = {
    Category.NEW_CATEGORY: 1.0,  # Points per minute
}

BASE_REWARD_COST = {
    Category.NEW_CATEGORY: 1.0,  # Cost per minute
}
```

### Extending Functionality
The modular design makes it easy to add:
- New task types
- Different scoring algorithms  
- Additional filters
- Export functionality
- GUI interface

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🐛 Troubleshooting

### Common Issues
1. **"ModuleNotFoundError: No module named 'src'"**
   - Ensure you're running from the project root directory
   - Check that `src/__init__.py` exists

2. **JSON decode errors**
   - Delete corrupted files in `datas/` folder
   - They will be recreated automatically

3. **Permission errors**
   - Ensure write permissions in project directory
   - Create `datas/` folder manually if needed

### Data Backup
Regularly backup the `datas/` folder to prevent data loss.

## 🌟 Future Enhancements

Planned features:
- [ ] Web interface
- [ ] Mobile app
- [ ] Cloud sync
- [ ] Advanced analytics dashboard
- [ ] Social sharing
- [ ] Custom category support
- [ ] Recurring tasks
- [ ] Reminder notifications

## 📞 Support

For issues, questions, or suggestions:
1. Check the troubleshooting section
2. Review the code comments
3. Create a GitHub issue

---

**Happy Productivity!** 🚀 Track your progress, earn rewards, and build better habits with this intuitive productivity system.
