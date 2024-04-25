my_string_again = "M4x Smith, aaron rodgers, Sam Darnold-Alexander, LeBron James, Micheal Jordan, Kevin Durant, Patrick McCormick, Sean O'Malley"

import re

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]


#names = re.split(r', ', my_string_again)


for name in names:
    name_match = re.match(r"([A-Z][A-Za-z]+) ?\w* ([A-Z]'?[A-Za-z-]+)", name)
    if name_match:
        print(name_match.group())

    else:
        print('Invalid Name')

# Code incomplete if there are numeric characters the name will still print and not read as invalid
# As not  case sensitive if middle name is not title case it stillmprint does not read as invaild