#To write to a file until i want to.#
'''create=open("File1.txt",'w')
text=input("write to the file/write exit to stop ")
while text!='exit':
   create.writelines(text+'\n')
   text=input()
print("Done with writing now save")
create.close()'''

'''#Using write, append,read#
f=open("File1.txt",'w')
f.writelines("This is my \n life")
f.close()

f=open("File1.txt",'a')
f.writelines("\n Namaste welcome to Nepal")
f.close()
with open("File1.txt","r") as f:
   text=f.read()
print(text)

#To change #
f=open("File1.txt",'w+') #w+ do both read and write#
f.writelines("Hello world")
f.seek(6)
f.writelines("everyone")
f.close()

# Code to add/update the file at particular location.#
n_text=input("What do you want to add/update")
loc=int(input('enter the location'))
f1=open('File.txt','r')
old_text=f1.readline()
print(old_text)
f1.seek(loc)
new_text=old_text[:loc]+n_text+old_text[loc:]'''

#HW1//Write a program that copies content of one file to other file.#
with open("file.txt") as f:
    with open("file1.txt","w") as f1:
        for line in f:
            f1.write(line)


#HW2//Write a program that corrects this: Hello-This-is-Python-class.#
files=open("File1.txt", 'r+')
files.writelines("Hello-This-is-Python-class.\n")
text1=files.readline()
print(text1)
text2=text1.replace('-',' ')
print(text2)
files.close()