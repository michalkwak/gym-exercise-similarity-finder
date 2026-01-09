# Gym Exercise Similarity Finder (Building AI)

## Summary

Project built entirely by me. The projects gives recommendations on gym exercises based on the similarity to the exercise given by the user. 
Recommendations movement patterns, muscle groups, and equipment used. It can help users discover alternative exercises based on their preferenecs. 


## Background

Choosing suitable alternative exercises can be difficult, especially for beginners or when equipment is limited.
Many fitness apps provide recommendations without explaining why, which can reduce trust and understanding.
My personal motivation comes from an interest in bodybuilding and fitness, where understanding why exercises are similar is just as important as the recommendation itself.

This project addresses:
- lack of explainable exercise recommendations
- difficulty finding substitutes for specific exercises
- limited personalization in workout planning

## How is it used?

The program runs in a simple command-line interface. The user enters the name of an exercise, and the system returns the most similar exercises with explanations based on predefined criteria such as muscle groups, push/pull movement, and equipment.

```
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

```

This tool can be useful:
- when planning workouts
- when replacing exercises due to injury or equipment availability
- for learning how different exercises relate to each other

## Data sources and AI methods

The exercise data is manually created and represented as feature vectors using my knowledge about resistance training. Each exercise is encoded using binary attributes such as upper/lower body, muscle targets, and movement type.

```
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
```

## Challenges

This project does not:
- adapt to an individual user 
- learn from user feedback
- guarantee optimal exercise replacement based on injury

## What next?

Possible future improvements include:
- adding weighting to features (e.g. muscle groups more important than equipment)
- expanding the exercise database
- adding a simple graphical interface
- personalization based on user goals, injury rehabilitation, available equipment or experience level

As I'm a computer science student at the University of Helsinki, I would love to continue working on this project and combine my love for fitness and software development!

# Acknowledgments
Project inspired by the Building AI course. All code and data made by the author for educational purposes.
