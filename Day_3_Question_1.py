import string

def is_pangram(sentence):
  """
  Checks if a sentence contains every letter of the English alphabet at least once.

  Args:
      sentence: The sentence to check.

  Returns:
      "complete" if the sentence is a pangram, "incomplete" otherwise.
  """
  alphabet_set = set(string.ascii_lowercase)
  for char in sentence.lower():
    if char.isalpha() and char in alphabet_set:
      alphabet_set.remove(char)


  return "complete" if not alphabet_set else "incomplete"


print(is_pangram("The quick brown fox jumps over the lazy dog"))
