#use in lambda

students = [("Sanika", 23),("Pankaj",26)]

result = sorted(students, key = lambda x : x [1])

print(result)