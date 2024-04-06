two_digit_number = input ()
# Don't change the code above. 
# the goal is a programm which will add the two numbers from the input
# above. It should print X + Y = Z Write the code below.

# input is string. so first I need to get both numbers like so

#first_number = two_digit_number [0]
#second_number = two_digit_number [1]

# this is for debugging purposes
#print(first_number, second_number)
# works so far

# now i need to get the result. strings can't be added into numbers so I need 
# to change them into integers 
result = (int(two_digit_number[0])+int(two_digit_number[1]))
result_in_str = str(result)
#debuging again
#print(result)
# also works
# now we need to print the whole thing as stated above. since 'result' is defined as string
#  in 'result_ins_str', there should not be any problems wirh concatenation
print(two_digit_number[0] + "+" + two_digit_number[1] + "=" + result_in_str)

