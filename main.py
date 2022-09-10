# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
comb_name=l_name1+l_name2
combined_name=comb_name.lower()

first_digit=str(combined_name.count('t')+combined_name.count('r')+combined_name.count('u')+combined_name.count('e'))

sec_digit=str(combined_name.count('l')+combined_name.count('o')+combined_name.count('v')+combined_name.count('e'))

# print(first_digit)
# print(sec_digit)

final_score=int(first_digit+sec_digit)
# print(final_score)

if final_score<10 or final_score>90:
  print(f"Your score is {final_score}. , you go together like coke and mentos.")
elif 40<=final_score<=50:
  print(f"Your score is {final_score}. , you are alright together.")
else:
  print(f"Your score is {final_score}.")
  

