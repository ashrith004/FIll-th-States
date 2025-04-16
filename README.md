India State Game 🐢
This is a Python-based interactive game to learn the states of India using the Turtle graphics library. When a player guesses the name of a state correctly, the name is displayed on the map at the appropriate location.


🧠 How It Works
The game uses a blank India map outline (india_states.gif).

Users are prompted to enter the names of Indian states.

Correct guesses appear on the map.

The game ends when:

All 31 states are guessed.

The user types Exist to quit and see the missing states.

📁 Project Structure
graphql
Copy
Edit
├── india_states.gif             # Map of India (outline with state boundaries)
├── 31_states.csv               # CSV file with state names and their coordinates
├── main.py                     # Main game logic
├── tempCodeRunnerFile.py       # Temporary debug/run file (optional)
└── README.md                   # You're here!
🗂️ CSV File Format (31_states.csv)
Make sure your CSV file is structured like this:

csv
Copy
Edit
state,x,y
Maharashtra,100,-50
Punjab,-200,100
...
state: Name of the Indian state

x, y: Coordinates where the name should be placed on the map

▶️ How to Run
Install dependencies:

bash
Copy
Edit
pip install pandas
Ensure all files (main.py, 31_states.csv, india_states.gif) are in the same directory.

Run the game:

bash
Copy
Edit
python main.py
🚨 Known Bug
In the Exist check section, there's a typo:

python
Copy
Edit
missing_states.apppend()  # should be append(state)
✅ Fix:
python
Copy
Edit
missing_states.append(state)
🧩 Future Improvements
Add more states/UTs (currently 31 listed).

Allow fuzzy matching for inputs (e.g., case-insensitive).

Add a timer or scoring system.

🏁 Exit Behavior
Click anywhere on the screen or close the window to exit.
