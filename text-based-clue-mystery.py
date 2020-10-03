import random
import time

#------ Starting message ------#
print("loading Clue: Text-Based Adventure ...")
time.sleep(4)
print("*murder mystery music plays*")
time.sleep(1)
print("The year is 1964. Dr. Black was murdered in his own home last night while some house guests were present.")
print("\tThere are no signs of a break-in. The only possible suspects are those who spent the night:")
time.sleep(6)
print("\tMiss [S]carlet, Mrs. [W]hite, Mrs. [Pe]acock, Professor [Pl]um, Mr. [G]reen, and Colonel [M]ustard")
time.sleep(2)

#------ Randomly set location, weapon, and killer in case file ------#
num_k = random.randint(1, 6)
num_w = random.randint(1, 5)
num_r = random.randint(1, 9)
switcher_k={
    1:'Miss Scarlet',
    2:'Mrs Peacock',
    3:'Mrs White',
    4:'Prof Plum',
    5:'Col Mustard',
    6:'Mr Green'
}
killer = switcher_k.get(num_k,"error")

switcher_w={
    1:'Rope',
    2:'Wrench',
    3:'Candlestick',
    4:'Lead Pipe',
    5:'Knife'
}
weapon = switcher_w.get(num_w,"error")

switcher_r={
    1:'Hall',
    2:'Lounge',
    3:'Dining Room',
    4:'Kitchen',
    5:'Ballroom',
    6:'Conservatory',
    7:'Billiard Room',
    8:'Library',
    9:'Study'
}
room = switcher_r.get(num_r)
print(killer)
print(weapon)
print(room)

#------ Function for entering a room ------#
def enter_room(x): # x is number associated with room to enter
    x_name = switcher_r.get(x, "... ERROR")
    print("\nWelcome to the ", x_name)

    on = 1
    while on == 1:
        guess_room(x)

        print("\nThis turn is now over. Here are your options:")
        switcher2={
            1:'-[S]tay, [L]eave-',
            2:'-[S]tay, [L]eave, Secret [T]unnel to conservatory-',
            3:'-[S]tay, [L]eave-',
            4:'-[S]tay, [L]eave, Secret [T]unnel to study-',
            5:'-[S]tay, [L]eave-',
            6:'-[S]tay, [L]eave, Secret [T]unnel to lounge-',
            7:'-[S]tay, [L]eave-',
            8:'-[S]tay, [L]eave-',
            9:'-[S]tay, [L]eave, Secret [T]unnel to kitchen-'
        }
        x_name = switcher2.get(x)
        print(x_name)
        next = input()

        if next == 'L':
            on = 0
            out = [1, x]
            return out
        elif next == 'T':
            on = 0
            switcher3={
            9:[0, 4],
            2:[0, 6],
            4:[0, 9],
            6:[0, 2],
            }
            out = switcher3.get(x)
            return out
        else:
            pass

#------ Function for interrogating when you're in a room ------#
def guess_room(x): # x is number associated with player's current room
    room_g = switcher_r.get(x)
    weapon_g = input("-guess weapon-\n")
    killer_g = input("-guess killer-\n")
    count = 0
    a = 0
    b = 0
    d = 0
    c = ["","",""]

    if room_g == room: # Room guess is correct
        count += 1
        c[0] = room
        a = 1
    if weapon_g == weapon: # Weapon guess is correct
        count += 1
        c[1] = weapon
        b = 1
    if killer_g == killer: # Killer guess is correct
        count += 1
        c[2] = killer
        d = 1

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

#------ Function for leaving a room ------#
def moving(x): # x is number associated with player's current room
    on = 1
    print("You are now in the hallway. Would you like to travel to the next [cl]ockwise or [co]unter-clockwise room?")

    while on == 1:
        walk = input()

        if walk == "cl":
            if x == 9:
                nextrm = 1
            else:
                nextrm = x + 1
        elif walk == "co":
            if x == 1:
                nextrm = 9
            else:
                nextrm = x - 1
        else:
            print("Invalid input. You will travel clockwise by default.")
            nextrm = x + 1

        z = switcher_r.get(nextrm, "... ERROR")
        print("\nYou are now at the", z, "Do you want to [e]nter, or keep [w]alking down the hall?")
        decision = input()

        if decision == "e":
            on = 0
            return nextrm
        elif decision == "w":
            print("Would you like to travel to the next [cl]ockwise or [co]unter-clockwise room?")
            x = nextrm
        else:
            print("Invalid input. You will enter by default.")
            on = 0

#------ Function for ending the game ------#
def guess_final():
    room_f = input("-identify the scene of the crime-\n")
    weapon_f = input("-identify the murder weapon-\n")
    killer_f = input("-identify the killer-\n")

    print("...")
    time.sleep(1)
    print("You exclaim: It was in the " +room_f+ ", with the " +weapon_f+ ", and " +killer_f+ " did it!")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("You read over the case files")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("It was in the " +room+ ", with the " +weapon+ ", and " +killer+ " did it!")
    time.sleep(2)

    if room_f == room and weapon_f == weapon and killer_f == killer:
        print("Congratulations, you cracked the case!")
        time.sleep(1)
        print("*murder mystery music plays over a montage of the night of the murder")
        time.sleep(3)
        print(killer+ " was tried and convicted for the brutal murder of Dr. Black.")
        time.sleep(3)
        print(killer+ " confessed that (s)he was a patient of the victim. Dr. Black had been blackmailing " +killer+ " with sensitive health records.")
        time.sleep(3)
    elif killer_f != killer:
        print(killer_f+ " was tried and wrongfully convicted for the brutal murder of Dr. Black.")
        time.sleep(3)
        print(killer_f+ " spent 2 years in prison before the necessary evidence surfaced to prove his/her innocence.")
        time.sleep(4)
        print("However, prosecutors lacked proper evidence to convict the true killer.")
        time.sleep(3)
        print(killer+ " got away with the murder and is now living out a life of luxury in the Bahamas with their inheritance.")
        print("It turns out " +killer+ " was Dr. Black's cousin, and his next of kin.")
        time.sleep(5)
    else:
        print(killer+ " was tried for the brutal murder of Dr. Black, but the evidence didn't hold up in court.")
        time.sleep(4)
        print(killer+ " got away with the murder and is now living out a life of luxury in the Bahamas with their inheritance.")
        print("It turns out " +killer+ " was Dr. Black's cousin, and his next of kin.")
        time.sleep(5)

    print("...")
    time.sleep(1)
    print("Thanks for playing!")

#------ Playing the game ------#
def main():
    player = input("-choose your character-\n")
    switcher1={
        "S":1,
        "W":4,
        "Pe":6,
        "Pl":9,
        "G":5,
        "M":3
    }
    location = switcher1.get(player,"invalid input. an internal error has occurred. you must reset the game")

    loc_name = switcher_r.get(location)
    print("You just left the ", loc_name)

    on = 1
    temp = moving(location)
    temp2 = enter_room(temp)
    tunnel_flag = temp2[0]
    location = temp2[1]

    while on == 1:

        if tunnel_flag == 0: # Secret tunnel to new room
            temp = enter_room(location)
            tunnel_flag = temp[0]
            location = temp[1]
        else: # Moving in the hall
            temp = moving(location)
            temp2 = enter_room(temp)
            tunnel_flag = temp2[0]
            location = temp2[1]

        print("Are you ready to open the case files?")
        stuff = input("-[Y]es or [N]o-\n")

        if stuff == "Y":
            on = 0
            guess_final()
        else:
            pass

main()
