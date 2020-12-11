if __name__ == '__main__':
    print('PyCharm')
the_number_of_correct_answer = 0
# introduction
print("Now i will ask you a few question")
print("this is the first question")
# receive user's answer
answer = int(input("what is the answer of 4 + 2? You can only type number!"))
# evaluate the solution
if answer == 6:
    print("correct")
    the_number_of_correct_answer += 1
else:
    print("wrong")

print("\nthis is the second question")
# ask the user the question
answer = int(input("what is the solution of 5 % 2? You can only type number!"))
# check
if answer == 1:
    print("yes")
    the_number_of_correct_answer += 1
else:
    print("nop")

print("\nthis is third question")
# ask user the question
solution = input("what is the name of the most brilliant programming teacher?\nsymbols you can type are only ? and !")
# evaluation
if solution.lower().strip("?!") == "ubial":
    print("you are right!")
    the_number_of_correct_answer += 1
else:
    print("no,you are wrong~")

print("\nthis is the forth question")
solution = input("which class does Rita love the most?\nsymbols you can type are only ? and !")
if solution.lower().strip("?!") == "cs":
    print("you are right")
    the_number_of_correct_answer += 1
else:
    print("it is not")


print("\nthis is the fifth question")
solution = input("what is SnowWhite's favorite food? \nsymbols you can type are only ? and !")
if solution.lower().strip("?!") == "apple":
    print("yep!")
else:
    print("nop, you don't know snow white well~")


print("\nthis is the sixth question")
print("please choose the best statement below\na.Rita is pretty\nb.Nancy is pretty\nc.Olivia is pretty\nsymbol only?!")
solution = input("what do you choose?")
if solution.lower().strip("?!") == "a":
    print("Sure")
    the_number_of_correct_answer += 1
else:
    print("nop")

percentage = (float(the_number_of_correct_answer) / float(5)) * 100
print("Your percentage of correct answer is" + str(percentage) + "%")
