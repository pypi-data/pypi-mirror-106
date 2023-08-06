import secrets
class Guess_Number:
    """Guess the number game. Call object with no parameters to start. 

    """  
    def __init__(self):
        while True:
            lower_cache = input("(If you want to quit type 'Quit')\nEnter Lower Bound: ")
            if lower_cache == "Quit" :
                print("\nQuitting Game")
                return
            if lower_cache.isnumeric():
                lower_bound = int(lower_cache)
                break
            else:
                print("\nLower Bound needs to be positive numeric")
                continue
        while True:
            upper_cache = input("(If you want to quit type 'Quit')\nEnter Upper Bound: ")
            if upper_cache == "Quit" :
                print("\nQuitting Game")
                return
            elif upper_cache.isnumeric():
                if int(upper_cache) == 0:
                    print("\nUpper Bound cannot be 0")       
                    continue    
                if lower_bound >= int(upper_cache):
                    print("\nUpper Bound cannot be equal or lower than Lower Bound")       
                    continue
                upper_bound = int(upper_cache)
                break
            else:
                print("\nUpper Bound needs to be positive numeric")
                continue        
        random = secrets.SystemRandom().randint(lower_bound, upper_bound)
        print("\nGenerated A Random Number")
        while True:
            guess_cache = input("\n(If you want to quit type 'Quit')\nInitialize Number of guesses: ")
            if guess_cache == "Quit" :
                print("\nQuitting Game")
                return
            elif guess_cache.isnumeric():
                if int(guess_cache) == 0:
                    print("\nNumber of guesses needs to be positive numeric")       
                    continue
                guess = int(guess_cache)
                break
            else:
                print("\nNumber of guesses needs to be positive numeric")
                continue        
        predicts = []
        print ("\nGuessed Numbers") 
        print("None")
        for i in range(guess):  
            print (*predicts)
            print ("\nRemaining Guesses %d" %(guess-i))
            while True:
                predict_cache = input("\n(If you want to quit type 'Quit')\nGuess the number: \n")
                if predict_cache == "Quit" :
                    print("\nQuitting Game")
                    return
                elif predict_cache.isnumeric():
                    if int(predict_cache) == 0:
                        print("\nGuess needs to be positive numeric")
                        print ("\nGuessed Numbers")
                        continue
                    if int(predict_cache) in predicts:
                        print("\nYou have already guessed this number")
                        print ("\nGuessed Numbers")
                        continue
                    predict = int(predict_cache)
                    if predict == random:
                        print("\nCongratulations you did it in ",
                              i+1, " Try")
                        print("\nQuitting Game")
                        return                        
                    elif random > predict:
                        print("\nYou Guessed Too Small!")
                        predicts.append(predict)
                        print ("\nGuessed Numbers")
                        break
                    elif random < predict:
                        print("\nYou Guessed Too High!")
                        predicts.append(predict)
                        print ("\nGuessed Numbers")
                        break
                else:
                    print("\nGuess needs to be positive numeric")
                    print ("\nGuessed Numbers")
                    continue                    
        print (*predicts)
        print("\nThe number was %d" % random)
        print("\tBetter Luck Next time!")
        return
        
    
    