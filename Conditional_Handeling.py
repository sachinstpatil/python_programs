import sys

type = sys.argv[1]

if type == "t2.micro":
    print ("t2.micro belongs to the free tier")
elif type == "t3.micro":
    print ("t3.micro belongs to the free tier")
else:
    print (f"{type} does not belong to the free tier")