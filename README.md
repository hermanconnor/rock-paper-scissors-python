# 🎮 Rock, Paper, Scissors - Python Terminal Edition 🐍

A colorful terminal-based Rock, Paper, Scissors game built with Python. It includes ASCII art animations!


## ✨ Features

- **Animated ASCII Art** - Watch rock, paper, and scissors come to life with ASCII animations
- **Color-Coded Interface** - Intuitive color scheme using Colorama for cross-platform terminal colors
- **Countdown Animation** - Exciting "Rock... Paper... Scissors... SHOOT!" countdown before each reveal
- **Side-by-Side Display** - See your choice and the computer's choice displayed together

### 🎮 User-Friendly Design
- **Flexible Input** - Accept full names (`rock`) or abbreviations (`r`)
- **Case Insensitive** - Type however you want: `ROCK`, `Rock`, or `rock`
- **Input Validation** - Helpful error messages guide you to valid inputs
- **Easy Exit** - Type `quit`, `exit`, or `q` anytime to leave gracefully

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Setup

1. **Clone or download this repository**
```bash
git clone https://github.com/hermanconnor/rock-paper-scissors-python.git
cd rock-paper-scissors-python
```

2. **Install required dependencies**
```bash
pip install colorama
```

That's it! You're ready to play.

## 🎲 How to Play

### Starting the Game

Run the game from your terminal:
```bash
python game.py
```

### Making Your Choice

Each round, enter your choice:
- Type the full name: `rock`, `paper`, or `scissors`
- Or use shortcuts: `r`, `p`, or `s`
- Case doesn't matter: `ROCK`, `Rock`, and `rock` all work!

### Watch the Magic

After you choose, enjoy the countdown animation followed by the ASCII art reveal showing both choices side-by-side!

### Understanding the Results

The game will show:
- 🟢 **Green** for your wins
- 🔴 **Red** for computer wins
- 🟡 **Yellow** for ties

## 📖 Game Rules

Classic Rock, Paper, Scissors rules apply:
- 🪨 **Rock** crushes **Scissors**
- 📄 **Paper** covers **Rock**
- ✂️ **Scissors** cuts **Paper**

## 🎨 Color Scheme

The game uses an intuitive color system:
- 🔵 **Blue** - Your choices and information
- 🟣 **Magenta** - Computer's choices
- 🟢 **Green** - Wins and positive messages
- 🔴 **Red** - Losses and errors
- 🟡 **Yellow** - Ties and prompts
- 🔵 **Cyan** - Headers and informational text

## 🏗️ Project Structure

```
rock-paper-scissors/
├── game.py           # Main game file with all logic
├── README.md         # This file
└── requirements.txt  # Python dependencies
```

## 💻 Technical Details

### Built With
- **Python 3** - Core programming language
- **Colorama** - Cross-platform colored terminal text
- **Standard Library** - `random`, `time`, `sys` modules

### Key Programming Concepts Demonstrated
- Data-driven design using dictionaries
- Input validation and error handling
- Terminal animation techniques
- String formatting and manipulation
- Cross-platform compatibility


## 📝 License

[MIT License](LICENSE).

