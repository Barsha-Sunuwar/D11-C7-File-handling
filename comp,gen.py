'''#HW3//Write a program to find prime numbers from 1 to 2500 using list compression.#
list = [x for x in range(2,2500) if all(x%y!=0 for y in range(2,x))]
print(list)'''

#HW4//Write a program that uses map to convert a list of temperature in Farenheit to Celsus.#
list_f = [20,30,40,50,60.5,75.5]
list_c = list(map(lambda x:((x-32)/1.8), list_f))
print(list_c)