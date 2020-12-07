"""
--- Day 6: Custom Customs ---
As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

abcx
abcy
abcz
In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

The first group contains one person who answered "yes" to 3 questions: a, b, and c.
The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
The last group contains one person who answered "yes" to only 1 question, b.
In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

--- Part Two ---
As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?

"""

def get_yes_answers(grp_ans):
    yes_answers = []
    for ans in grp_ans:
        if not ans in yes_answers and not ans == '\n':
            yes_answers.append(ans)
    return len(yes_answers)

def get_all_yes_ans(grp_arr):
    # if only one person answered, return all his yes's
    if len(grp_arr) == 1:
        return get_yes_answers(grp_arr[0])
    else:
        ans_list = []
        unanimous = []
        # get all the answers
        for i in range(0, len(grp_arr)):
            for ch in grp_arr[i]:
                if not ch == '\n':
                    ans_list.append(ch)
        # for all the answers, check to see if the length
        # equals the total number of people responding
        for ans in ans_list:
            if ans_list.count(ans) == len(grp_arr) and \
                not ans in unanimous:
                unanimous.append(ans)
        return len(unanimous)

if __name__ == "__main__":
    with open('day6.txt', 'r') as file:
        lines = file.readlines()
    yes_count = 0
    unanimous_count = 0
    grp_ans = ""
    grp_arr = []

    for line in lines:
        if line != '\n':
            grp_ans += line
            grp_arr.append(line)
        else:
            yes_count += get_yes_answers(grp_ans)
            unanimous_count += get_all_yes_ans(grp_arr)
            grp_arr.clear()
            grp_ans = ''
    print("# of yes ans=", yes_count)
    print('# of unanimous ans=', unanimous_count)


