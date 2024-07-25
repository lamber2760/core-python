f= open("pose.txt")
data=f.read()
if ("lamber" in data):
    print("the word is present in the data ")
else:
    print("the word is not present in the data")    
f.close()