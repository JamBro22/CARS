cars = [56, 78, 34, 21, 56, 34, 125, 45, 89, 75, 12, 56] #declaring list
print(cars) #displaying list
cars.sort() #sorting list
print(cars) #displaying sorted list
print(min(cars),max(cars)) #displaying the smallest and largest numbers in the list
print(sum(cars)) #displaying the sum of all the numbers in the list
cars = list(dict.fromkeys(cars)) #removing duplicates from list
print(cars) #displaying the list without duplicates