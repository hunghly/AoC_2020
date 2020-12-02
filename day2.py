"""
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
"""

def validate_policy(policy):
    lower = int(policy[0][0])
    upper = int(policy[0][1])
    ch = policy[1]
    pw = policy[2]
    ch_count = pw.count(ch)
    if ch_count in range(lower, upper+1): #inclusive range
        return True
    return False

def parse_policy(str):
    half = str.split(':')
    limits = half[0].split(' ')[0].split('-') # get lower/upper bounds
    char = half[0].split(' ')[1] # get character for policy
    password = half[1].strip() # get password
    return [limits, char, password]

if __name__ == '__main__':
    policy = parse_policy('1-3 a: abcde')
    valid_count = 0
    with open('day2.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        policy = parse_policy(line)
        if validate_policy(policy):
            valid_count+=1
    print("valid_count is: ", valid_count)