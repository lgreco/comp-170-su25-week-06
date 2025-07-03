### Intersection of two strings
def intersection(foo: str, bar: str) -> str | None:
    intersection_string = None
    # Make sure that input strints are not null
    if foo and bar:
        # Check trivial case two strings are identical. 
        # THERE IS A BUG IN HERE. DISCUSS IT! FIX IT.
        if foo == bar:
            intersection_string = foo
        else:
            # Initialize an empty intersection string
            intersection_string = ""
            # Begin traversing the outer string one character at a time
            for f in foo:
                f_in_intersection = f in intersection_string
                if not f_in_intersection:
                    # Set up traversal of inner string one char at a time
                    b_index = 0
                    # This loop can end without going through the whole bar string: as
                    # soon as the f char is found in the bar string, we are done with this
                    # traversal and we can move to the next f char.
                    while b_index < len(bar) and not f_in_intersection:
                        b = bar[b_index]
                        if b not in intersection_string:
                            if bar[b_index] == f:
                                # Found an intersecting character. Add it to the result
                                # string, and show that character f is now in the intersection
                                # (to stop the loop)
                                intersection_string += f
                                f_in_intersection = True
                        # Prepare to advance to the next character in the bar string
                        b_index += 1
    return intersection_string
    # end method intersection


###  Alphabetical assessment
def is_alphabetical(string: str) -> bool:
    alpha_only = True
    # Verify that input string not null
    if string:
        index = 0
        # Traverse the string from left to right
        while index < len(string) and alpha_only:
            # Obtain the character at the index position
            c = string[index]
            # Determine if character is upper case
            is_upper = c >= "A" and c <= "Z"
            # Determine if character is lower case
            is_lower = c >= "a" and c <= "z"
            # Character is alphabetical if either upper or lower. The moment it is
            # neither, the loop ends b/c boolean alpha_only becomes False.
            alpha_only = is_upper or is_lower
            # Advance to the next character
            index += 1
    else:
        # Input string is null.
        alpha_only = False
    return alpha_only
    # end method is_alphabetical


### Letters only
def letters_only(string: str) -> str | None:
    transformed_string = None
    # Make sure string is not null
    if string:
        # Initialize an empty string
        transformed_string = ""
        # Traverse the input string
        for c in string:
            if (c >= "A" and c <= "Z") or (c >= "a" and c <= "z"):
                transformed_string += c
    return transformed_string
    # end method letters_only


### Palindrome generator
def generate_palindrome(string: str) -> str | None:
    pali = None
    # Guard against null input
    if string:
        pali = string
        for i in range(len(string) - 1 - len(string) % 2, -1, -1):
            pali += string[i]
    return pali
    # end method generate_palindrome


### Palindrome detector
def is_palindrome(string: str) -> bool:
    is_pali = False
    # Guard against null input
    if string:
        string = string.upper()
        rightbound = 0
        leftbound = len(string) - 1
        is_pali = True
        # Start traversing string from both ends. Loop ends when mismatched 
        # pair of characters found or when left and rightbound traversals 
        # meet (at the middle of the alphanumerical string)
        while is_pali and rightbound <= leftbound:
            rb = string[rightbound]
            lb = string[leftbound]
            # Make sure that rightbound and leftbound characters are alphanumerical 
            # only. If either of them is not alphanumerical advance to to its next 
            # one (+1 for rightbound, -1 for leftbound)
            if not ((rb >= "A" and rb < "Z") or (rb >= "0" and rb <= "9")):
                rightbound += 1
            elif not ((lb >= "A" and lb <= "Z") or (lb >= "0" and lb <= "9")):
                leftbound -= 1
            else:
                is_pali = lb == rb
                leftbound -= 1
                rightbound += 1
    return is_pali
    # end method is_palindrome


# --------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# --------------------------------------------------------------------------------#
#

# 
# Testing here is done a bit more formally than using simple print statements.
# This type of testing is called "Unit Testing" and can be extremely useful.
# Unit testing applies to small components of the software we write -- in this
# case the units tested are the individual methods we wrote.
#

import unittest

class TestStringMethods(unittest.TestCase):

    def test_intersection(self):
        self.assertEqual(intersection("airplanes", "repairman"), "airpne")
        self.assertEqual(intersection("abc", "def"), "")
        self.assertEqual(intersection("hello", "hello"), "hello")
        self.assertEqual(intersection("aaaa", "aaa"), "a")
        self.assertEqual(intersection("", "abc"), None)
        self.assertEqual(intersection("abc", ""), None)
        self.assertEqual(intersection("", ""), None)
        self.assertEqual(intersection("abc", "cab"), "abc")  # preserves order of `foo`

    def test_is_alphabetical(self):
        self.assertTrue(is_alphabetical("abcXYZ"))
        self.assertFalse(is_alphabetical("abc1"))
        self.assertFalse(is_alphabetical("hello!"))
        self.assertFalse(is_alphabetical(" "))
        self.assertFalse(is_alphabetical(""))
        self.assertFalse(is_alphabetical(None))
        self.assertTrue(is_alphabetical("ZzAaBb"))

    def test_letters_only(self):
        self.assertEqual(letters_only("abc123XYZ!@#"), "abcXYZ")
        self.assertEqual(letters_only("!@#$%^&*()"), "")
        self.assertEqual(letters_only(""), None)
        self.assertEqual(letters_only(None), None)
        self.assertEqual(letters_only("LettersONLY"), "LettersONLY")

    def test_generate_palindrome(self):
        self.assertEqual(generate_palindrome("mice"), "miceecim")
        self.assertEqual(generate_palindrome("mad"), "madam")
        self.assertEqual(generate_palindrome("a"), "a")
        self.assertEqual(generate_palindrome(""), None)
        self.assertEqual(generate_palindrome(None), None)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))
        self.assertFalse(is_palindrome("Hello"))
        self.assertFalse(is_palindrome("Palindrome"))
        self.assertFalse(is_palindrome(""))
        self.assertFalse(is_palindrome(None))


# This allows the test to be run from the command line using `python -m unittest filename.py`
if __name__ == '__main__':
    unittest.main()
