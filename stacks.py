#Stack is a list with restriction that insertion and deletion can only be done at one end called TOP
#LIFO
class stack:

    def __init__(self,arr):
        self.arr = arr
        self.counter = len(self.arr)-1  #Counter stores the index of the top 
    def push(self, num1):       #Appends the number at the end of the top
        self.arr.append(num1) 
        self.counter+=1
    def pop(self):      #Deletes the number at the top of the list
        if self.counter >=1 :
            del(self.arr[self.counter])
            self.counter-=1
        else:
            print('Can\'t pop anymore')
    def top(self):      #Prints the number at the top of the list
        print('{}'.format(self.arr[self.counter]))
    def isempty(self):  #If the array is not zero then gives false 
        if len(arr)>1:
            return False
        else:
            return True
    
arr=[1,2,3,2]
s1 = stack(arr)
s1.top()
s1.pop()
s1.top()
s1.push(8)
s1.top()
print(arr)
print(s1.isempty())
for i in range(len(arr)):
    s1.pop()
