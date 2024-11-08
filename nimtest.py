from inspect import getframeinfo, stack

from nim import *




def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def tests():
    """
    The test_suite function utilizes the testit() function,
    and is designed to test the take_balls and computer_take functions

    """
# take_balls tests
    unittest(take_balls([15], 4) == [11])
    unittest(take_balls([5], 2) == [3])
    unittest(take_balls([45], 1) == [44])
    unittest(take_balls([13], 4) == [9])
# computer_take tests
# unsure how to test randomness
    unittest(computer_take([14]) == [10])
    unittest(computer_take([6]) == [5])
    unittest(computer_take([27]) == [25])
    unittest(computer_take([9]) == [5])

def main():
    """
    calls tests function
    :return: none
    """
    tests()


if __name__ == '__main__':
    main()
