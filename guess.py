import random
class rand:
    n = random.randrange(1, 100)
    print("guess the number = ")

    def check(self):
        while True:
            x = int(input())
            if x == self.n:
                print("u guessed it right = " + str(x))
                break
            else:
                if self.n < x:
                    print("high")
                elif self.n > x:
                    print("low")


lol = rand()
lol.check()