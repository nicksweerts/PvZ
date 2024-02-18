## This is a script to automate the bungee-sunflower glitch in Plants vs Zombies - I, Zombie Endless
import pyautogui, time

## The location of the bungee zombie
bungeeZombieLocation = (325, 65)

## The location of the 'resume game' button
resumeGameLocation = (395, 470)

## A function that waits two seconds, prints out the pointer position, and then returns the pointer position
def wait_and_print():
    time.sleep(2)
    x = pyautogui.position()
    print(x)
    return x

## A function that clicks on the 'resume game' button
def click_resume_game():
    pyautogui.click(resumeGameLocation)

## A function that clicks on the bungee zombie location
def click_bungee_zombie():
    pyautogui.click(bungeeZombieLocation)

## A function that performs the bungee-sunflower glitch 4 times
def bungee_sunflower_glitch(sunflowerLocation):
    i = 0
    click_resume_game()
    while i < 4:
        click_bungee_zombie()
        pyautogui.click(sunflowerLocation)
        i+=1

def main():
    sunflowerLocation = wait_and_print()
    bungee_sunflower_glitch(sunflowerLocation)

if __name__ == "__main__":
    main()