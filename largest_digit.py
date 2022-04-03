"""
File: largest_digit.py
Name: 游雅媛
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: the integer
	:return: the largest digit
	"""
	return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(n, current_largest):
	if n < 0:
		n = -n
	if n == 0:
		return current_largest
	else:
		num = n % 10
		if num > current_largest:
			current_largest = num
		return find_largest_digit_helper(n//10, current_largest)


if __name__ == '__main__':
	main()
