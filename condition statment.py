# Grades on the basis of marks 

marks= int(input())
#>= 90 excellent 
#70-90 Good 
#70-40 fair  
#<40 bad 

if marks >= 90:
   print ("excellent")
elif marks >=70:
  print("good")
elif marks >=40:
  print ("fair")
else:
  print ("bad")
