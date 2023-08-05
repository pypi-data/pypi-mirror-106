import random as rand


def generate_password():
 all_kind_of_letters_in_password = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
    "s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","u",
    "V","W","X","Y","Z",]
 all_kinds_of_special_charecters_in_password = ["!","@","#","$","%","&","1","2","3","4","5","6","7","8","9",]
 password = ["0","1","2","3","4","5","6","7"]


 #------------------------------------------------------------------------------------------------
 which_password_index_should_have_numbers_and_special_chars = rand.choice(password)

 #0
 if which_password_index_should_have_numbers_and_special_chars == "0":
    password[0] = rand.choice(all_kinds_of_special_charecters_in_password)
 else:
    password[0] = rand.choice(all_kind_of_letters_in_password)
 #1
 if which_password_index_should_have_numbers_and_special_chars == "1":
    password[1] = rand.choice(all_kinds_of_special_charecters_in_password)
 else:
    password[1] = rand.choice(all_kind_of_letters_in_password)
 #2
 if which_password_index_should_have_numbers_and_special_chars == "2":
     password[2] = rand.choice(all_kinds_of_special_charecters_in_password)
 else:
    password[2] = rand.choice(all_kind_of_letters_in_password)
 #3
 if which_password_index_should_have_numbers_and_special_chars == "3":
    password[3] = rand.choice(all_kinds_of_special_charecters_in_password)
 else:
    password[3] = rand.choice(all_kind_of_letters_in_password)
 #4
 if which_password_index_should_have_numbers_and_special_chars == "4":
     password[4] = rand.choice(all_kinds_of_special_charecters_in_password)
 else:
    password[4] = rand.choice(all_kind_of_letters_in_password)
 #5
 if which_password_index_should_have_numbers_and_special_chars == "5":
    password[5] = rand.choice(all_kinds_of_special_charecters_in_password)
 else:
    password[5] = rand.choice(all_kind_of_letters_in_password)
 #6
 if which_password_index_should_have_numbers_and_special_chars == "6":
    password[6] = rand.choice(all_kinds_of_special_charecters_in_password)
 else:
    password[6] = rand.choice(all_kind_of_letters_in_password)
 #7
 if which_password_index_should_have_numbers_and_special_chars == "7":
    password[7] = rand.choice(all_kinds_of_special_charecters_in_password)
 else:
    password[7] = rand.choice(all_kind_of_letters_in_password)   
 
 generated_password = ''.join(map(str,password))
 return generated_password
