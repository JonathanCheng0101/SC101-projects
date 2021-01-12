"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
Python_List = []
Count = 0
Found_List = []


def main():
	"""
	TODO:
	"""
	i = 0
	row = []
	for i in range(0,4):
		row_i = input(f"{i+1} row of letter:").lower()
		row_i = list(row_i)
		row.append(row_i)
		if len(row_i) != 4:      # let's first forget about the blank issue
			print("Illegal input")
		else:
			i += 1
	read_dictionary()
	boggle(row)
	print(f"There are {len(Found_List)} words in total!")
	print("done searching yaya ")


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global Python_List
	with open(FILE, "r") as f:
		for word in f:
			word = word.strip("\n")
			Python_List.append(word)


def boggle(row):
	print("searching...")
	for i in range(4):                  # 做出一個對應4*4的座標系統
		for j in range(4):
			boggle_helper(row, [i, j], [], "", i, j)


def boggle_helper(row, used_position, used_position_list, cur_str, x, y):
	global Found_List
	used_position_list.append(used_position)

	if cur_str in Python_List and len(cur_str) >= 4:      # base case
		if cur_str not in Found_List:
			Found_List.append(cur_str)
			print(f"Found: {cur_str}")
			boggle_helper(row, [x, y], used_position_list, cur_str, x, y)
			used_position_list.pop()     # 找到字以後記得要把它的位置退掉，要不然就不能找其他的

	for i in range(-1, 2):           # recursive case    (不用else: 所以就算是找到room，他還是會繼續找其他的而不會就停下來)
		for j in range(-1, 2):
			new_x = x + i
			new_y = y + j

			if len(cur_str) == 0:  # 找新的字母把做開頭的時候
				cur_str += row[x][y]

			if [new_x, new_y] not in used_position_list:   # 代表新的new_x, new_y沒有走回之前的老路
				if 0 <= new_x < 4 and 0 <= new_y < 4:
					cur_str += row[new_x][new_y]      # 把新的字母家在原本就有的字母之後

					if has_prefix(cur_str) == True:            # 測試一下cur_str開頭的字存不存在
						boggle_helper(row, [new_x, new_y], used_position_list, cur_str, new_x, new_y)  # 存在的話繼續找新鄰居試試看
						cur_str = cur_str[:len(cur_str) - 1]   # 要backtracking，把原本的字母退掉
						used_position_list.pop()               # 把之前那個字母的位置從used_position_list裡面退掉
					else:
						cur_str = cur_str[:len(cur_str)-1]     # 不存在的話把原本的這個字母退掉


def has_prefix(sub_s):
	global Count
	for word in Python_List[:]:
		if word.startswith(sub_s) == True:
			return True
	else:
		return False


if __name__ == '__main__':
	main()
