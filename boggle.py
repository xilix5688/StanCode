"""
TODO: The program asks the user to input 4*4 letters, and finds words that match to the words in the dictionary.
"""

import time
from itertools import chain

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

ROW = 4
COL = 4
LENGTH_OF_LETTERS = 7

dictionary = []


def main():
	"""
	The program asks the user to input 4*4 letters, and finds words that match to the words in the dictionary.
	"""
	start = time.time()
	####################
	input_list = []
	read_dictionary()
	for i in range(ROW):
		input_letters = input(str(i+1) + ' row of letters: ').lower()
		input_list.append([])
		for k in range(COL):
			letter = input_letters.split()[k]
			if letter.isalpha() and len(letter) == 1:
				input_list[i].append(letter.lower())
			else:
				print('Illegal input')
				break

	found_list = find_word(input_list)
	print('There are %d words in total.' % (len(found_list)))

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_word(input_list):
	word_list = flatten(input_list)
	found_list = []
	for i in range(len(input_list)):
		for k in range(len(input_list[0])):
			find_word_helper(word_list, '', i, k, found_list)
	return found_list


def find_word_helper(word_list, current, last_row, last_col, found_list):
	if current in dictionary and len(current) >= 4 and current not in found_list:
		print('Found: ', current)
		found_list.append(current)

	for i in range(len(word_list)):
		row, col, letter = word_list[i]
		if (-1 <= (int(row) - int(last_row)) <= 1) and (-1 <= (int(col) - int(last_col)) <= 1):
			if has_prefix(current + letter) is True:
				# choose
				current += letter
				# explore
				find_word_helper(word_list, current, last_row, last_col, found_list)
				# un-choose
				current = current[:-1]


def flatten(input_list):
	# convert 2d list to 1d list
	input_row_col = []
	for i in range(len(input_list)):
		for k in range(len(input_list[0])):
			input_row_col.append((i, k, input_list[i][k]))
	return input_row_col


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dictionary
	with open(FILE, "r") as f:
		for letter in f:
			words = letter.split('\n')[0].strip()
			if len(words) >= 4:
				dictionary += words


def has_prefix(sub_s):
	"""
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(str(sub_s)):
			return True
	return False


if __name__ == '__main__':
	main()
