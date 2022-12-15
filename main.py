import replit
filename = input("please enter the file you want to open (without .txt)\n")
filefull = filename+".txt"
file = open(filefull, "r")
replit.clear()
text = file.read()
print(text)
   
   
   

  

