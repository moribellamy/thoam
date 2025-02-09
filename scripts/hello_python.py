# e.g. chatgpt
# how do i use python to convert a string like '2024-02-01' into a native date object?

from datetime import datetime

date_string = '2024-02-01'
date_object = datetime.strptime(date_string, '%Y-%m-%d').date()

print(date_object)  # Output: 2024-02-01
print(type(date_object))  # Output: <class 'datetime.date'>