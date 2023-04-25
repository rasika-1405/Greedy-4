"""
Rasika Sasturkar
Time Complexity: O(n), n is length of the array
Space Complexity: O(1)
"""

from collections import defaultdict


def minDominoRotations(tops, bottoms) -> int:
    # using map
    # domino_map = defaultdict(int)
    # n = len(tops)
    # candidate = -1
    #
    # for i in range(n):
    #     top = tops[i]
    #     domino_map[top] += 1
    #     cntT = domino_map[top]
    #     if cntT >= n:
    #         candidate = top
    #         break
    #     bottom = bottoms[i]
    #     domino_map[bottom] += 1
    #     cntB = domino_map[bottom]
    #     if cntB >= n:
    #         candidate = bottom
    #         break
    #
    # if candidate == -1:
    #     return -1
    #
    # t_rot, b_rot = 0, 0
    # for i in range(n):
    #     if tops[i] != candidate and bottoms[i] != candidate:
    #         return -1
    #     if tops[i] != candidate:
    #         t_rot += 1
    #     if bottoms[i] != candidate:
    #         b_rot += 1
    # return min(t_rot, b_rot)

    # without using map
    n = len(tops)

    def check(candidate):
        t_rot, b_rot = 0, 0
        for i in range(n):
            if tops[i] != candidate and bottoms[i] != candidate:
                return -1
            if tops[i] != candidate:
                t_rot += 1
            if bottoms[i] != candidate:
                b_rot += 1
        return min(t_rot, b_rot)

    result = check(tops[0])
    if result != -1:
        return result
    return check(bottoms[0])


def main():
    """
    Main function - examples from LeetCode problem to show the working.
    This code ran successfully on LeetCode and passed all test cases.
    """
    print(minDominoRotations(tops=[2, 1, 2, 4, 2, 2], bottoms=[5, 2, 6, 2, 3, 2]))  # returns 2
    print(minDominoRotations(tops=[3, 5, 1, 2, 3], bottoms=[3, 6, 3, 3, 4]))  # returns -1


if __name__ == "__main__":
    main()
