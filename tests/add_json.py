import json

from pydantic_core import to_json

tasks = [
    {
        "id":11,
        "description":"blabla00"
    },
    {
        "id":22,
        "description":"blabla01"
    }
]

# Convert the list of dictionaries to JSON format
json_data = json.dumps(tasks, indent=2)

# Write the JSON content to a file named students.json
with open("tasks.json", "w") as f:
    f.write(json_data)

print("JSON file 'tasks.json' has been created successfully.")