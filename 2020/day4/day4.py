# Day 2, 2020

def solve(input_lines):

    print(f"######### Day 4")

    import re
    from collections import namedtuple

    Passport = namedtuple("Passport", [
        "byr", # birthyear
        "iyr", # issueyear
        "eyr", # expirationyear
        "hgt", # height
        "hcl", # hair color
        "ecl", # eye color
        "pid", # passport ID
        "cid"  # country ID
    ])

    ignorableFields = [
        "cid"
    ]

    def isEmptyLine(line):
        return line == ""

    def parsePassport(passportLines):
        fields = []
        for l in passportLines:
            tokens = l.split(" ")
            fields.extend(tokens)

        passport = dict()
        for f in fields:
            key, val = f.split(":")
            passport[key] = val
        # print(passport)
        return passport

    passports = []
    acc = []
    for l in input_lines:
        if (isEmptyLine(l)):
            passports.append(parsePassport(acc))
            acc.clear()
            continue

        acc.append(l)
    # off by one
    if (acc):
        passports.append(parsePassport(acc))

    def isValidPartOne(passport):
        if (passport.get("byr") is None): return False
        if (passport.get("iyr") is None): return False
        if (passport.get("eyr") is None): return False
        if (passport.get("hgt") is None): return False
        if (passport.get("hcl") is None): return False
        if (passport.get("ecl") is None): return False
        if (passport.get("pid") is None): return False
        return True
        #if (passport.get("cid") is None): return False
    
    def parseInt(s):
        if (s is None):
            return None
        try:
            return int(s)
        except ValueError:
            # not int
            return None

    def parseHeight(s, suffix):
        if (s is None) or (suffix is None):
            return None
        if (suffix not in s): return None
        m = re.search(f"(\d+){suffix}", s)
        # print(m)
        if (m is None) or (m.group(0) is None) or (len(m.group(0)) != len(s)):
            return None
        return (m.group(1), suffix)

    def parseHairColor(s):
        if (s is None):
            return None
        m = re.search("#[0-9a-f]{6}", s)
        # print(m)
        if (m is None) or (m.group(0) is None) or (len(m.group(0)) != len(s)):
            return None
        return m.group(0)

    def parseEyeColor(s):
        if (s is None):
            return None
        m = re.search("amb|blu|brn|gry|grn|hzl|oth", s)
        # print(m)
        if (m is None) or (m.group(0) is None) or (len(m.group(0)) != len(s)):
            return None
        return m.group(0)

    def parsePid(s):
        if (s is None):
            return None
        m = re.search("\d{9}", s)
        # print(m)
        if (m is None) or (m.group(0) is None) or (len(m.group(0)) != len(s)):
            return None
        return m.group(0)


    def isValidPartTwo(passport):
        print("#############")
        print(f"passport : {passport}")
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        byr = parseInt(passport.get("byr"))
        if (byr is None): return False
        if not (1920 <= parseInt(byr) <= 2002): return False
        print("PASS byr")
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        iyr = parseInt(passport.get("iyr"))
        if (iyr is None): return False
        if not (2010 <= int(iyr) <= 2020): return False
        print("PASS iyr")
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        eyr = parseInt(passport.get("eyr"))
        if (eyr is None): return False
        if not (2020 <= int(eyr) <= 2030): return False
        print("PASS eyr")
        # hgt (Height) - a number followed by either cm or in:
            # If cm, the number must be at least 150 and at most 193.
            # If in, the number must be at least 59 and at most 76.
        hgtStr = passport.get("hgt")
        if (hgtStr is None) or (("cm" not in hgtStr) and ("in" not in hgtStr)): return False
        suffix = "cm" if ("cm" in hgtStr) else "in"
        hgt = parseHeight(hgtStr, suffix)
        if (hgt is None): return False
        if (hgt[1] == "cm") and not (150 <= int(hgt[0]) <= 193):
            return False
        if (hgt[1] == "in") and not (59 <= int(hgt[0]) <= 76):
            return False
        print("PASS hgt")
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        hcl = parseHairColor(passport.get("hcl"))
        if (hcl is None): return False
        print("PASS hcl")
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        ecl = parseEyeColor(passport.get("ecl"))
        if (ecl is None): return False
        print("PASS ecl")

        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        pid = parsePid(passport.get("pid"))
        if (pid is None): return False
        print("PASS pid")

        # cid (Country ID) - ignored, missing or not.

        return True


    # print(passports[0])
    # print(isValid(passports[0]))
    # print(passports[1])
    # print(isValid(passports[1]))

    print(len([x for x in passports if isValidPartOne(x)]))
    print(len([x for x in passports if isValidPartTwo(x)]))

    validPartTwo = [x for x in passports if isValidPartTwo(x)]


    for x in validPartTwo:
        print("#########")
        for k in sorted(x.keys()):
            if (k == "pid"):
                print(f" {k} : {x.get(k)} ")


    print(len([x for x in passports if isValidPartTwo(x)]))
    
    # byr (Birth Year)
    # iyr (Issue Year)
    # eyr (Expiration Year)
    # hgt (Height)
    # hcl (Hair Color)
    # ecl (Eye Color)
    # pid (Passport ID)
    # cid (Country ID) --- ignore

    # count valid passports (must have all fields except cid)
