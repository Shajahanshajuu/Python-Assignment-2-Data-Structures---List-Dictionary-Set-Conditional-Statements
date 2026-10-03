# 1. List Creation[span_2](start_span)[span_2](end_span)
# a. Create a list named age_list with five integer elements[span_3](start_span)[span_3](end_span)
age_list = [24, 25, 26, 27, 28]

# b. Create a list named name_list with five string elements[span_4](start_span)[span_4](end_span)
name_list = ["Rahul", "Sneha", "Kiran", "Meera", "Arun"]

print("Initial age_list:", age_list)
print("Initial name_list:", name_list)
print("-" * 30)


# 2. List Operations / Modifications[span_5](start_span)[span_5](end_span)

# a. Append the string "Yazhini" to name_list[span_6](start_span)[span_6](end_span)
name_list.append("Yazhini")
print("After appending 'Yazhini':", name_list)

# b. Insert the element 30 at index 2 in age_list[span_7](start_span)[span_7](end_span)
age_list.insert(2, 30)
print("After inserting 30 at index 2:", age_list)

# c. Remove the string "Yazhini" from name_list[span_8](start_span)[span_8](end_span)
name_list.remove("Yazhini")
print("After removing 'Yazhini':", name_list)

# d. Pop the last element from age_list[span_9](start_span)[span_9](end_span)
popped_element = age_list.pop()
print("After popping last element:", age_list)

# e. Extend the age_list with additional ages [29, 30, 26][span_10](start_span)[span_10](end_span)
age_list.extend([29, 30, 26])
print("After extending age_list:", age_list)

# f. Sort age_list in descending order[span_11](start_span)[span_11](end_span)
age_list.sort(reverse=True)
print("age_list in descending order:", age_list)

# g. Find Max age, Min age and sum of all ages from age_list[span_12](start_span)[span_12](end_span)
print("Max age:", max(age_list))
print("Min age:", min(age_list))
print("Sum of all ages:", sum(age_list))
print("-" * 30)


# 3. Accessing List Elements[span_13](start_span)[span_13](end_span)

# a. Print the first element of name_list[span_14](start_span)[span_14](end_span)
print("First element of name_list:", name_list[0])

# b. Print the last element of name_list[span_15](start_span)[span_15](end_span)
print("Last element of name_list:", name_list[-1])

# c. Print the elements from index 2 to index 4 in name_list[span_16](start_span)[span_16](end_span)
# Note: Slicing [2:5] includes index 2, 3, and 4
print("Elements from index 2 to 4:", name_list[2:5])

# d. Print the elements of name_list in reverse order[span_17](start_span)[span_17](end_span)
print("name_list in reverse order:", name_list[::-1])
print("-" * 30)


# a. Create a dictionary named student_marks that maps the names of five students to their marks (use scale of from 0 to 100)[span_19](start_span)[span_19](end_span)
student_marks = {
    "Rahul": 85,
    "Sneha": 92,
    "Kiran": 78,
    "Meera": 95,
    "Arun": 88
}
print("Initial student_marks:", student_marks)

# b. Access and print the mark of a specific student, of your choice[span_20](start_span)[span_20](end_span)
print("Mark of Sneha:", student_marks["Sneha"])

# c. Add a new student "Janani" with a mark of 80 to the student_marks dictionary[span_21](start_span)[span_21](end_span)
student_marks["Janani"] = 80
print("After adding Janani:", student_marks)

# d. Update the mark of any one older student to 82[span_22](start_span)[span_22](end_span)
student_marks["Kiran"] = 82
print("After updating Kiran's mark to 82:", student_marks)


# e. Use the keys(), values(), and items() methods to print all keys, values, and key-value pairs[span_1](start_span)[span_1](end_span)
print("Keys:", student_marks.keys())
print("Values:", student_marks.values())
print("Items (Key-Value pairs):", student_marks.items())
print("-" * 30)

# a. Create a set called my_set with the given values[span_3](start_span)[span_3](end_span)
my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}
print("my_set:", my_set)

"""
Explanation for (a): 
Sets do not allow duplicate values. Therefore, even though the characters 'a' and 'i' are provided multiple times in the input, they will only appear once in the output. The set automatically removes the duplicates.
"""

# b. Attempt to change the value of my_set[4] = 's[span_4](start_span)'[span_4](end_span)
# my_set[4] = 's'  # Uncommenting this line will cause an error

"""
Explanation for (b):
If you run my_set[4] = 's', it will throw a "TypeError: 'set' object does not support item assignment". This happens because sets are unordered collections and do not support indexing. You cannot access or modify elements using an index position like you do with lists.
"""

# c. Create two sets[span_5](start_span)[span_5](end_span)
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

# d. Compute and print the union and intersection of set1 and set2[span_6](start_span)[span_6](end_span)
print("Union of set1 and set2:", set1.union(set2))
print("Intersection of set1 and set2:", set1.intersection(set2))
print("-" * 30)


# Performance Category Program[span_8](start_span)[span_8](end_span)

# 1. Prompt user for Input. Score range should be from 0 to 10 (both inclusive)[span_9](start_span)[span_9](end_span)
score = float(input("Enter your score (0 to 10): "))

# 2, 3 & 4. Find the performance category, print it, and add a custom prompt[span_10](start_span)[span_10](end_span)
if score > 7 and score <= 10:
    print("Above Average: Excellent work! Keep it up.")
elif score >= 4 and score <= 7:
    print("Average: Good effort! Keep practicing, there's room for improvement.")
elif score >= 0 and score < 4:
    print("Below Average: Need to improve your performance, consistent practice will lead to better results.")
else:
    print("Invalid Score! Please enter a value between 0 and 10.")