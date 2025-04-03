# The Higher Lower Game

## Project Overview

This project is an interactive game developed in **Python** using **Pygame**, based on the "Higher Lower" concept. The goal is to compare the populations of two countries and guess whether the second one has a higher or lower population than the first.

## Key Features

- User-friendly graphical interface built with **Pygame**
- Country and population data loaded from an **Excel** file
- Score tracking system that saves the highest score
- Visually appealing elements, including country flags and themed backgrounds
- Interactive buttons for user input

## Project Structure

The project includes the following files and folders:

- `main.py` – Main source code for the game  
- `lista_tarilor.xlsx` – Excel file containing country names and populations  
- `images/` – Folder containing images used in the game:  
  - `lower_higher.png` – Main background image  
  - `poza_fundal.png` – Secondary interface background  
  - `gameover.png` – Image displayed at the end of the game  
  - `tari/` – Folder containing country flags  

## Usage Instructions

### 1. Install Dependencies

Make sure **Python 3.x** is installed, then install the required modules:

```bash
pip install pygame pandas openpyxl
```

### 2. **Run the Game**
To start the game, run the following command in your terminal:
```sh
python main.py
```

### 3. **How to Play**

- Click the PLAY button to begin.
- You will see two countries with flags and the population of the first country.
- Choose whether the second country has a higher or lower population.
- If your guess is correct, you earn a point and the game continues.
- If your guess is incorrect, the game ends and your score is displayed.

## Screenshots

1. **Main Menu**
  ![Image](https://github.com/user-attachments/assets/89862f8e-4088-4ebe-b701-685a3cc3b32a)

2. **Game in Progress**
   ![Image](https://github.com/user-attachments/assets/421e9384-03d9-4d6a-9ba1-09e93ce4c8d6)

3. **Game Over Screen**
  ![Image](https://github.com/user-attachments/assets/98ecd94e-cead-4cbb-a439-81c0e27893de)

## Technical Requirements

- **IDE:** PyCharm (recommended)
- **Libraries Used**
  - `pygame` - for graphical interface
  - `pandas` - for handling the Excel filel
  - `random` - for selecting random countries

## Authors
- **Names:** Catalin Voicu & Victor Enache
- **Emails:** catavoicu01@gmail.com & enachevictor887@gmail.com
- Project developed as part of the course: Computer Programming and Programming Languages 3 – Python Project.
- **University:** Faculty of Electronics, Telecommunications and Information Technology, Polytechnic University of Bucharest.

