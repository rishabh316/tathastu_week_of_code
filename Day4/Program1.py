tup=(10,10,5,2,1,0,5,6,3,2,4,10,1,9)
print("Choose elements from given tuple",tup)

def count(tup,num): 
	return tup.count(num)


first=int(input("Enter first element "))
second=int(input("Enter second element "))
third=int(input("Enter third element "))

print(first ,"occur",count(tup,first),"times")
print(second ,"occur",count(tup,second),"times")
print(third ,"occur",count(tup,third),"times")
