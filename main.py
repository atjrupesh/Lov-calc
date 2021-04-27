# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names_conv = name1 + name2
lower_case_string = names_conv.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t+r+u+e


l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l+o+v+e 

sum3=int(str(true) + str(love))

print(f"your score is  {sum3}")

if ((sum3<10) or (sum3>90)):
 print(f"Your love score is {sum3}, you go together like trump and melania. ")
elif ((sum3>=40) and (sum3<=50)):
 print(f"Your love score is {sum3}, you are alright together. ")

else:
  print(f"your love score is {sum3}")
  
  
  
  
  
  
  
  
# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# names_conv = name1.lower() + name2.lower()



# c1=name1.count("t")+name2.count("t")
# c2=name1.count("r")+name2.count("r")
# c3=name1.count("u")+name2.count("u")
# c4=name1.count("e")+name2.count("e")
# sum1=c1+c2+c3+c4
# c5=name2.count("l")+name1.count("l")
# c6=name2.count("o")+name1.count("o")
# c7=name2.count("v")+name1.count("v")
# c8=name2.count("e")+name1.count("e")
# sum2=c5+c6+c7+c8
# # print(c1,c2,c3,c4)
# # print(c5,c6,c7,c8)
# sum3=int(str(sum1) + str(sum2))

# print(f"your score is  {sum3}")

# if ((sum3<10) or (sum3>90)):
#  print(f"Your score is {sum3}, you go together like trump and melania. ")
# elif ((sum3>=40) and (sum3<=50)):
#  print(f"Your score is {sum3}, you are alright together. ")

# else:
#   print(f"your score is {sum3}")


