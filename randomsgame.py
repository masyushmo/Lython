import random
from coloring import colors


def restart():
    (print(colors.fg.cyan,"Do you want to try again?", colors.reset))
    while True:
        print("Please enter " + colors.fg.green,'Yes', colors.reset + " or " + colors.fg.red, 'No', colors.reset)
        str = input()
        if str == 'Yes':
            return True
        elif str == 'No':
            return False
        else:
            print(colors.fg.red,"Bad input, please enter 'Yes' or 'No'", colors.reset)
            continue
        
        
def hotcold(a, b, r):
    if r - a < r - b:
        print(colors.bg.orange, "Hotter",colors.reset)
    if r - a > r - b:
        print(colors.bg.blue, "Colder",colors.reset)


def game(mini, maxi):
    attempts, lastegg = [], 0
    rnum = random.randint(mini, maxi)
    print("I've guessed the number between " + str(mini) + " and " + str(maxi - 1) + " try to guess it")
    for t in range(10, 0, -1):
        print(colors.fg.lightgrey, "you have " + str(t) + " tries left", colors.reset)
        while True:
            try:
                egg = int(input())
                break
            except:
                print(colors.fg.red,"Bad input, please enter int between " + str(mini) + " and " + str(maxi - 1), colors.reset)
                continue
        attempts.append(egg) # collect attempts
        lastegg = attempts[len(attempts) - 2] # save last number for hotter colder comparison
        if egg == rnum:
            print(colors.fg.green,"You're right! Number I guessed is " + str(rnum), colors.reset)
            break
        elif mini > egg or egg> maxi:
            print("Congrats, you lost one attempt because ur number is out of scope", colors.fg.red,"^0^",colors.reset)
        elif egg < rnum:
            hotcold(egg, lastegg, rnum)
        elif egg > rnum:
            hotcold(lastegg, egg, rnum)
    if egg != rnum:
        print(colors.fg.red, 'Game over! No attempts left.\n Correct number was ' + str(rnum), colors.reset)

        
def main():
    print(colors.fg.orange,"Hello, today we'll play my first game wrinten in Python\n", colors.reset)
    while True:
        game(10, 30) #range input minimun and maximum
        if restart() == False:
            exit()
    
main()
