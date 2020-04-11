employee_file = open("employee.txt","r") # r, w, a, r+

for aRow in employee_file.readlines():
    print(aRow)


print(employee_file.readable())
print(employee_file.readline()) # read a line
print(employee_file.readlines()) # read into Array
print(employee_file.readlines()[1]) # print 1 row in Array
print(employee_file.read()) # read the whole file

employee_file.close()