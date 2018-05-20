# Comparing Text Generating Models

## Background
This project explores whether algorithms can be creative when learning, based on knowledge from music lyrics. The goal is to compare the performances of two language models: one that uses a Markov Chain and a second that uses a Recurrent Neural Network (RNN). For each model, song lyrics will be generated given a user’s input of genre, year, and/or artist. Performance will be evaluated using two scores. The first will be a comparison of similarities between the training data and the generated songs using a text comparison tool created by Alimony (see link below). The second will be a variation of the Turing test, in which human subjects will be shown lyrics and asked whether or not they think the lyrics were created by a human or a machine. 

## Motivation
We would like to better understand how machines generate text and how to recognize machine-generated text in real life. Furthermore, we are exploring bigger questions, like:
* What makes a song a song?
* What metrics can be used to evaluate the computer-generated lyrics?
* What does it means for something to be creative?
* Are computers demonstrating creativity through the computer-generated lyrics?

## Models and Tools

### Markov Chain

This model was implemented by Rob Dawson. 

https://github.com/codebox/markov-text

### Recurrent Neural Network
We decided to use a recurrent neural network created by Spiglerg to generate the lyrics. We chose this model because it is a simpler version of typical text generating neural networks, using Tensorflow. With the given model, we were able to adjust variables to control run time (and therefore, accuracy). Note: this is a character based model. 

We chose to use a recurrent neural network because RNNs can “make use of sequential information” [1] and have been used to achieve great success in various natural language processing tasks. In particular, recurrent neural networks are powerful for this task because they are able to predict the likelihood of the next letter given the previous letter, meaning the output of the trained model would be the sequence of predicted letters.

https://github.com/spiglerg/RNN_Text_Generation_Tensorflow

The following model is a word based model created by hunkim. We wanted to compare the performance of character based and word based models. The model took 3-4 to train on a training set of 5000 songs (filesize approx. 3MB). 
https://github.com/hunkim/word-rnn-tensorflow

### Text Comparison Tool

This is a tool that can be used to identify common words between the input text and the output file (see common-words.py). What is more useful however, is the ngram-finder.py, which finds sequences of words (up to length n) that the texts have in common.
https://github.com/alimony/text-comparison-tools

## Results

### N-Grams Found when Comparing Original Text with Machine Output: 
  
---  --------  ---------------------------------------------------------------------------------------------------------------
 n = 26 
 
head alone inside my tiny little world it 's not my life in those old pictures the ones you threw away for i was always someone else
 
alone inside my tiny little world it 's not my life in those old pictures the ones you threw away for i was always someone else and
 
---  --------  ---------------------------------------------------------------------------------------------------------------
  n = 25 
  
my head alone inside my tiny little world it 's not my life in those old pictures the ones you threw away for i was always someone
 
inside my tiny little world it 's not my life in those old pictures the ones you threw away for i was always someone else and always
 
little world it 's not my life in those old pictures the ones you threw away for i was always someone else and always far away walking
 
tiny little world it 's not my life in those old pictures the ones you threw away for i was always someone else and always far away
 
tiny little world it 's not my life in those old pictures the ones you threw away for i was always someone else and always far
 
my tiny little world it 's not my life in those old pictures the ones you threw away for i was always someone else and always far

---  --------  ---------------------------------------------------------------------------------------------------------------
 n = 24

inside my head alone inside my tiny little world it 's not my life in those old pictures the ones you threw away for i was always
 
world it 's not my life in those old pictures the ones you threw away for i was always someone else and always far away walking in

---  --------  ---------------------------------------------------------------------------------------------------------------
  n = 23

alone inside my head alone inside my tiny little world it 's not my life in those old pictures the ones you threw away for i was
 
those old pictures the ones you threw away for i was always someone else and always far away walking in the darkest places where the mission meets
 
feel alone inside my head alone inside my tiny little world it 's not my life in those old pictures the ones you threw away for i

i feel alone inside my head alone inside my tiny little world it 's not my life in those old pictures the ones you threw away for
 
it 's not my life in those old pictures the ones you threw away for i was always someone else and always far away walking in the
 
not my life in those old pictures the ones you threw away for i was always someone else and always far away walking in the darkest places
 
my life in those old pictures the ones you threw away for i was always someone else and always far away walking in the darkest places where
 
's not my life in those old pictures the ones you threw away for i was always someone else and always far away walking in the darkest
 
room i feel alone inside my head alone inside my tiny little world it 's not my life in those old pictures the ones you threw away

---  --------  ---------------------------------------------------------------------------------------------------------------
  n = 22

my room i feel alone inside my head alone inside my tiny little world it 's not my life in those old pictures the ones you threw
 
in those old pictures the ones you threw away for i was always someone else and always far away walking in the darkest places where the mission
 
life in those old pictures the ones you threw away for i was always someone else and always far away walking in the darkest places where the

---  --------  ---------------------------------------------------------------------------------------------------------------
  n = 21

inside my room i feel alone inside my head alone inside my tiny little world it 's not my life in those old pictures the ones you

---  --------  ---------------------------------------------------------------------------------------------------------------
  n = 20

alone inside my room i feel alone inside my head alone inside my tiny little world it 's not my life in those old pictures the ones


## Credits
[1] http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/
