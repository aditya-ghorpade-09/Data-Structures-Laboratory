from collections import deque

queue = deque()

def addCall(customerID, callTime):
    queue.append((customerID, callTime))

def answerCall():
    if queue:
        return queue.popleft()
    else:
        return None

def viewQueue():
    for call in queue:
        print(call)

def isQueueEmpty():
    return len(queue) == 0

addCall("C001", 5)
addCall("C002", 3)
addCall("C003", 7)

viewQueue()
print("Answering:", answerCall())
viewQueue()
print("Queue Empty?", isQueueEmpty())










# from collections import deque

# queue = deque()

# def addCall():
#     customerID = input("Enter Customer ID: ")
#     callTime = int(input("Enter Call Time (in minutes): "))
#     queue.append((customerID, callTime))
#     print("Call added to queue.")

# def answerCall():
#     if queue:
#         call = queue.popleft()
#         print("Answering call:", call)
#     else:
#         print("No calls in queue.")

# def viewQueue():
#     if queue:
#         print("Calls in queue:")
#         for call in queue:
#             print(call)
#     else:
#         print("Queue is empty.")

# def isQueueEmpty():
#     if len(queue) == 0:
#         print("Queue is empty.")
#     else:
#         print("Queue is not empty.")

# while True:
#     print("\n--- Call Center Menu ---")
#     print("1. Add Call")
#     print("2. Answer Call")
#     print("3. View Queue")
#     print("4. Check if Queue is Empty")
#     print("5. Exit")
    
#     choice = input("Enter choice: ")
    
#     if choice == "1":
#         addCall()
#     elif choice == "2":
#         answerCall()
#     elif choice == "3":
#         viewQueue()
#     elif choice == "4":
#         isQueueEmpty()
#     elif choice == "5":
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice. Try again.")