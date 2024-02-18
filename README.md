# Bungee-Sunflower Glitch Automation

This directory contains a Python script for automating the Bungee-Sunflower glitch in Plants vs Zombies: Gane of the Year Edition, as well as a requirements.txt file specifying the dependencies needed to run the script.

**Note:** I tested with different timings to see how bungees I could attach at a single time and found the max to be 4 with this method. Since each bungee zombie costs 125 sun and the sunflower drops 200 sun, this means that there is a profit of 75 sun per bungee zombie. Thus, by using this glitch you will be gaining an extra 100 (75 \* 4 - 200) sun more than what is expected per sunflower.

## Script Overview

The Python script, named `bungee_sunflower_glitch.py`, is designed to automate the Bungee-Sunflower glitch in a game. The glitch involves interacting with specific in-game elements using the `pyautogui` library. The script is structured as follows:

- **Bungee Zombie and Resume Game Locations:**

  - The locations of the Bungee Zombie and the 'Resume Game' button are specified as coordinates.
  - You may use some of the functions in the python script to find the locations of these for your individual instance.
  - The ones that are already in the code are assuming that you are running the game in windowed mode and have the window against the top left corner of your screen.

- **Functions:**

  - `wait_and_print()`: Waits for two seconds, prints the current pointer position, and returns the pointer position.
  - `click_resume_game()`: Clicks on the 'Resume Game' button.
  - `click_bungee_zombie()`: Clicks on the Bungee Zombie location.
  - `bungee_sunflower_glitch(sunflowerLocation)`: Performs the Bungee-Sunflower glitch by clicking on the 'Resume Game' button, clicking the Bungee Zombie, and then clicking on a specified sunflower location. This process is repeated four times.
  - `main()`: Calls the `wait_and_print()` function to obtain the sunflower location and then initiates the Bungee-Sunflower glitch.

- **Script Execution:**
  - The script is set up to execute when run directly (`__name__ == "__main__"`), calling the `main()` function.

## Requirements

To run the script, make sure you have the required dependencies installed. You can install them using the following command:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains the necessary Python package `pyautogui`.

## Usage

1. Install the required dependencies as mentioned above.
2. Run the script using the following command:

```bash
python bungee_sunflower_glitch.py
```

Feel free to modify the script or contribute to its development. Happy gaming!
