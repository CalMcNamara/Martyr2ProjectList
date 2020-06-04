# See rules.txt for the rules on pig latin grammer. 

def con_vow():
    piglat_string = input_string[1:] + input_string[0] + 'ay'
    print(piglat_string)

def con_con():
    i = 0
    for x in input_string:
        if x in vowel_list:
            break
        else:
            i+=1
    piglat_string = input_string[i:] + input_string[:i] + 'ay'        
    print(piglat_string)
def vowel():
    piglat_string = input_string + 'yay'
    print(piglat_string)

vowel_list = ['a','e','i','o','u'] # Not using Y as a vowel.
input_string = input("Enter the word you would like to translate: ")
piglat_string = " "




if input_string[0] in vowel_list:
    vowel()
if input_string[0] not in vowel_list and input_string[1] in vowel_list:
    con_vow()
if input_string[0] not in vowel_list and input_string[1] not in vowel_list:
    con_con()

