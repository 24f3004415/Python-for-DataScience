#!/usr/bin/env python3
def is_palindrome_number(n: int) -> bool:
	"""Return True if integer n is a palindrome (reads the same forwards/backwards).

	Negative numbers are not considered palindromes.
	"""
	if n < 0:
		return False
	s = str(n)
	return s == s[::-1]


def main() -> None:
	try:
		s = input("Enter an integer: ").strip()
		# Convert to int to validate input (allows leading + or -)
		n = int(s)
	except ValueError:
		print("Invalid input. Please enter a valid integer.")
		return

	if is_palindrome_number(n):
		print(f"{n} is a palindrome.")
	else:
		print(f"{n} is not a palindrome.")


if __name__ == "__main__":
	main()

