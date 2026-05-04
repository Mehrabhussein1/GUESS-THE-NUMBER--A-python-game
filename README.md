# Random Number Guessing Game

A fun and interactive command-line number guessing game built with Python. Test your luck and intuition across three difficulty levels!

## Features

✨ **Multiple Difficulty Levels**
- Easy (1-10, 3 attempts)
- Medium (1-20, 5 attempts)
- Hard (1-50, 10 attempts)

🎨 **Colorful UI**
- Color-coded feedback messages
- Green for success, red for failure
- Cyan for important numbers
- Pink for score display
- Yellow for correct answer reveal

💡 **Smart Hints**
- Real-time hints guide you higher or lower
- Attempt counter shows remaining guesses
- Final score based on number of attempts needed

🔄 **Infinite Replay**
- Loop menu to play multiple rounds
- Easy exit option

## Requirements

- Python 3.6+
- No external dependencies

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd "Random number guessing game"
```

2. Run the game:
```bash
python random_num_guesser.py
```

## How to Play

1. **Select Difficulty**: Choose from Easy (1), Medium (2), Hard (3), or Exit (4)
2. **Guess the Number**: Enter your guess within the specified range
3. **Get Hints**: The game tells you if the number is higher or lower
4. **Score Calculation**: 
   - Guess on first attempt: 10 points
   - Guess on second attempt: 7-9 points (varies by difficulty)
   - Guess on third+ attempts: 3-6 points (varies by difficulty)
5. **Reveal Answer**: If you fail all attempts, the correct number is revealed
6. **Play Again**: Return to the menu to try another game

## Game Modes

### Easy Mode
- **Range**: 1-10
- **Attempts**: 3
- **Scoring**: 10 → 7 → 3 points

### Medium Mode
- **Range**: 1-20
- **Attempts**: 5
- **Scoring**: 10 → 9 → 7 → 5 → 3 points

### Hard Mode
- **Range**: 1-50
- **Attempts**: 10
- **Scoring**: 10 → 9 → 8 → 7 → 6 → 5 → 4 → 3 → 2 → 1 points

## Example Gameplay

```
Enter the difficulty you want to play on:
1. Easy (The number is between 1~10) || You get 3 attempts.
2. Medium (The number is between 1~20) || You get 5 attempts.
3. Hard (The number is between 1~50) || You get 10 attempts.
4. Exit         
Your Choice (1/2/3/4): 1

---- Selected: Easy Mode ----
    The correct number is within the range 1 to 10
    You get to take 3 attempts.
    Choose your guesses wisely !!

Attempt 1: 5
Hint: Try a bit higher

Attempt 2: 8
Congratulations! Your Guess is Correct
Your Score: 7
```

## Color Legend

| Color | Meaning |
|-------|---------|
| 🟢 Green | Correct guess |
| 🔴 Red | Wrong guess / Game over |
| 🔵 Blue | Hints |
| 🟡 Yellow | Correct number reveal |
| 🟣 Magenta | Your score |
| 🟦 Cyan | Important numbers |

## Future Enhancements

- [ ] Leaderboard system
- [ ] Difficulty progression
- [ ] Statistics tracking
- [ ] Custom number ranges
- [ ] Multiplayer mode

## License

This project is open source and available under the MIT License.

## Author

Created as a fun Python learning project.

---

**Enjoy the game and happy guessing! 🎮**
