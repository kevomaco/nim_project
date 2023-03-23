# NIM
Inspired by: https://programmingbydoing.com/a/nim.html
## Your Task
Nim (https://en.wikipedia.org/wiki/Nim) is a classic game for two players.  In this project, you will simulate a set of pre-recorded moves from a file, determining if the moves are valid, and if they are, a winner.
### Rules of Nim
1. First decide how many counters (small objects of some kind) and how many piles are to be used.
2. Divide the counters among the piles.  Each pile can have any number of counters.
3. Each player then alternates by selecting any number of counters (up to the total amount) from one pile.
4. The game finishes when one player is forced to take the last token from a pile. This player loses.
### Input and output
In this assignment, you will be given a file that describes a game of NIM, and asked to simulate this game.  Part of this task will be determining if the file represents a valid game of NIM.
Your input will be a file in the format described below, and your output will be either a simulation of the game, or a notice that the file does not represent a valid game.
#### File Format
Example file:

    12;3
    3;3;6
    0;3
    2;5
    1;3
- The first line contains two numbers, separated by a semicolon: the number of counters, followed by the number of piles.
- The second line gives the starting state, with all the counters separated into the given piles. 
  - The result is a list of numbers, one for each pile, separated by semicolons.
- Following that are the moves in the game, starting with Player 1 and alternating.
- Each move is a pair of numbers separated by semicolons: which pile the player is taking from, followed by how many are taken.
  - Note that pile numbers are 0-indexed, with the left-most pile being indicated by 0, and the rightmost by `num_of_piles`-1
  - The move where the final player would take the last token is **not** represented in the file.
#### Result
Your program will scan the file and either print the phrase `Invalid Game.`, or a simulation of the game.  If the game is invalid, **only** print `Invalid Game.`, and nothing else.
#### Example Simulation
Here is an example simulation for the game above:

    Starting State:
    3  3  6
    Player 1 takes 3 tokens from the pile 1.
    State:
    0  3  6
    Player 2 takes 5 tokens from the pile 3.
    State:
    0  3  1
    Player 1 takes 3 tokens from the pile 2.
    State:
    0  0  1
    Player 2 loses.
Notes:
- The text of your code will be directly compared with our sample output, **make sure your formatting matches ours exactly**
- There are exactly two spaces between each pile number in the state.
- The output text for a move must be exactly `Player i takes n tokes from the pile k.` (note the period)
  - `i` is the current player, either 1 or 2.  Player 1 always goes first.
  - `n` is how many tokens are taken.
  - `k` is the pile the tokens are taken from. 
    - **Very important note: The input file uses 0-indexed pile numbers, but you should output 1-indexed numbers here.**
    - So, if the file says `0;3`, you need to output that the player took tokens from pile `1`, not pile `0`.
- The last line should read either `Player 1 loses.` or `Player 2 loses.` and should be output when only one token remains in all the piles.
### Valid Game
A game is valid if:
- The initial state is valid:
  - The first line of the file contains exactly two numbers separated by a semicolon: the number of counters and the number of piles.  Both of these number must be greater than zero.
  - The second line contains exactly as many numbers separated by semicolons as the number of piles.
  - The total of all the numbers in the second line exactly equals the number of counters.
  - All the numbers on the second line are greater than or equal to zero.
- All the moves are valid.
  - Each move contains two numbers separated by a semicolon: the pile to be removed from, and how many tokens are removed.
  - The pile number is between 0 and one less than the number of piles.
  - The given pile must have at least as many tokens as the move wants to remove.
  - The result of the move cannot cause all piles to become empty.
- At the end of the last move, there is exactly one token in all the piles combined.

Any game matching all of these criteria is valid, any other game is invalid.

## Testing
A few example games are included, but you are responsible for adding test cases of your own.
## Hints
### simulate_game
The central challenge of this assignment is designing the structure of `simulate_game` yourself.  The other functions are important building blocks, but you need to determine how to use them.

Work through the structure of `simulate_game` before starting to write it. Or, to put it another way: "Think before you hack."

Remember that you should output `Invalid Game.` **and nothing else** if the game is invalid.  This is even if the last move in the game is the invalid one.  Make sure you don't start printing output before determining if the game is valid.


### Misc
- Make sure that your formatting is correct!
- `str.spltlines()` returns an array containing each line of the input string.

- Python's f-strings are your friend here.  f-strings are a simple way to format strings that contain variables.
### f-string example
    name = "Eric"
    age = 74
    print(f"Hello, {name}. You are {age}.")
    Hello, Eric. You are 74.
## Further Reading
Rules of Nim: https://en.wikipedia.org/wiki/Nim
## Credits
Inspired by: https://programmingbydoing.com/a/nim.html