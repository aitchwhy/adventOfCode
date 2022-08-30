

class Fish():
    newFishAge = 6

    def __init__(self, age):
        self.age = age

    # decrement or reset own age + return new fish count (0 or 1).
    def spendDay(self):
        # Decrement age by 1.
        # if 0, reset to 6 + spawn new
        if (self.age == 0):
            self.age = Fish.newFishAge
            return 1
        else:
            self.age -= 1
            return 0

    def __repr__(self):
        return f"{self.age}"


def solve(lineContents):

    # Parse input.
    fishes = [Fish(int(x)) for x in lineContents[0].split(",")]
    print(fishes)

    # days = 18
    # days = 80
    days = 256

    for day in range(days):
        print(f"Day {day}")
        # Spend a day.
        newFishCount = 0
        for fish in fishes:
            newFishCount += fish.spendDay()
        fishes.extend([Fish(8) for _ in range(newFishCount)])
        # print(fishes, newFishCount)
        # print(fishes)

    print(len(fishes))
