from random import randint
list = []
print(list)
for i in range(10):
  list.append(randint(0,100))
print(list)

def bublle_sort(array):
    lenght = len(array)
    for i in range(lenght):
        for j in range(lenght - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        
    
    return array

print(bublle_sort(list))