# def countVowels(s):
#     s = s.lower()
#     count = 0

#     for ch in s:
#         if ch in 'aeiou':
#             count +=1
        
        
#     print(count)
# countVowels('Hello')

# def factorial(n):
#     total=1
#     while n>0:
#         total =total *n
#         n -=1
#     return total
# print(factorial(5))

# def sum_of_digit(n):
#     sum=0
#     for i in range(len(str(n))):
#         c=n%10

#         sum =sum +c

#         n=n//10
#     return sum
# print(sum_of_digit(1234))

# def sum_of_digit(n):
#     sum=0
#     while n>0:
#         c=n%10

#         sum =sum +c

#         n=n//10
#     return sum
# print(sum_of_digit(1234))

# def isArmstrong(num):
#     b=num
#     sum=0
#     p=len(str(num))
#     while (num>0):
#         c=num%10
#         sum =sum +c**p
#         num=num//10
#     if sum ==b:
#         return True
#     else:
#         return False
# print(isArmstrong(153))

# def isprime(n):
#     if n <= 1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

# def fibonacci(n):
#     a=0
#     b=1

#     for i in range(n):

#         print(a)
#         c = a + b
#         a=b
#         b=c
# fibonacci(6)

# def Reverse_a_Number(n):
#     r_num=0

#     while n>0:
#         c=n%10
#         r_num=r_num*10+c
#         n=n//10
#     return r_num

# print(Reverse_a_Number(1234))
    

# arr=[3,7,2,9,5]

# def min_max(n):
#     max_num= n[0]
#     min_num=n[0]

#     for i in range (len(n)):
#         max_num=max(max_num,n[i])
#         min_num=min(min_num,n[i])
#     return max_num,min_num
# print(min_max(arr))

# def twoSum(nums, target):
#     d = {}

#     for i in range(len(nums)):
#         num = nums[i]
#         needed = target - num
#         if needed in d:
#             return[d[needed],i]
#         else:
#             d[num]=i
# nums = [2,7,11,15]
# target = 18
# print(twoSum(nums,target))

# def removeDuplicates(arr):
#     # convert to set
#     result=list(set(arr))

#     # convert back to list
    
#     return result


# def removeDuplicates(arr):
#     result = []

#     for num in arr:
#         if num not in result:
#             result.append(num)

#     return result

# b=[1, 2, 2, 3, 4, 4]
# print(removeDuplicates(b))


# def bubbleSort(arr):
#     n = len(arr)

#     for i in range(n):
#         for j in range(n - i - 1):
#             # compare
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#             # swap if needed

#     return arr
# print(bubbleSort([5, 3, 2, 4]))

def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i]== target:
            return i
        
    return -1

print(linearSearch([3,7,2,9,5], 9))