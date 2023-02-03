# FitGenie

## inspiration

Fitness is one of the important aspect of our life. Some people cannot go to gym for doing exercises due to many reasons such as no cost affordability, personal reasons, hectic schedule etc. It would be helpful for them if they can do the workouts in home. So, this was our inspiration to build an AI based gym assister.

![Kaia-Personal-Trainer-1024x636](https://user-images.githubusercontent.com/84268500/215325986-379b1ee0-2dfe-409f-a04f-24cfffebda45.jpg)

## About it 

FitGenie is an AI based gym assister which assists people who prefer home workouts. Insttead of going to gym, this gym assister helps people to do exercises correctly and also counts the number of sets and reps. Users can create their own at-home regimen by choosing from a library of exercises. They can then use their webcams to check the quality of their form using the app's feedback.This can be a great help to people who cannot afford to go to gym or do not go due to some personal reasons.

## Demo

### Streamlit website
![Image2](https://user-images.githubusercontent.com/84268500/215326094-8f460f7b-9e5d-45ec-9df4-96547b141bea.jpg)
### Squats
![squats](https://user-images.githubusercontent.com/84268500/215326419-c261dfda-fbdb-4c6e-934d-cef09ba32fd1.jpeg)
### Biceps
![biceps](https://user-images.githubusercontent.com/84268500/215326450-0e16abfc-b788-4cd8-a32d-ff3d16daece1.jpeg)

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

## Requirements
```
pip install opencv-python
pip install mediapipe
pip install streamlit
pip install streamlit_lottie
pip install requests
pip install PIL
pip install st-annotated-text
```

## Command for executing
Clone this repository using ```git clone``` and after entering inside the folder run:
```
python -m streamlit run app.py
```
