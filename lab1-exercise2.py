students = ["Hubert", "Siddhant", "Ian"]
students.sort()
print(students)
first_name = students[0]
first_name = first_name[:-1]
print(first_name)
longest_name = ''
for s in students:
	if len(s) > len(longest_name):
		longest_name = s
print(longest_name)
