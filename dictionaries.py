# dictionaries
# Create a dictionary with three key-value pairs representing a student's information:
#  name, age, and grade. Print each key-value pair on a new line.
students_info = {
    "Name": "Myrah",
    "Age": 20,
    "Grade": "Cohort 3"
}
for keys, value  in students_info.items():
  print(keys + ':', value)

# Write a function that takes a dictionary of people's names and their ages,
#  {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older.
def adult_names(people):
    return[ n for n, age in people.items() if age >= 21]
people = {
    "Alice": 24,
    "Bob": 19,
    "Charlie": 30}
adults = adult_names(people)
print(adults)
adult_names(people)
        
#Given a dictionary representing items in a store with their prices, 
#{'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that
#  takes a list of items bought, ['apple', 'orange', 'banana', 'banana'],
#  and calculates the total cost.
def cost_of_items():
    store_dict = {   "apple": 0.5,
        "banana": 0.3,
        "orange": 0.7
    }
    items_bought = {"apple", "orange", "banana","banana" }
    total_cost = 0
    for items in items_bought:
        total_cost += store_dict[items]
        print("The total cost of items is: ", total_cost)
cost_of_items()
   
#Write a program that counts the occurrences of each word in a given sentence.
#  Example: for the sentence "hello world hello," the output should be
#  {'hello': 2, 'world': 1}.
def word_occurence():
    sentence = "hello world hello"
    words = sentence.split()
    occurences = {}
    for word in words:
        if word in occurences:
            occurences[word] += 1
        else:
            occurences[word] = 1
    print(occurences)
word_occurence()   
