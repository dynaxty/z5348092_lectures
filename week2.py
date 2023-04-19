#variable containing textual information
tic = "QAN.AX"


#to compare float nukbers
#use isoclose
import math
f = 0.2 + 0.2 + 0.2
print(math.isclose(f, 0.6))

#strings
a="happy"
a='happy'
a='''happy'''
a="""happy"""
print(a)

#senetnces wit '
x="Connor's so nice"
print(x)

x= '''hi:
"said Connor" '''
print(x)

x='''John said: "Lets's learn python together"'''
print(x)

#Numbers

#== is to test true or false
a=1
testb=1==1
print(testb)

#float is wrong
f=0.2+0.2+0.2
print(f==0.6)

#use isclose function
import math
f=0.2+0.2+0.2
print(math.isclose(f,0.6))

#booleans true or false
#<less >more >=more n equal  == equal

print(1>2) #false as not true
print (1==1.0)

#not true = false
#not false = true

#none type none cant be added to anything else
#a= 2+None
#print(a)

#to check a type

a=1
print (type(a)) #class int

xstr= '1'
print(type(xstr)) #str

test= x == xstr #false
print(test)
print(type(test)) #bool

print(1+2) #3 add numbers together

print ('1'+'2') #12 add both tgt if string

#cant add integer to strinh
#print ('1' + 2) error

print ('x' * 2) # multiplying strings  2times of x

x="b"
print(x)
print(type(x))

#convert from lower to uper ways to convert to upper
x=('abc')
xup=str.upper(x)
print(xup)

x=str.upper('abc')
print(x)

y='abc'.upper() #reccomended
print(y)

weird_case = "HAPPY" #issue
print ("weird_case.lower = weird_case.lower()")

#required - reg_parm
#optional -
#default -
#multiple value -

x="Hi".center(40)
print(x)

x="Hi".center(40, '-') #to add lines
print(x)

#mix text n data anything within curly brackets will take keys
a= True
b=2
x= (f"the value of a is {a} and b is {b}")
print(x)

#or

a= True
b=2
x= ("the value of a is {} and b is {}".format(a,b))
print(x)

#names must only start wit alphabet or underscore
# cant use some like import true false

length = 56
width = 33
Height = 30.5
volume = length * width * Height
print(f"the volume of the box is {volume} cubic centermeter")

#list
lst= [1,2,3]
print(lst)

t=type(lst)
print(t)

#empty list
lst =[]
lst=list()

#in list = 0 1 2 3 4
#from back -1 -2 -3 -4
a = ['h','a','f','l','m']
print(a[1])

#list slicing except the last one

lst = ("1","2","hi","3","hi","2")
print (lst [0:4] )

#append

lst_a = [1] # lst_a is [1]
list.append(lst_a, 2) # lst_a is now [1, 2]
print(lst_a)

lst_a = [1] # lst_a is [1]
lst_a.append(2) # lst_a is now [1, 2]
print(lst_a)

lst_a = [1]
lst_b = [2]
lst_a.extend(lst_b)
print(lst_a)

#removing method
lst = [1, "string", True, None, True]
print(f"Original lst is {lst}")
lst.remove(True) ### take a look of the output, 1 will be removed.
print(f"lst after removing the first True is {lst}")
lst.pop(2)
print(f"lst after removing the element CURRENTLY at index 2 is {lst}")
lst.pop()
print(f"lst after removing the CURRENT last element is {lst}")

#reverse
lst = [1,2,3]
lst.reverse()
print (lst)

#length
lst=[1, "string", True, None, True]
a =len(lst)
print(f"it has {a} length") #(f command)

#split
line= "con con is the best wee"
x =line.split()
print(x)

line = 'From nickname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020'
domain = line.split()[1].split('@')[1]
print(domain)

#list []
#set {}

#page 97