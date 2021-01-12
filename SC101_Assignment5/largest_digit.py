"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""

largest_digit = 0
def main():
	#print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	#print(find_largest_digit(6))          # 6
	#print(find_largest_digit(-111))       # 1
	#print(find_largest_digit(-9453))      # 9

def find_largest_digit(n):
	#global largest_digit
	#largest_digit = 0
	#find_digit_helper(n)


# def find_digit_helper(n):
	global largest_digit

	if n == 0:
		pass

	else:
		# 解決負數的問題
		if n < 0:
			n = -n

		last_digit = n % 10     # 做出餘數(新尾數)
		if last_digit > largest_digit:   # 新尾數跟之前的舊尾數比大小
			largest_digit = last_digit

		find_largest_digit(n//10)

	return largest_digit
















if __name__ == '__main__':
	main()
