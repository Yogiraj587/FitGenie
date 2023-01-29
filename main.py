import json
import Exercises.Biceps
import Exercises.Squats
import Exercises.Crunches
import Exercises.BenchPress

def start(arr):
    for i in arr:
        if i == 'Biceps':
            reps = int(arr['Biceps']['reps'])
            sets = int(arr['Biceps']['sets'])
            Exercises.Biceps.start(sets,reps)
        elif i == 'Squats':
            reps = int(arr['Squats']['reps'])
            sets = int(arr['Squats']['sets'])
            Exercises.Squats.start(sets,reps)
        elif i == 'Crunches':
            reps = int(arr['Crunches']['reps'])
            sets = int(arr['Crunches']['sets'])
            Exercises.Crunches.start(sets, reps)
        elif i == 'Benchpress':
            reps = int(arr['Benchpress']['reps'])
            sets = int(arr['Benchpress']['sets'])
            Exercises.BenchPress.start(sets,reps)