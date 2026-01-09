import numpy as np

'''exercise vector criteria: 
[isUpperBody, targetsChest, targetsBack, targetsArms, targetsLegs,
isCompund, withBarbell, isPush, isPull]'''

exercises = {
    "bench_press":            [1, 1, 0, 1, 0, 1, 1, 1, 0],
    "incline_bench_press":    [1, 1, 0, 1, 0, 1, 1, 1, 0],
    "dumbbell_bench_press":   [1, 1, 0, 1, 0, 1, 0, 1, 0],
    "push_up":                [1, 1, 0, 1, 0, 1, 0, 1, 0],

    "overhead_press":         [1, 0, 0, 1, 0, 1, 1, 1, 0],
    "dumbbell_shoulder_press":[1, 0, 0, 1, 0, 1, 0, 1, 0],
    "lateral_raise":          [1, 0, 0, 1, 0, 0, 0, 1, 0],

    "pull_up":                [1, 0, 1, 1, 0, 1, 0, 0, 1],
    "lat_pulldown":           [1, 0, 1, 1, 0, 1, 0, 0, 1],
    "barbell_row":            [1, 0, 1, 1, 0, 1, 1, 0, 1],
    "seated_cable_row":       [1, 0, 1, 1, 0, 1, 0, 0, 1],

    "bicep_curl":             [1, 0, 0, 1, 0, 0, 0, 0, 1],
    "barbell_curl":           [1, 0, 0, 1, 0, 0, 1, 0, 1],
    "tricep_pushdown":        [1, 0, 0, 1, 0, 0, 0, 1, 0],
    "skull_crusher":          [1, 0, 0, 1, 0, 0, 1, 1, 0],

    "squat":                  [0, 0, 0, 0, 1, 1, 1, 1, 0],
    "front_squat":            [0, 0, 0, 0, 1, 1, 1, 1, 0],
    "leg_press":              [0, 0, 0, 0, 1, 1, 0, 1, 0],
    "lunges":                 [0, 0, 0, 0, 1, 1, 0, 1, 0],

    "deadlift":               [0, 0, 1, 1, 1, 1, 1, 0, 1],
    "romanian_deadlift":      [0, 0, 1, 0, 1, 1, 1, 0, 1],
    "hip_thrust":             [0, 0, 0, 0, 1, 1, 1, 1, 0],

    "calf_raise":             [0, 0, 0, 0, 1, 0, 0, 1, 0],
}

'''Compute the euclidian distance'''
def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)

'''Find the most similar exercise using the distance function'''
def nearest(x_train, x_test):
    nearest_index = -1
    min_distance = np.inf

    for i, vector in enumerate(x_train):
        if vector == x_test:
            continue

        distance = dist(vector, x_test)
        if distance < min_distance:
            min_distance = distance
            nearest_index = i

    return nearest_index

'''Return the top k most similar exercises for broader recommendation'''
def top_k_similar(x_train, x_test, k=3):
    distances = []

    for i, vector in enumerate(x_train):
        if vector == x_test:
            continue
        distances.append((i, dist(vector, x_test)))

    distances.sort(key=lambda x: x[1])
    return distances[:k]

criteria = [
    "Upper body",
    "Targets chest",
    "Targets back",
    "Targets arms",
    "Targets legs",
    "Compound movement",
    "Uses barbell",
    "Push movement",
    "Pull movement"
]

'''Add explanations for the recommendation'''
def explain_similarity(a, b):
    reasons = []
    for i in range(len(a)):
        if a[i] == 1 and b[i] == 1:
            reasons.append(criteria[i])
    return reasons

exercise_names = list(exercises.keys())
x_train = list(exercises.values())

while True:
    query = input("\nType in an exercise to find similar exercises. Type \"exit\" to quit. Type \"1\" for all available exercises. ").lower()

    if query in ("exit"):
        print("Goodbye!")
        break

    if query == "1":
        print("Available:", ", ".join(exercise_names))
        continue

    if query not in exercises:
        print("Unknown exercise.")
        continue
    

    x_test = exercises[query]

    results = top_k_similar(x_train, x_test, k=3)

    print(f"\nExercises similar to {query}:")
    for idx, dist_val in results:
        name = exercise_names[idx]
        print(f"- {name}")

        reasons = explain_similarity(x_test, exercises[name])

        print("  Similar because:", ", ".join(reasons))
