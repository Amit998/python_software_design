class GuessNumber:
    def __init__(self,number,min=0,max=100):
        self.number = number
        self.guesses=0
        self.min=min
        self.max=max
    
    def get_guess(self):
        guess=input(f"Please guess a Number ({self.min} - {self.max}) : ")

        if (self.valid_number(guess)):
            return int(guess)
        else:
            print("please enter a valid number")
            return self.get_guess()
    
    def valid_number(self,str_number):
        try:
            number=int(str_number)
        except :
            return False
        return self.min <= number <= self.max
    def play(self):
        while True:
            self.guesses=self.guesses+1
            guess=self.get_guess()

            if (guess < self.number):
                print("Your Guess Was Under")

            elif guess > self.number:
                print("your guess was over")
            else:
                break
        print(f"You guessed it in {self.guesses} guesses")



game=GuessNumber(56,0,100)
game.play()