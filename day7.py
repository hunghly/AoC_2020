"""
--- Day 7: Handy Haversacks ---
You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)
"""


def parse_str(str):
    main_bag = str[:str.index(' bags')]
    contained_bags = str[str.index('contain')+8:]
    bag_arr = []
    bag_details = []
    bag_details.append(main_bag)
    if ',' in contained_bags:
        bag_arr = contained_bags.split(',')
    else:
        if 'no other' in contained_bags:
            return bag_details
        bag_arr.append(contained_bags)
    # get all the bag details
    for bag in bag_arr:
        bag = bag.strip() # make sure the string has no white spaces
        # print(bag)
        # remove all unnecessary information in string
        bag = bag.replace(' bags', '')
        bag = bag.replace(' bag', '')
        bag = bag.replace('\n', '')
        bag = bag.replace('.', '')
        # print(bag)
        # add the bag details to the array
        bag_details.append(bag[:bag.index(' ')].strip())
        bag_details.append(bag[bag.index(' '):].strip())
        # print(bag_details)
    # print(str)
    # print(f"Your main bag {main_bag} contains: {bag_details}")
    return bag_details
    # print(contained_bags)
    # print(bag_arr)
    # print(bag_details)
   
def bag_contains_color(bag_details, color):
    for i in range(2, len(bag_details), 2):
        # print(i)
        # print("bag d", bag_details[i])
        if bag_details[i] == color:
            return True
    return False

# get the bag details from the master_list based on color
def get_bag_details(master_list, color):
    for bag in master_list:
        if bag[0] == color:
            return bag
    return False

def get_containing_bags(master_list, color):
    curr_bag_detail_list = []
    bag_details = get_bag_details(master_list, color)
    curr_bag_detail_list.append(bag_details)
    found_colors = []
    found_colors.append(color)
    while bag_details:
        # if only 1 color that contains nothing then add and break
        if len(bag_details) == 1:
            curr_bag_detail_list.append(bag_details[0])
            break
        for i in range(2, len(bag_details),2):
            print(bag_details[i])
            curr_bag_detail_list.append(get_bag_details(master_list, bag_details[i]))

        break
    print(curr_bag_detail_list)

# checks all bags for the bags that contain the color, whether directly or as a secondary form
def check_bags(master_list, color):
    matched_colors = []
    # check every item in the master list to see what master item contains one of the colors
    for bag in master_list:
        # if the bag already  contains the color, then increment counter
        if bag_contains_color(bag, color) and not bag[0] in matched_colors:
            matched_colors.append(bag[0])
            continue
        # also check bags within bags to see if any of them can hold your color
        for i in range(2, len(bag), 2):
            bag_details = get_bag_details(master_list, bag[i])
            if bag_contains_color(bag_details, color):
                if  not bag[0] in matched_colors:
                    matched_colors.append(bag[0])
                if not bag_details[0] in matched_colors:
                    matched_colors.append(bag_details[0])
                break
    return matched_colors

def find_all_bags(master_list, color):
    curr_color_list = check_bags(master_list, color)
    counter = 0
    new_color_list = []
    # we have the colors, now check all the bags that can contain that color
    while counter < 2:
        for bag in curr_color_list:
            new_color_list = check_bags(master_list, bag)
            for color in new_color_list:
                if not color in curr_color_list: # if the color isn't in the list, then we need to add it
                    curr_color_list.append(color)
                    counter = 0
        counter+=1
        new_color_list.clear()
    return curr_color_list


if __name__ == "__main__":
    master_list = []
    color = 'shiny gold'
    with open('day7.txt', 'r') as file:
        lines = file.readlines()
    # create master list
    for line in lines:
        master_list.append(parse_str(line))
    print(master_list)
    get_containing_bags(master_list, color)
    # all_color_bags = find_all_bags(master_list, color)
