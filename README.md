Python Tic Tac Toe ❌⭕
A robust, console-based Tic Tac Toe game implemented in Python featuring dynamic emoji rendering, smart move validation, and a solo-play AI mode.

Features 🎮
Emoji Interface: Uses modern icons (1️⃣-9️⃣, 🅾️, 🗙) for a clear and engaging visual experience.

Multiplayer & Singleplayer: Play against a friend locally or challenge the computer.

Robust Input Handling: Advanced validation prevents overwriting occupied squares or crashing on invalid entries.

Dynamic Turn Logic: Seamlessly alternates between players with instant win or draw detection.

"Center-First" AI: The computer follows a tactical strategy by prioritizing the center of the board.

Cross-Platform: Automatically clears the screen on Windows (cls) and Unix/Linux/macOS (clear).

Game Rules 📋
Objective: Align three of your symbols (🅾️ or 🗙) horizontally, vertically, or diagonally.

The Board:

Consists of 9 squares numbered 1 through 9.

Player 1 always uses the 🅾️ symbol.

Player 2 (or the Computer) uses the 🗙 symbol.

Gameplay:

Players enter the number corresponding to their desired square.

Once a square is occupied, it cannot be reused.

The game ends immediately when a player achieves "Three-in-a-Row" or when all squares are filled (Draw).

Project Structure 📁
Tic-Tac-Toe-game/
├── main.py                # Main game logic and entry point
├── README.md              # Project documentation (this file)
└── Tic_Tac_Toe_image.png
Main Functions Overview:
clear_screen() - Clears the console to keep the interface tidy.

display_board() - Renders the 3x3 grid with current symbols.

get_player_names() - Handles initialization and mode selection (Solo/Duo).

get_valid_board_move() - Manages user input and updates available options.

get_valid_board_move_computer() - Decision logic for the AI.

game_logic() - Analyzes the board for winning combinations.

main() - The core loop managing turns and replayability.

Requirements ✅
Python 3.x

No external dependencies (uses standard random, time, os modules).

Installation & Setup 🚀
Clone the repository:
Bash
git clone https://github.com/FrontN/Tic-Tac-Toe-game.git
cd Tic-Tac-Toe-game
How to Play 🎯
Run the game:

Bash
python main.py
Enter your name and choose whether to play with a friend (y) or the computer (n).

You will see the grid with numbers 1️⃣-9️⃣.

On your turn, type the number of the square where you want to place your symbol.

The board updates instantly to show the move.

After the match, type y for a rematch or n to quit.

Game Output Example 📺
+------+------+------+
|      |      |      |
|  1️⃣ |  🅾️  |  3️⃣ |
|      |      |      |
+------+------+------+
|      |      |      |
|  4️⃣  |  🗙  |  6️⃣ |
|      |      |      |
+------+------+------+
|      |      |      |
|  🗙  |  8️⃣ |  9️⃣  |
|      |      |      |
+------+------+------+

Enter your move 🅾️ Mario: 1
Technical Highlights 💡
Modularity: Dedicated functions for input, output, and logic make the code easy to read and modify.

Emoji Compatibility: Smart string handling to ensure emojis align perfectly within the terminal grid.

Memory Management: Uses a SQUARES_TO_POP list to track legal remaining moves.

Replay Loop: Allows for multiple sessions without manually restarting the script.

Future Enhancements 🎯
Scoreboard System: Track wins/losses per session (Player 1 vs Player 2).

Unbeatable AI: Implementation of the Minimax algorithm for a perfect computer opponent.

Customization: Allow users to choose their own starting emojis.

Match History: Option to review the sequence of moves after the game.

Contributing 🤝
Feel free to fork this repository and submit pull requests for any improvements!

Author 👨‍💻
FrontN - Developed as a learning project for Python game logic and terminal-based UI.

Enjoy the game! ❌⭕
