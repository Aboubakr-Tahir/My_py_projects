#u can assign the number of desks u want here
number_of_desks=3


A=list(range(number_of_desks,0,-1))
B=[]
C=[]

#a little print to show us the starting desk positions in each rode (rode=list in this code)
print(A,B,C,'\n')


def hanoi(n,source,auxiliary,target):
    #base case:
    if n <= 0 :
        return
    #first recursion making the n-1 disks go to the auxiliary desk
    hanoi(n-1,source,target,auxiliary)
    #this commend to make the nth disk go to the target rode
    auxiliary.append(source.pop())
    #print the changes
    print(A,B,C,'\n')
    #second recursion making the n-1 desk in the auxiliary to go to target rode
    hanoi(n-1,auxiliary,source,target)

hanoi(number_of_desks,A,B,C)        