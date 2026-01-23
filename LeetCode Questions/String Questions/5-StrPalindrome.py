def is_palindrome_two_pointers(s):
  """Checks if a string is a palindrome using two pointers."""
  left_pointer = 0
  right_pointer = len(s) - 1

  while left_pointer < right_pointer:
    if s[left_pointer] != s[right_pointer]:
      return False
    left_pointer += 1
    right_pointer -= 1

  return True

# Example Usage
test_string_1 = "racecar"
test_string_2 = "python"

print(f"'{test_string_1}' is a palindrome: {is_palindrome_two_pointers(test_string_1)}")
print(f"'{test_string_2}' is a palindrome: {is_palindrome_two_pointers(test_string_2)}")
