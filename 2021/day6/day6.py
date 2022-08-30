
from collections import Counter


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


class FishSchool():

    fishMaxAge = 8

    def __init__(self, initAges):
        self.fishCountByAge = Counter(initAges)

    def __repr__(self):
        return f"{self.fishCountByAge}"

    def spendDay(self):
        resetFishCount = self.fishCountByAge[0]
        self.fishCountByAge[0] = 0
        for age in range(1, FishSchool.fishMaxAge+1):
            self.fishCountByAge[age-1] += self.fishCountByAge[age]
            self.fishCountByAge[age] = 0
        self.fishCountByAge[6] += resetFishCount
        self.fishCountByAge[8] += resetFishCount

    def getFishCount(self):
        return sum(self.fishCountByAge.values())


def solve(lineContents):

    # Parse input.
    school = FishSchool([(int(x)) for x in lineContents[0].split(",")])
    fishes = [Fish(int(x)) for x in lineContents[0].split(",")]
    print(fishes)

    # days = 18
    # days = 80
    days = 256

    for day in range(days):
        print(f"Day {day}")
        # part 1 (naive)
        # # Spend a day.
        # newFishCount = 0
        # for fish in fishes:
        #     newFishCount += fish.spendDay()
        # fishes.extend([Fish(8) for _ in range(newFishCount)])
        # # print(fishes, newFishCount)
        # # print(fishes)

        # part 2 - keep counter (each day shift by 1 for each timer + add new)
        school.spendDay()
        # print(school, school.getFishCount())
        print(school.getFishCount())

    # print(len(fishes))
