#To write to a file until i want to.#
'''create=open("File1.txt",'w')
text=input("write to the file/write exit to stop ")
while text!='exit':
   create.writelines(text+'\n')
   text=input()
print("Done with writing now save")
create.close()'''
#Using write, append,read#
'''f=open("File1.txt",'w')
f.writelines("This is my \n life")
f.close()'''

'''f=open("File1.txt",'a')
f.writelines("\n faRSOIIIIII")
f.close()'''
with open("File1.txt","r") as f:
   text=f.read()
print(text)