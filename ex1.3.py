def minmax(data):
    smallest = largest = data[0]  # Initialize with the first element
    # Iterate through the data to find smallest and largest
    for num in data[1:]: #pheli value to fix, dosri value se shuru kr rhe hen islie 1 se start kra 
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    return (smallest, largest)  # Returning in tuple
# calling the function
numbers = [3, 1, 7, 5, 2]
result = minmax(numbers)
print("Smallest and largest:", result)  # Output: (1, 7)

#pheli value ko do variable assign kre hen take wo comparision ke lie use hoske
#isme ho ye rha ha ke, mene first number ko starting point bana lia or us se age ki list ko compare krwaya hai,
# 3=1 1 chota ha smallest me update ajaegy phr 7 bara ha largest me update ajaegi, ab 5 and 2 age arhe hen or
# smallest and largest key beech me arhe hen islie no change. 