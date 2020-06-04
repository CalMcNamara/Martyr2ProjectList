string_input = input("enter you input here.")

reveresed_string = " "
length_of_string = len(string_input)

i = 1
for x in string_input:
    reveresed_string = reveresed_string + string_input[length_of_string-i]
    i+=1 
print(reveresed_string)