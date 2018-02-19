def Binary_search(target, array):
   minimum = 0
   maximum = len(array) - 1
   while True:
      if maximum == (minimum + 1):
         if array[maximum] == target:
            return maximum
         elif array[minimum] == target:
            return minimum
         else:
            return -1
      else:  
         guess = int(((maximum - minimum) / 2) + minimum)
         if array[guess] == target:
            return guess
         elif minimum > maximum:
            return -1
         elif target > array[guess]:
            minimum = guess + 1
         elif target < array[guess]:
            maximum = guess - 1         

array = [1, 15, 26, 36, 52, 74, 75, 84, 91, 99, 100]

print("Array: ", array)

for number in array:
   print("Index of {}: ".format(number), Binary_search(number, array))

print("Index of {}: ".format(17), Binary_search(17, array))
print("Index of {}: ".format(53), Binary_search(53, array))
print("Index of {}: ".format(101), Binary_search(101, array))
print("Index of {}: ".format(0), Binary_search(0, array))
