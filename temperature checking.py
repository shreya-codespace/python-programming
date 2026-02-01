# temperature checking  
temp = int(input())
#25-50-> hot 
#10-24->cold
#<10-> extremely cold 

if  temp <=50 and temp>=25:
  print("hot")
elif temp <=24 and temp>=10:
  print("cold")
elif temp <10:
  print("extremely cold")
