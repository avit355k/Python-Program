from collections import defaultdict

students = {
    0: "David", 1: "Rik", 2: "Sam", 3: "Prakash", 4: "Ishika",
    5: "Medha", 6: "Jim", 7: "Ankit", 8: "Pam", 9: "Diti"
}

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1, "Postgres"),
    (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"), (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"), (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"), (7, "neural-networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"), (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def common_interests(name):
    name_id = None
    for student_id, student in students.items():
        if student == name:
            name_id = student_id
            break
    if name_id is None:
        return None

    interests_dict = defaultdict(list)
    for student_id, interest in interests:
        interests_dict[student_id].append(interest)

    name_interests = set(interests_dict[name_id])
    similar_interests = []

    for student_id, student_interests in interests_dict.items():
        if student_id != name_id:
            common = set(student_interests) & name_interests
            if len(common) > 0:
                similar_interests.append((students[student_id], list(common)))
    return similar_interests

name_to_check = "David"
similar_interests = common_interests(name_to_check)
if similar_interests is None:
    print(f"No student found with the name {name_to_check}")
else:
    print(f"Persons with similar interests to {name_to_check}:")
    for person, interests in similar_interests:
        print(f"{person}: {interests}")
