import os
import csv

csv_load = os.path.join("python_challenge/PyBank/Resources/data_budget.csv")


with open (csv_load) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    csv_header = next(csvreader)
    print(f"csv Header: {csv_header}")

    
    date = []
    pro_los = []


    for row in csvreader:
        

        date.append(row[0])
    
        
        print("---------------------------------------------------------------------")

        print("Financial Analysis")
        print("---------------------------------------------------------------------")
        print(f"Total Months: {len(date)}")
        pro_los.append(int(row[1]))
        print(f"Total: $",sum(pro_los))

    

    total_rev = []

    for x in range (0,len(pro_los)):
        rev = sum(pro_los)
    print(f"Total profit and loss is {rev}")



    a_changes = []

    for i in range(1,len(date)):
     change = pro_los[i] - pro_los[i-1]
     a_changes.append(change)

    average_change=sum(a_changes)/len(a_changes)
print(f"The average of change is {average_change}")
    


def largest (arr,n):
    max = arr[0]

    for i in range (1, n):
        if arr[i] > max:
            max = arr[i]
    return max
arr = pro_los
n = len(arr)
increase = largest(arr,n)
print (f"Greatest increase number is {increase} ")
print (date[25])


def lowest (arr,n):
    min = arr[0]

    for i in range (1,n):
        if arr[i] < min:
            min = arr[i]
    return min
arr = pro_los
n = len(arr)
decrease = lowest(arr,n)
print (f"Greatest decrease number is {decrease}")
print (date[44])

print("-------------------------------------------------------------------------")
