import random

#Random function will randomly pick one of the item below
answer = ['Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No',]

question = input('What do you need help with making decision? ')
#Picked one by the random function will be append to the list below
ans = []

def answ():#Function to pick random decision
    for i in range(10):#This will pick 10 random items from the answer list above
        
        a = random.choice(answer)
        ans.append(a)

        
    c1 = ans.index('Yes')#This will count how many YES from the ans list above
    c2 = ans.index('No')#This will count how many NO from the ans list above
    print()
    print(question)
    print()
    print('Yes: ',c1)
    print('No:',c2)
    print()


answ()
