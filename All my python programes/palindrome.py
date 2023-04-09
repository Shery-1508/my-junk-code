def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	check = True

	new_string = input_string.lower().replace(" ","")
	reverse_string = input_string.lower().replace(" ","")

	for i in range(1,len(new_string)):
		print(f"new_string[{i-1}]{new_string[i-1]}  == reverse_string[-{i}]:{reverse_string[-i]:}")
		if new_string[i-1] == reverse_string[-i]:
			check = True
		else:
			return False # directly returning when string not same 
	
	return check

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
print(is_palindrome("BottoB")) 
