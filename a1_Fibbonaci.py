# Non-recursive fibonacci
import time
n = int(input("Enter the number of elements in fibonacci series: "))
start_time = time.time()
a = n - 2
l = [0, 1]
no1 = 0
no2 = 1
count = 1
for i in range(a):
    no3 = no1 + no2
    print("Step ", count, " : ", no1, "+", no2, "=", no3)
    no1 = no2
    no2 = no3
    l.append(no3)
    count = count + 1
print("Total Step-count: ", count - 1)
print(l)
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time)
print("--------------------------------------------------------------")

# Recursive fibonacci
n = int(input("Enter the number of elements in fibonacci series: "))
start_time = time.time()
a = n - 2
l = [0, 1]

def fibo(l, a, no1, no2, count1):
    if a == 0:
        print("Total Step-count: ", count1 - 1)
        return
    else:
        no3 = no1 + no2
        print("Step ", count1, " : ", no1, "+", no2, "=", no3)
        no1 = no2
        no2 = no3
        l.append(no3)
        a = a - 1
        count1 = count1 + 1
        fibo(l, a, no1, no2, count1)

fibo(l, a, 0, 1, 1)
print(l)
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time)
print("--------------------------------------------------------------")
