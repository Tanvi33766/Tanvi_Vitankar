def is_symmetrical(text):
  """
  Checks if reversing the ASCII values of a string results in the same sequence.

  Args:
      text: The string to check.

  Returns:
      "symmetrical" if the reversed ASCII sequence is the same, "not symmetrical" otherwise.
  """
  if not text:
    return "not symmetrical"
  ascii_values = [ord(char) for char in text]

  return "symmetrical" if ascii_values == ascii_values[::-1] else "not symmetrical"


print(is_symmetrical("acxz"))
