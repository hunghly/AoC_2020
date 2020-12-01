"""
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
"""


def find_2020(arr):
    found = -1
    for item in arr:
        remainder = 2020 - item
        try:
            found = arr.index(remainder)
            if found != -1:
                print("Match found ", item, arr[found])
                break
        except:
            print("Did not compute.")
    return found

def find_2020_three_entries(arr):
    found = -1
    for item in arr:
        remainder = 2020 - item
        pair = add_to_equal(arr, remainder)
        if (add_to_equal(arr, remainder)):
            print("Match found for 2020 using [{},{},{}]".format(item, pair[0],pair[1]))
            break
        try:
            found = arr.index(remainder)
            if found != -1:
                print("Match found ", item, arr[found])
                break
        except:
            print("Did not compute.")
    return found

def add_to_equal(arr, val):
    found_item = -1
    for item in arr:
        diff = val - item
        try:
            found_item = arr.index(diff)
            if found_item != -1:
                # print("Found two matches [{},{}]to equal {}".format(item, arr[found_item], val))
                return (item, arr[found_item])
                break
        except:
            pass
    return False

test_input = [1456, 979, 366, 299, 675, 1721]
input = [
    1313, 1968, 1334, 1566, 820, 1435, 1369, 1230, 1383, 1816, 1396, 1974,
    1911, 1989, 1824, 1430, 1709, 1204, 1792, 1800, 1703, 2009, 1467, 1400,
    1315, 1985, 1598, 1215, 1574, 1770, 1870, 1352, 1544, 1339, 188, 1347,
    1986, 2003, 1538, 1839, 1688, 1350, 1191, 1961, 1578, 1946, 1548, 1975,
    1745, 1631, 1390, 1811, 1586, 1409, 247, 1600, 1565, 1929, 1854, 1602,
    1773, 1815, 1887, 1689, 1266, 1573, 1534, 1939, 1909, 1273, 1386, 1713,
    1268, 1611, 1348, 1478, 1857, 1916, 1113, 936, 1603, 1716, 1875, 1855,
    1834, 1701, 1279, 1346, 1503, 1797, 1287, 1447, 1475, 1950, 1614, 1261,
    1442, 1299, 1465, 896, 1481, 1804, 1931, 1849, 1675, 1726, 355, 1485, 1343,
    1697, 1735, 1858, 1205, 1345, 1281, 253, 1808, 1557, 1964, 1771, 1891,
    1583, 1896, 1398, 1930, 1258, 1338, 1208, 1328, 1493, 1963, 1374, 1212,
    1223, 1501, 2004, 1591, 1954, 115, 1972, 1814, 1643, 1270, 1349, 1297,
    1399, 1969, 1237, 1228, 1379, 1779, 1765, 1427, 1464, 1247, 1967, 1577,
    1719, 1559, 1274, 1879, 1504, 1732, 1277, 1758, 1721, 1936, 1605, 1358,
    1505, 1411, 1823, 1576, 1682, 1439, 1901, 1940, 1760, 1414, 1193, 1900,
    1990, 1781, 1801, 1239, 1729, 1360, 1780, 1848, 1468, 1484, 1280, 1278,
    1851, 1903, 1894, 1731, 1451, 549, 1570
]
find_2020_three_entries(input)
# print(add_to_equal(input, 2020))