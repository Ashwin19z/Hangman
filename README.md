# Hangman Game

This is a simple command-line Hangman game implemented in Python.

## Files

- [`source.py`](source.py): Main Python script for the game.
- [`words.txt`](words.txt): List of words used in the game.

## How to Play

1. Run the game using Python:
    ```sh
    python source.py
    ```
2. The game will randomly select a word from [`words.txt`](words.txt).
3. You have 6 lives to guess the word, one letter at a time.
4. Enter your guesses when prompted. Correct guesses reveal letters; incorrect guesses reduce your lives.
5. The game ends when you guess the word or run out of lives.

## Requirements

- Python 3.x

## Customization

- To add more words, edit [`words.txt`](words.txt) and add one word per line.

## License

This project is for educational purposes.
