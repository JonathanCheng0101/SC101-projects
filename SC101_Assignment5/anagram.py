"""
File: anagram.py
Name:
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

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
Python_List = []              # a list to carry all the words from the FILE
Count = 0                     # used in pre_fix() to test if startswith() == True
Number = 0                    # the number of anagrams
Answer_list = []              # a list to carry all the answer anagrams


def main():
    global Answer_list, Number
    print("Welcome to stanCode\"Anagram Generator \"")
    read_dictionary()
    while True:

        word = input("Find anagram for: ")
        if word == EXIT:
            break
        print("Searching....")
        Answer_list = []   # 記得資料儲存結構不受stackframe影響
        Number = 0
        find_anagrams(word)
        print(f"{word}    has {Number} anagrams.")
        print(Answer_list)


def read_dictionary():
    global Python_List
    with open(FILE, "r") as f:
        for word in f:
            word = word.strip("\n")
            Python_List.append(word)


def find_anagrams(s):
    """
    :param s:
    :return: nothing
    """
    word_number_list = []
    for i in range(0,len(s)):
        word_number_list.append(i)

    find_anagram_helper(s,"", [],word_number_list)


def find_anagram_helper(s, cur,cur_num,word_number_list):
    """

    :param s: input word
    :param cur: ""
    :param cur_num: [] change the word into index order
    :param word_number_list: ex dog-->[0,1,2]
    :return:
    """
    global Number
    if len(s) == len(cur_num):  # base case
        for i in cur_num:
            cur += s[i]  # num-->word
        if cur in Python_List:
            print(f"Found:{cur}")      # plz help:when same string shows in one word twice, the function doubled the numbers it found
            Number += 1
            Answer_list.append(cur)
            pass
    else:
        for i in word_number_list:
            if i in cur_num:
                pass
            else:
                cur_num.append(i)   # choose
                find_anagram_helper(s, cur, cur_num, word_number_list)    # explore
                cur_num.pop()   # un-choose



def has_prefix(sub_s):
    """
    :param sub_s:
    :return: True or False
    """
    global Count
    for word in Python_List:
        if word.startswith(sub_s) == True:
            return True
        Count += 1
    if Count == 0:
        return False


if __name__ == '__main__':
    main()
