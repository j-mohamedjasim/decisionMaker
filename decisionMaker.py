import random

answer = ['Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No','Yes','No',]

question = input('What do you need help with making decision? ')

ans = []

def answ():
    for i in range(10):
        
        a = random.choice(answer)
        ans.append(a)

        #print(a)
    c1 = ans.index('Yes')
    c2 = ans.index('No')
    print()
    print(question)
    print()
    print('Yes: ',c1)
    print('No:',c2)


answ()