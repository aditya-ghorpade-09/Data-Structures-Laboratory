def linear_search(arr, key):
    for id in arr:
        if id == key:
            return True
    return False

def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return False

account_ids = []
n=int(input("Enter the number of IDs you want to enter: "))
for i in range(n):
    account_ids.append(int(input(f"Enter ID {i+1}: ")))
    
key = int(input("Which ID you want to search: "))
print("1. Linear search")
print("2. Binary search")
choice = int(input("Enter choice: "))

if choice == 1:
    found = linear_search(account_ids, key)
elif choice == 2:
    account_ids.sort()
    found = binary_search(account_ids, key)
else:
    found = False

if found:
    print("Found")
else:
    print("Not Found")