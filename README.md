# Comparing Text Generating Models

## Background
This project explores whether algorithms can be creative when learning, based on knowledge from music lyrics. The goal is to use an existing language model to generate song lyrics given a user’s input of genre, year, and/or artist, then evaluate the computer generated lyrics.

The model we chose to use to generate lyrics is a recurrent neural network using Tensorflow, created by Spiglerg (link below). For the evaluation, we used a text comparison tool created by Alimony (link below). 

## Motivation
We would like to better understand how machines generate text and how to recognize machine-generated text in real life. Furthermore, we are exploring bigger questions, like:
* What makes a song a song?
* What metrics can be used to evaluate the computer-generated lyrics?
* What does it means for something to be creative?
* Are computers demonstrating creativity through the computer-generated lyrics?

## Models and Tools

### Recurrent Neural Network
We decided to use a recurrent neural network created by Spiglerg to generate the lyrics. We chose this model because it is a simpler version of typical text generating neural networks, using Tensorflow. With the given model, we were able to adjust variables to control run time (and therefore, accuracy).

We chose to use a recurrent neural network because RNNs can “make use of sequential information” [1] and have been used to achieve great success in various natural language processing tasks. In particular, recurrent neural networks are powerful for this task because they are able to predict the likelihood of the next letter given the previous letter, meaning the output of the trained model would be the sequence of predicted letters.

https://github.com/spiglerg/RNN_Text_Generation_Tensorflow

### Text Comparison Tool
https://github.com/alimony/text-comparison-tools

## Results

### Lyric Generation
Below are some generated lyrics.

## Credits
[1] http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/
