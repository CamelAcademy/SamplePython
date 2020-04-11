# w - will over write
# a will append at end
#r+ for both read and write


employee_file = open("employee.txt","r+")
employee_file.write("Kelly- Couster Service\n") #excape char
print(employee_file.read())
employee_file.close()
