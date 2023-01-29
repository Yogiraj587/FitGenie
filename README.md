# FitGenie

## Inspiration

Fitness is one of the important aspect of our life. Some people cannot go to gym for doing exercises due to many reasons such as no cost affordability, personal reasons, hectic schedule etc. It would be helpful for them if they can do the workouts in home. So, this was our inspiration to build an AI based gym assister.

## About it 

FitGenie is an AI based gym assister which assists people who prefer home workouts. Insttead of going to gym, this gym assister helps people to do exercises correctly and also counts the number of sets and reps. Users can create their own at-home regimen by choosing from a library of exercises. They can then use their webcams to check the quality of their form using the app's feedback.This can be a great help to people who cannot afford to go to gym or do not go due to some personal reasons.

## How we built it

We have built this application using OpenCV, Mediapipe for capturing and visualizing the exercises of the user. This python web application was hosted using streamlit and deployed in Heroku. 

## Challenges we ran into

1. Being one camera connected at a time prevented us from being able to have as many exercises we wnated to do.
2. Giving the exact angles for the exercises for correct detection was not easy.
3. Testing our model required open and spatial environment and accurate tracking of movements was difficult.

## Accomplishments we are proud of 

1. One accomplishment was that we have learnt how to use streamlit for hosting our python web applications and deployment in Heroku.
2. We have learnt how to use Opencv and mediapipe for human pose tracking.

 ## What we Learned
 
We have learnt about opencv, mediapipe tools for computer vision. We have learnt about streamlit and how to host python applications in streamlit. 

 ## What's next for FitGenie
 
One of the improvements is that we could add a feature such that users can be able to add their wn type of exercises, so that they will not be limited to the exercises that we have provided.

One camera being attached at a time was one of the main problems we ran across because it limited the number of workouts we could perform. This is crucial and an enhancement because it allows us to add new workouts and let the user choose how to train without having to adjust the camera.
