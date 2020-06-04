vowel_list = ['a','i','o','e','u']
string_input = input("Enter the string below: ")
vowel_count = 0 

for x in string_input:
    if x in vowel_list:
        vowel_count += 1
    else:
        pass
print(str(vowel_count) +' a ' + str(string_input.count('a')) + ' i ' + str(string_input.count('i')) +  ' o ' + str(string_input.count('o')) + ' u ' + str(string_input.count('u')) + ' e ' + str(string_input.count('e')) )
