"""
File: anagram.py
Name: 游雅媛
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
# global variable
python_list = []
word_list = []
count = 0


def main():
    """
    The program recursively finds all the anagram(s) for the word input by a user.
    """
    global word_list, count
    read_dictionary()
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    start = time.time()
    while True:
        input_word = input('Find anagrams for: ')

        if input_word == EXIT:
            break
        else:
            print('Searching...')
            found_list = find_anagrams(input_word)
            count = len(found_list)
            print(count, 'anagrams', found_list)

    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:
        for words in f:
            word = words.split('\n')[0].strip()
            python_list.append(word)


def find_anagrams(s):
    found_list = []
    find_anagrams_helper(s, '', found_list)
    return found_list


def find_anagrams_helper(s, current, found_list):
    """
    :param found_list: list of found anagram(s)
    :param current: the searching strings
    :param s: the word input by a user
    """
    global python_list, count
    if (len(s) == len(current)) and current in python_list:
        print("Found:  ", current)
        print("Searching ...")
        count += 1
        found_list.append(current)
    else:
        for i in range(len(s)):
            ele = s[i]
            ele_current = current.count(ele)
            ele_s = s.count(ele)
            if (ele_current < ele_s) and ((current + ele) not in found_list):
                if has_prefix(current) is True:
                    # Choose
                    current += s[i]
                    # Explore
                    find_anagrams_helper(s, current, found_list)
                    # Un-choose
                    current = current[:-1]


def has_prefix(sub_s):
    """
    :param sub_s: string(s) input to check the prefix
    :return: True/ False to check if the word starts with sub_s
    """
    for word in python_list:
        if word.startswith(str(sub_s)):
            return True
    return False


if __name__ == '__main__':
    main()
