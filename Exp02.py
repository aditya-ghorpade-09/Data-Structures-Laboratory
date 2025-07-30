def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

salaries = []
n=int(input("Enter the number of salaries you want to enter: "))
for i in range(n):
    salaries.append(float(input(f"Enter salary {i+1}: ")))

print("1. Selection Sort")
print("2. Bubble Sort")
choice = int(input("Choose sorting method: "))

if choice == 1:
    sorted_salaries = selection_sort(salaries.copy())
elif choice == 2:
    sorted_salaries = bubble_sort(salaries.copy())
else:
    sorted_salaries = salaries

top_five = sorted_salaries[-5:]
top_five.reverse()

print("Top 5 highest salaries:")
for salary in top_five:
    print(salary)