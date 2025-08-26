
## List comprehension: 



## Corrected code to remove users whose names contain the letter 'e'
users = [ "alice", "bob", "charlie", "dean", "emma", "ellie" ]

# doesn't work as we are modifying the list while iterating over it
for user in users:
  if user.startswith("e"):
    users.remove(user)

print(users)

# solution 1: iterate over a copy of the list
filtered_users = []
for user in users:
    if not user.startswith("e"):
        filtered_users.append(user)

print(filtered_users)

# solution 2: use list comprehension
users_filtered = [user for user in users if not user.startswith("e")]

print(users_filtered)
