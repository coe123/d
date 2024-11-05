def greedy(arr, capacity):
	total_profit = 0
	for item in arr:
    	if item[2] <= capacity:
        	capacity -= item[2]
        	total_profit += item[1]
        	item.append(1)
    	else:
        	fraction = capacity / item[2]
        	total_profit += item[1] * fraction
        	item.append(fraction)
        	break
	print("Total Profit:", total_profit)
	print("------------------------------------------")
	for item in arr:
    	if len(item) > 4:
        	print(f"Object Inserted: {item[0]} Fraction: {item[4]}")
        	print("------------------------------------------")

n = int(input("Enter the number of objects: "))
print("------------------------------------------")
processes = []
capacity = int(input("Enter the capacity of the knapsack: "))
print("------------------------------------------")

for i in range(n):
    process = []
    process.append(i + 1)
    profit = int(input("Enter the Profit of object: "))
    process.append(profit)
    weight = int(input("Enter the Weight of object: "))
    process.append(weight)
    process.append(profit / weight)
    processes.append(process)

print("------------------------------------------")
print(f" ID\tPROFIT\tWEIGHT\tRATIO")
for i in processes:
	print(f" {i[0]}\t{i[1]}\t{i[2]}\t{i[3]}")
print("------------------------------------------")

processes.sort(key=lambda x: x[3], reverse=True)
greedy(processes, capacity)
