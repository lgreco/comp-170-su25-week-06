
def longest_word(words: list[str]) -> str:
    """
    Finds and returns the longest word in a list.

    Parameters:
        words (list of str): A list of words.

    Returns:
        str or None: The longest word in the list, or None if the list is empty or None.
    """
    longest = None
    if words is not None and len(words) > 0:
        longest = words[0]
        for word in words:
            # Update if the current word is longer than the longest seen so far
            if len(word) > len(longest):
                longest = word
    return longest


def shortest_word(words: list[str]) -> str:
    """
    Finds and returns the shortest word in a list.

    Parameters:
        words (list of str): A list of words.

    Returns:
        str or None: The shortest word in the list, or None if the list is empty or None.
    """
    shortest = None
    if words is not None and len(words) > 0:
        shortest = words[0]
        for word in words:
            # Update if the current word is shorter than the shortest seen so far
            if len(word) < len(shortest):
                shortest = word
    return shortest


def odd_words(words: list[str]) -> list[str]:
    """
    Returns a list of words that have an odd number of characters.

    Parameters:
        words (list of str): A list of words.

    Returns:
        list of str or None: A list of words with odd lengths, or None if the input is empty or None.
    """
    odds = None
    if words and len(words) > 0:
        odds = []
        for word in words:
            # Check if the word length is odd
            if len(word) % 2 == 1:
                odds.append(word)
    return odds


def average_words(words: list[str]) -> list[str]:
    """
    Returns a list of words whose lengths are within ±1 of the average word length.

    Parameters:
        words (list of str): A list of words.

    Returns:
        list of str or None: Words close to the average length, or None if the input is empty or None.
    """
    averages = None
    if words and len(words) > 0:
        averages = []
        avg = 0
        for word in words:
            # Sum up the lengths of all words
            avg += len(word)
        avg /= len(words)
        for word in words:
            # Include word if its length is within ±1 of the average
            if avg - 1 <= len(word) and len(word) <= avg + 1:
                averages.append(word)
    return averages


def intersect(foo: list[str], bar: list[str]) -> bool:
    """
    Checks whether two lists of words share at least one word in common.

    Parameters:
        foo (list of str): First list of words.
        bar (list of str): Second list of words.

    Returns:
        bool: True if there is any common word between the two lists, False otherwise.
    """
    intersection_found = False
    if foo and bar and len(foo) > 0 and len(bar) > 0:
        f = 0
        while not intersection_found and f < len(foo):
            b = 0
            while not intersection_found and b < len(bar):
                # Check if the current pair of words match
                intersection_found = foo[f] == bar[b]
                b += 1
            f += 1
    return intersection_found


#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# Basic testing. This block validates the logic of the code. Additional 
# requirements such as single return statements are not tested here but 
# must be met anyway.
if __name__ == "__main__":
  testA = ["a", "list", "of", "nearly", "random", "words", "and", "strings"]
  testB = []
  testC = ["a", "be", "cat", "door", 
           "eagle", "galaxy", "forests", "harvests", 
           "important", "journalist"]
  testD = ["Frodo", "Gandalf", "Gollum", "Legolas", "Aragorn", "Rivendell"]
  testE = ["Saruman", "Boromir", "Faramir", "Sauron", "Gollum", "Minas Tirith"]
  testF = None

  # -------- Testing
  print("\nTesting shortest_word")
  if shortest_word(testF) is not None:
    print("shortest_word FAILS null test")
  else:
    print("shortest_word passes null test")

  if shortest_word(testB) is not None:
    print("shortest_word FAILS empty test")
  else:
    print("shortest_word passes empty test")

  if shortest_word(testA) is not testA[0]:
    print("shortest_word FAILS length test")
  else:
    print("shortest_word passes length test")

  # -------- Testing
  print("\nTesting longest_word")
  if longest_word(testF) is not None:
    print("longest_word FAILS null test")
  else:
    print("longest_word passes null test")

  if longest_word(testB) is not None:
    print("longest_word FAILS empty test")
  else:
    print("longest_word passes empty test")

  if longest_word(testA) is not testA[len(testA)-1]:
    print("longest_word FAILS length test")
  else:
    print("longest_word passes length test")
  
  # -------- Testing
  print("\nTesting odd_words")
  if odd_words(testF) is not None:
    print("odd_words FAILS null test")
  else:
    print("odd_words passes null test")
  
  if odd_words(testB) is not None:
    print("odd_words FAILS empty test")
  else:
    print("odd_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if odd_words(testC) != odd_test:
    print("odd_words FAIlS logic test")
  else:
    print("odd words passes logic test")

  # -------- Testing
  print("\nTesting average_words")
  if average_words(testF) is not None:
    print("average_words FAILS null test")
  else:
    print("average_words passes null test")
  
  if average_words(testB) is not None:
    print("average_words FAILS empty test")
  else:
    print("average_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if average_words(testC) != ['eagle', 'galaxy']:
    print("average_words FAILS logic test")
  else:
    print("average_words words passes logic test")

  # -------- Testing
  print("\nTesting intesect")
  if intersect(testF, testA):
    print("intersect FAILS first null test")
  else:
    print("intersect passes first null test")

  if intersect(testA, testF):
    print("intersect FAILS second null test")
  else:
    print("intersect passes second null test")
  
  if intersect(testB, testA):
    print("intersect FAILS first empty test")
  else:
    print("intersect passes first empty test")

  if intersect(testA, testB):
    print("intersect FAILS second empty test")
  else:
    print("intersect passes second empty test")

  if not intersect(testD, testE):
    print("intersect FAILS logic test for true")
  else:
    print("intersect words passes logic test for true")
  
  if intersect(testA, testE):
    print("intersect FAILS logic test for false")
  else:
    print("intersect words passes logic test for false")
