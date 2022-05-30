import random

#============================================================================[Global Parameters]============================================================================

# colorslist = ['1','2','3','4','5','6','7','8','9','0']  # Digits version 
colorslist = ['Red','Yellow','Blue','Green','Tourquise','Pink','Purple','White','Cyan','Black'] # Colors version 
repeated_colors = True   # If the same color can be chosen more than once
choices = 5  # Amount of colors to choose
isguesslimit = False # Whether the game ends after x amount of rounds regardless of results or played untill win
guesslimit = 50 # If Above is true, the maximum amount of guesses before round is over


def choice_generator(colors_list, choices, repeated_colors):
  random.seed()
  lchoice = []
  i = 0
  while i < choices:
      choice = random.randint(0, len(colors_list) - 1)
      if repeated_colors == True:
          lchoice.append(colors_list[choice])
          i += 1
      else:
          if colors_list[choice] in lchoice:
              continue
          else:
              lchoice.append(colors_list[choice])
              i +=1
  return lchoice


def scoring(players_choices , computers_choices):
    scoringdict = {'Bulls' : 0 , 'Cows' : 0}
    for choice in computers_choices:
        if choice not in players_choices:
            continue
        else:
            if computers_choices.index(choice) == players_choices.index(choice):
                scoringdict['Bulls'] += 1
            else:
                scoringdict['Cows'] += 1
    return scoringdict



def score(colors_list, p_choice , c_choice , prev_score = None , prev_guesses = None , guessnum = 1):

    rscore = scoring(p_choice , c_choice)
    print(f'guess: {guessnum} | choice: {p_choice} | score: {rscore} | prev guess: {prev_guesses} | prev_score: {prev_score}')

    # Initial condition
    if guessnum == 1:
        secondchoice = guess(p_choice,rscore)
        return score( secondchoice[1], secondchoice[0] , c_choice , [rscore] , [p_choice] , guessnum + 1)

    scores_list = prev_score[:]
    guesses_list = prev_guesses[:]

    # End conditions
    if rscore['Bulls'] == choices:   # All colors are bulls
        return game_summary(c_choice , guessnum , True)

    if isguesslimit == True:  # Reached guess limit
        if guesslimit == guessnum:
            return game_summary(c_choice , guessnum , False)

    # Scoring
    if prev_score[-1]['Bulls'] > rscore['Bulls']: 
        newchoice = guess(prev_guesses[-1] , prev_score[-1])
        return score( newchoice[1] , newchoice[0] , c_choice  , scores_list , guesses_list , guessnum+1) # Forward

    elif prev_score[-1]['Bulls'] == rscore['Bulls']:  
        
        if prev_score[-1]['Cows'] > rscore['Cows']:
            newchoice = guess(prev_guesses[-1] , prev_score[-1])
            return score( newchoice[1], newchoice[0] , c_choice  , scores_list , guesses_list , guessnum+1)  # Forward
            
        elif prev_score[-1]['Cows'] == rscore['Cows']:
            newchoice = guess(p_choice,rscore)
            return score( newchoice[1], newchoice[0] , c_choice  , scores_list , guesses_list , guessnum+1)  # Stay

        elif prev_score[-1]['Cows'] < rscore['Cows']:
            scores_list.append(rscore)
            guesses_list.append(p_choice)
            newchoice = guess(p_choice,rscore)
            return score(newchoice[1], newchoice[0] , c_choice , scores_list  , guesses_list , guessnum+1)  # Backwards

    elif prev_score[-1]['Bulls'] < rscore['Bulls']:
            scores_list.append(rscore)
            guesses_list.append(p_choice)
            newchoice = guess(p_choice,rscore)
            return score(newchoice[1], newchoice[0] , c_choice , scores_list  , guesses_list , guessnum+1)  # Backwards
  

def guess(player_choice,score):
    player_choice_copy = player_choice[:]  # For indexes
    newchoice = player_choice[:]  # For masking the indexes
    indexes = list(x for x in range(0,len(player_choice_copy))) # generating list of indexes in length of number of bulls and cows
    
    if score['Bulls'] > 0:
        bullsindexes = random.sample(indexes ,score['Bulls'])  
        indexes = [i for i in indexes if i not in bullsindexes]
    if score['Cows'] > 0:
        cowsindexes = random.sample(indexes ,score['Cows'])  
        indexes = [i for i in indexes if i not in cowsindexes]
        
    if len(indexes) == 0:  # When Bulls + Cows = choices
        if score['Bulls'] == choices:  # Win
            available_colors = newchoice
            return newchoice , available_colors
            
        cowscolors = [player_choice_copy[i] for i in cowsindexes]
        random.shuffle(cowscolors)
        i = 0
        for index in cowsindexes:
            newchoice[index] = cowscolors[i]
            i += 1
        available_colors  = newchoice   # When all items are either bulls or cows, we guesses all colors correctly, just need to guess the order
        
    else:
        if(score['Cows']  > 0):  
            for i in cowsindexes:  # Guessing the cows (bulls are already in their indexes so left untouched)
                newindex = random.choice(indexes)
                newchoice[newindex] = player_choice_copy[i]
                indexes.remove(newindex)
                indexes.append(i)         
        for i in indexes:   # Guessing the neither bulls or cows
            if(repeated_colors == False):
                available_colors = [color for color in colorslist if color not in newchoice]
            else:
                available_colors = colorslist
            newchoice[i] = choice_generator(available_colors , 1 , repeated_colors)[0]    # generating new choice
    return newchoice , available_colors


def game_summary(computer_choice , guessnum , is_win):
    if is_win == False:
        print(f'You Lost! The hidden code was {computer_choice}')
        return guessnum , False
    elif is_win == True:
        print(f'You Won! The hidden code was {computer_choice} and guessed after {guessnum} guesses!')
        return guessnum , True


def StartGame():
    if type(colorslist) != list or type(repeated_colors) != bool or type(choices) != int or type(isguesslimit) != bool or type(guesslimit) != int:
        print('Error: One of the game parameters is not in the correct format, make sure they are all set to their correct format:')
        print('colorlist - list /nrepeated_colors - bool/nchoices - int isguesslimit - bool/n guesslimit -  int')
        return None
    if choices > len(colorslist) and repeated_colors == False:
        print('Error: Number of choices can not be higher than length of colors list if there is no repetition!')
        return None
    if choices < 1:
        print('Error: Number of choices must be atleast 1!')
        return None
    if len(colorslist) < 1:
        print('Error: Number of choices must be atleast 1!')
        return None
    if isguesslimit == True and guesslimit < 1:
        print('Error: Number of guesses must be atleast 1 if guess limit is true!')
        return None
    return score(colorslist,  p_choice = choice_generator(colorslist, choices , repeated_colors) , c_choice = choice_generator(colorslist, choices, repeated_colors) , guessnum = 1)


resultslist = []
for i in range(0,500):
    resultslist.append(StartGame()[0])
