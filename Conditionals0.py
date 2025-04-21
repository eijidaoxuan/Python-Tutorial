phone = "+1 234-567-8910"
print(phone[0:4])
print(phone[:4])
print(phone[4:])
print(phone[4:6])
print(phone[-4:])
print(phone[:-4])

#Tuple and List
coordinates_tuple = (1.18203, 2.103794, 3.47905)    #56 bytes
x, y, z = coordinates_tuple
print(x) 
print(coordinates_tuple[0])
coordinates_tuple = (5, 2.103794, 3.47905)
print(coordinates_tuple)

coordinates_list = [1.18203, 2.103794, 3.47905]     #72 bytes
x, y, z = coordinates_list
print(x)
print(coordinates_list[0])
coordinates_list[0] = 5        #Error for tuple
print(coordinates_list)

def main():
    x = input("Name: ").strip()
    if x == "":
        print(hello())
    else:
        print(hello(x))

def hello(x="Master"):
    return f"Welcome {x}"       #return x,y = return (x,y) > returning a tuple      return [x,y,z] > returning a list       return {"x":y,"z":a} = return {a:b} > returning a dictionary

a = 1
b = 4
c = 3
largest = max(a, b, c)        #max function (largest number)
if a == largest:
    print(f"a is the largest {a} points")
elif b == largest:
    print(f"b is the largest {b} points")
elif c == largest:
    print(f"c is the largest with {c} points")

d = [a, b, c]
print(sum(d))        #Add all numbers inside the list