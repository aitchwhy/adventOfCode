
def solve(lineContents):
    print(f"day 11 lineContents : {lineContents}")

    # TODO: Parse input (10x10) grid where each cell is octopus energy level.
    # Each step,
    # - EACH octopus energy +1.
    # - if energy > 9, "flash" occurs (all 8 adjacent +1 energy) and
    # - "flash" loop until no more
    # - When no more "flash" -> those who "flashed" energy = 0.

    # Note: feels like setting to 0 at end is deliberate wording. But NVM for now.
    # Can set to 0 right after "flash" occurs.

    # part 1. given initial state, how many TOTAL flashes after 100 steps?
    # TODO: 2 10x10 grids.
    # - "energyStates" : One for current energy state
    # - "energyDeltas" : one for 1 iteration of energy delta to apply (result of "flash")
    #   - Use energyDeltas to update E state each loop - do while all delta != 0
