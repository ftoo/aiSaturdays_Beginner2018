import random 


ourList = list() 
count = 0 
while (count < 11):
    ourList.append(random.randint(1,10))
    count += 1
  
for i in range(0,4):
    belowFive = random.choice(ourList)
   
print(ourList)
print(belowFive)

