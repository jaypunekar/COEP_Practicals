file1 =open("abc.txt","w")
lines =["Hello", "We enjoy", "File handling"]
file1.writelines(lines)
print("Data written successfully")
file1.close()