#collective data type in python - list , tuple ,dictionary, set

#1.  List

#eg 1
#list of subjects

l=[]   #This is an empty list
l.append("math")
l.append("accountancy")
l.append("economics")
l.append("business studies")
l.append("english")
print(l)
for i in l :
    print(i)



#eg 2
#list of random things
if(2<3):
    rand=[True , 20.5 , "hey", 100]
    print(rand)
    print(type(rand))
    print(len(rand))
else:
    print("it allows duplicate entries,it is mutable in nature,\
\nit allows indexing,it is enclosed in square brackets")
    


#2. Tuple

#eg 1    
tup = ('python',True ,20.5 ,99 ) 
print(tup)
print(type(tup))
print(len(tup))

#to show tuple is immutable
'''
tup2=("i","am","happy")
tup.append(tup2)
'''



#eg 2
my_tup=("A","B","C","D")
print(my_tup)
z=(my_tup+("E","F"))  #Concatenation
print (z)
print(z*3) #Repetition




#3.set
#eg 1
my_set={"subhangi" ,"is", "a","good","girl","subhangi","is","a","topper"}
print(my_set)
print(type(my_set))
print(len(my_set))



#eg 2
#set of mixed data types -a set cannot have mutable elements like lists or dictionaries as elements

def Set(n1,s2):
    
    my_set = {1.0, "Hello", (1, 2, 3),n1,s2}
    print(my_set)
    for i in my_set:
        print(i)

Set(52.5,"python")




#4. dictionary

#eg 1
n1=input("enter name")
n2=input("enter your city")
n3=input("enter your age")
n4=input("enter your gender")
n5=input("enter your course name")
otp={"name":n1,"city":n2,"age":n3,"gender":n4,"course":n5}
print(otp)
print(type(otp))
print(len(otp))



#eg 2
#marks in 3 subjects
marks={"math":20,"accountancy":40}
print(marks)
marks["business studies"]=60
print("marks obtained in 3rd subject is", marks)

#changing subject(key) name to economics 
new=marks["accountancy"]
del marks["accountancy"]
marks["economics"]=new
print(" final corrected subjects with their marks ",marks)



