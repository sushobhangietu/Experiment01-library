class_lower=[]
class_higher=[]
freq=[]
midpoint=[]
c_freq=[]

n=int(input("Enter the number of classes: "))
for i in range(n):
    a=int(input(f"Enter Lower limit of class {i+1}: "))
    b=int(input(f"Enter higher limit of class {i+1}: "))
    c=int(input(f"Enter the freq of class {i+1}: "))
    class_lower.append(a)
    class_higher.append(b)
    freq.append(c)
    midpoint.append((a+b)/2)
    

sum1=0

for i in range(n):
    sum1+=freq[i]
    c_freq.append(sum1)

for i in range(n):
    if(c_freq[i]>=(sum1/2)):
        median_class=i
        break

l=class_lower[median_class]
f1=freq[median_class]
f0=freq[median_class-1]
f2=freq[median_class+1]

h=class_higher[median_class]-class_lower[median_class]

mode = l+(((f1-f0)/(2*f1-f0-f2))*h)

print("Mode: ",mode)
