#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        # Mines are set as a set of random unique positions
        self.mines = set(random.sample(range(width * height), mines))
        # Initialize board and revealed status arrays
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            return False  # Hit a mine, game over
        self.revealed[y][x] = True
        # If no adjacent mines, recursively reveal neighboring cells
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                # Input validation for coordinates
                x = int(input("Enter x coordinate (0-{}): ".format(self.width - 1)))
                y = int(input("Enter y coordinate (0-{}): ".format(self.height - 1)))
                
                # Check if the input is within bounds
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Invalid input. Coordinates out of bounds.")
                    continue

                # Attempt to reveal the chosen cell
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

            except ValueError:
                print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()

