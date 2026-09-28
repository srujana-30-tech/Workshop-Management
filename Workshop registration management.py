registrations = [
    ("Anish", "Python Workshop", "Morning"),
    ("Rahul", "AI Workshop", "Evening"),
    ("Priya", "Python Workshop", "Morning"),
    ("Anish", "Python Workshop", "Morning"),
    ("Kiran", "Cyber Security", "Evening"),
    ("Rahul", "AI Workshop", "Evening"),
    ("Sneha", "Python Workshop", "Evening"),
]

# To remove duplicate registrations
unique = list(set(registrations))

print("Unique Registrations:")

for i in unique:
    print(i)

# All unique participants
participants = set()

for i in unique:
    participants.add(i[0])

print("\nUnique Participants:")

for p in participants:
    print(p)

# Print all unique workshops
workshops = set()

for i in unique:
    workshops.add(i[1])

print("\nUnique Workshops:")

for w in workshops:
    print(w)

# Count registrations for each workshop
print("\nRegistrations for each Workshop:")

count = {}

for i in unique:
    workshop = i[1]

    if workshop in count:
        count[workshop] += 1
    else:
        count[workshop] = 1

for w in count:
    print(w, ":", count[w])

# Count participants in Morning and Evening sessions
morning = 0
evening = 0

for i in unique:
    if i[2] == "Morning":
        morning += 1
    else:
        evening += 1

print("\nMorning Participants:", morning)
print("Evening Participants:", evening)

# Find workshop with highest registrations
max_count = 0
max_workshop = ""

for w in count:
    if count[w] > max_count:
        max_count = count[w]
        max_workshop = w

print("\nWorkshop with Highest Registrations:", max_workshop)

# Display participants registered for Python Workshop
print("\nParticipants in Python Workshop:")

for i in unique:
    if i[1] == "Python Workshop":
        print(i[0])