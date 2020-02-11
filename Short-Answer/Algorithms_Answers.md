#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    a = 0 O(1)
    while (a < n * n * n):  O()
        a = a + n * n O(1)
    O(1) + (O() * O(1))

b)  
    sum = 0    O(1)
    for i range(n): O(n)
        j = 1 O(1)
        while j < n: 
            j *= 2  O(1)
            sum += 1 O(1)
O(1) + (O(N) * O(1)) * (O(Log n) * O(1) * O(1))
O(1) + (O(n) * O(1)) * O(Log n) 
O(n) * O(Log n)

""""""O(n Log n)""""""
c)
 def bunnyEars(bunnies):
    if bunnies == 0:
        return 0    O(1)

    return 2 + bunnyEars(bunnies - 1) O(n)

    """""O(N)"""""

## Exercise II
Binary search would be the best way 

Start in the middle floor 

Drop the egg

if egg breaks anything above the middle floor is void
if the egg doesnt break and floor below the middle is void

Start from the middle again and repeat until you reach the last remaining floor

