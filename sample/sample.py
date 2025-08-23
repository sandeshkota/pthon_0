users = [ "alice", "bob", "charlie", "dean", "ellie: ]

for user in users:
  if user.startsWith("e"):
    users.remove(user)

print(users)
