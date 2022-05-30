# Bulls-Cows-Game

This is a generator of the famous Bulls Cows game. 
From Wikipedia:

" The numerical version of the game is usually played with 4 digits, but can be played with any number of digits.

On a sheet of paper, the players each write a 4-digit secret number. The digits must be all different. Then, in turn, the players try to guess their opponent's number who gives the number of matches. The digits of the number guessed also must all be different. If the matching digits are in their right positions, they are "bulls", if in different positions, they are "cows". Example:

Secret number: 4271
Opponent's try: 1234
Answer: 1 bull and 2 cows. (The bull is "2", the cows are "4" and "1".)
The first player to reveal the other's secret number wins the game. "

To read more about the rules of the game: https://en.wikipedia.org/wiki/Bulls_and_Cows

--------------------------------------------------------------------------------------------------------------

## Code explanation:

This game has several parameters that can be modifies:

**colorslist** - Has 2 options: Colors or Digits. The list of items the computer/player creates its codes from (can easily be modified if you choose to add/remove items).

**repeated_colors** - True/False. If the same color/digits can be chosen more than once. **DO NOT SET TO TRUE AS SCORING THERE IS CURRENTLY BUGGED!**

**choices** - Integer. How many items the code will be made of. Must be smaller or equal to colorslisr otherwise will throw an error.

**isguesslimit** = True/False. If the game is played with a limit of guesses by the player or continuous until the player finds the code.

**guesslimit** = Integer. If isguesslimit is set to True, how many guesses can the player make before the game is over.


The game is played between the computer and a player (which is also the computer). The algorithm was built in a recursive way. It generates an initial random code, creates lists of previous codes and scores and then checks if the number of bulls/cows has increased. If yes, appends the guess and score to the previous guesses and scores list respectively and progresses by generating a new code based on the new score. If not, dismisses the code, regresses to the previous best guess and generates a new code based on it. 
The following diagram summarizes the options:


**Important Note!**: The algorithm was kept semi-dummy on purpose for the sake of randomness and noise , as the code was mainly written for datasets creating for Machine Learning modeling.


Like said before, the code is excellent for various statistical analysis, data analysis, data visualization, machine learning modeling etc. It is modular so you can
write on top of it a code that saves whatever data you want and need to analyse.

An example dataset I created using this code: https://www.kaggle.com/datasets/nurielreuven/bullscows-game-results

--------------------------------------------------------------------------------------------------------------

## Open issues:

-Scoring is bugged when repeated_colors is True. This is because the scoring is done with the .index attribute, which finds the index of the FIRST occurence in the list.

--------------------------------------------------------------------------------------------------------------

For any further questions feel free to contact me here or by email: nuriel8833@gmail.com
Created by Nuriel Reuven , Uploaded on 25/05/2022 , All Rights Reserved.
