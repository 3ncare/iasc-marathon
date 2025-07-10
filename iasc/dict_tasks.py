contacts = {
    "Anna": "093-123-45-67",
    "Ivan": "050-888-99-00",
    "Olha": "097-777-33-22"
}

contacts["Taras"] = "063-000-11-22"

contacts.pop("Ivan", None)

print("імена:", list(contacts.keys()))  

print("номери:", list(contacts.values()))

print("Katya є у книзі?", "Katya" in contacts)


grades = {
    "math": 88,
    "physics": 75,
    "english": 93,
    "history": 59
}

subjects = list(grades.keys())
scores = list(grades.values())

max_index = 0
for i in range(1, len(scores)):
    if scores[i] > scores[max_index]:
        max_index = i
top_subject = subjects[max_index]

average = sum(scores) / len(scores)

high_scores = []
for i in range(len(scores)):
    if scores[i] > 80:
        high_scores.append(subjects[i])



transactions = [
    ("Anna", 200),
    ("Ivan", -50),
    ("Anna", 100),
    ("Olha", 500),
    ("Ivan", 150),
    ("Olha", -100),
]

balances = {}
for name, amount in transactions:
    if name in balances:
        balances[name] += amount
    else:
        balances[name] = amount

max_balance_client = max(balances, key=balances.get)

negative_balances = [name for name, balance in balances.items() if balance < 0]

print("Словник балансів:", balances)
print("Клієнт з найбільшим балансом:", max_balance_client)
print("Клієнти з від'ємним балансом:", negative_balances)


text = "hello world hello again hello world test world"

word_count = {}

for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)


import json

student = {
    "name": "Anna",
    "age": 20,
    "courses": ["math", "physics", "english"]
}

student_json = json.dumps(student, ensure_ascii=False)
print("json :")
print(student_json)

student_dict = json.loads(student_json)

student_dict["courses"].append("history")

print("\n оновлений словник:")
print(student_dict)