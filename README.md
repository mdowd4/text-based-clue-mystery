# text-based-clue-mystery

<p align="center">
<img src="/images/clueboard.jpg" height=500>
</p>

## Description
This is a single-player, text-based version of the boardgame Clue.

## Directions
When you are prompted to enter a command, certain words will have brackets around one or more of the letters. Enter the letter(s) of the option you want to pick. For example, to [w]alk you would type "w" and hit enter. When guessing the killer, weapon, and room, you will have to type the whole name. You must enter it exactly as shown below (case sensitive) otherwise the program will say that your guess was not correct and it will not warn you that you made an invalid entry.

Suspected killers: Miss Scarlet, Mrs Peacock, Mrs White, Prof Plum, Col Mustard, Mr Green

Suspected weapons: Rope, Wrench, Candlestick, Lead Pipe, Knife

Suspected rooms: Hall, Lounge, Dining Room, Kitchen, Ballroom, Conservatory, Billiard Room, Library, Study

When moving around the hallway, reference an image of the Clue board to know where the rooms are in relation to each other. You will have the option to move to the next room in the clockwise or counterclockwise direction.  

If you want to cheat, uncomment lines 50-52 to print the answers at the beginning of the game. You will get different endings based on how much of the case you solved correctly.

## Challenges
The most challenging part of this project was telling the player what they guessed correctly, if any, when visiting a room. There are 8 combinations of correct and incorrect killer, weapon, and room so I knew there would be a lot of if-statements involved, but I wanted it to be coded as cleanly and efficiently as I could. This is the first part of the solution to this challenge:
```python
if room_g == room: # Room guess is correct
  count += 1
  c[0] = room
  a = 1
```
This code is repeated for killer and weapon, each time incrementing the index of the array. This will count how many of the three were correct, as well as record the string in an array for printing later. Next is what to print depending on how many were correct:
```python
if count == 0:
  print("None are true")
elif count == 1: # Only one thing is correct
  print("you correctly guessed ", end ="")
  print(c[0], end ="")
  print(c[1], end ="")
  print(c[2], end ="")
elif count == 2: # Two things are correct
  if a == b: # Both room & weapon are correct
    i = random.randint(0, 1)
    print("you correctly guessed", c[i])
  elif b == d: # Both weapon & killer are correct
    i = random.randint(1, 2)
    print("you correctly guessed", c[i])
  else: # Both room & killer are correct
    i = random.randint(0, 100)
    if i < 50:
      print("you correctly guessed", c[0])
    else:
      print("you correctly guessed", c[3])
else: # All three things are correct
  i = random.randint(0, 2)
  print("you correctly guessed", c[i])
```
For all and none correct, it was pretty straightforward. For two correct, the code first determines which of the two categories it was. Then I wanted a random selection of which one to print to make the game more fair. If only one is correct, I kept it simple and printed the whole array (including the empty cells) which ends up looking a little weird. Based on the way it prints I can tell that only one guess was correct, but a player who doesn't know the code wouldn't be able to deduce that so I left it like that. In the future I could find a better way to write it.

## History
This was my first Python project. I wrote it in April 2020 when I was learning the basics of Python over spring break. I fixed some bugs and reorganized the code before uploading it to GitHub in the initial commit. 

## Future Additions
- [ ] An error message for when the user has typed an invalid guess
- [ ] Improve some of the printing
- [ ] Fix printing for one correct guess while in a room (see challenges)
