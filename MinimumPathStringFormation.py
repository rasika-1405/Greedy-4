"""
Rasika Sasturkar
Time Complexity: Brute force = O(s*t), Optimal = O(s+tlogk)
Space Complexity: Brute force = O(1), Optimal = O(s)
where,
s is length of source string, t is length of target string,
k is avg. length of index lists in the map.
"""

from bisect import bisect_left
from collections import defaultdict


def shortestWay(source: str, target: str) -> int:
    sl = len(source)
    tl = len(target)
    count = 1
    sp, tp = 0, 0

    # brute force
    # char_set = set()
    # for char in source:
    #     char_set.add(char)
    #
    # while tp < tl:
    #     s_char = source[sp]
    #     t_char = target[tp]
    #     if t_char not in char_set:
    #         return -1
    #     if s_char == t_char:
    #         sp += 1
    #         tp += 1
    #         if tp == tl:
    #             return count
    #     else:
    #         sp += 1
    #     if sp == sl:
    #         count += 1
    #         sp = 0

    # Optimal solution
    char_map = defaultdict(list)
    for i in range(sl):
        char = source[i]
        char_map[char].append(i)

    while tp < tl:
        t_char = target[tp]
        if t_char not in char_map:
            return -1
        t_list = char_map[t_char]
        k = bisect_left(t_list, sp)
        if k < 0:
            k = -k - 1
        if k == len(t_list):
            count += 1
            sp = t_list[0]
        else:
            # target found in the list
            sp = t_list[k]
        sp += 1
        tp += 1

    return count


def main():
    """
    Main function - examples from LeetCode problem to show the working.
    This code ran successfully on LeetCode and passed all test cases.
    """
    print(shortestWay(source="abc", target="abcbc"))  # return 2
    print(shortestWay(source="abc", target="acdbc"))  # return -1
    print(shortestWay(source="xyz", target="xzyxz"))  # return 3


if __name__ == "__main__":
    main()
