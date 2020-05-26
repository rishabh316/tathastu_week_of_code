#Check for odd even number

def oddeven(n):
    if n%2==0:
        print(n,"ia an EVEN number")
    else:
        print(n,"is an ODD number")
#Check for prime number
 def prime(n):
    if n>0:
        for i in range(2,n):
            if n%i==0:
                print(n,"is NOT a PRIME NUMBER")
                break
        else:
            print(n,"is a PRIME NUMBER")
    else:
        print("Enter positive number=")
#Check for palindrome number

def palindrome(n):
    x=str(n)
    y=str(n)[::-1]
    if x==y:
        print(n,"is a palindrome number")
    else:
        print(n,"is not a Palindrome number")
 
 #Check for Armstrong number

def armstrong(n):
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp=temp//10
    if sum==n:
        print(n,"is an Armstrong number")
    else:
        print(n,"is not an Armstrong number")

num=int(input("Enter the number which you want to check="))
oddeven(num)
prime(num)
palindrome(num)
armstrong(num)
