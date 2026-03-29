
student_info = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science",
    "courses": ["Data Structures", "Algorithms", "Operating Systems"]
}

# Accessing values
print(student_info["name"])  # Output: John Doe
print(student_info["age"])   # Output: 20
print(student_info["major"]) # Output: Computer Science
print(student_info["courses"]) # Output: ['Data Structures', 'Algorithms', 'Operating Systems
print(student_info["courses"][0]) # Output: Data Structures


#list of dictionaries
students = [
    {"name": "Alice", "age": 22, "major": "Mathematics"},
    {"name": "Bob", "age": 21, "major": "Physics"},
    {"name": "Charlie", "age": 23, "major": "Chemistry"}
]

for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")

########################################################

ec2_instances = [
    {
        "id": "i-1234567890abcdef0", 
        "type": "t2.small", 
        "state": "running"
    },
    
    
    {
        "id": "i-0abcdef1234567890",
        "type": "t2.medium",
        "state": "stopped"
    },
    
    
    {
        "id": "i-0abcdef1234567891",
        "type": "t2.large",
        "state": "running"
    }
]

print(ec2_instances[1]["type"]) # Output: t2.medium