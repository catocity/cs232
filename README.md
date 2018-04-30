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

This is a tool that can be used to identify common words between the input text and the output file (see common-words.py). What is more useful however, is the ngram-finder.py, which finds sequences of words (up to length n) that the texts have in common.
https://github.com/alimony/text-comparison-tools

## Results

### Lyric Generation
Below are some generated lyrics.
(Something to note about the RNN we used is that the user runs the model with a given letter. In our case, the given letter was always "T", which is why all of the generated lyrics start with "the".)

* Example 1:
the heat goes on
i know that the heat goes on
i know that the heat goes on
you play tight, you're nobody's fool
you're not cold, but i know that you're cool
look at you, i know the heat goes on"
"written by babyface, keith andes (1996)
performed by az yet
this was the place of our first date
it was a place we love
that was the place we laughed
where we had so much fun
there was the place i met her
that's where we fell in love
and it was the place where she broke my heart
so how do we tell this story

* Example 2:
the doorway
standing in the doorway
standing in the doorway
..."
"this union with creation is a brilliant coronet
what i cannot gain by knowledge, i infect, as i posses
put into perspective as i walk up the facade
instead of sinking, it's got me thinking
how could i be wrong when i am right?
i'll never know
we learn to sacrifice, we learn to take a life
we take and we don't give, live how we want to live
and no one wants to lie but we all have to lie
yeah, no one wants to lie, relax, then die
we hea

* Example 3:
the business, stand as a wicn calious ard the's a digh and suckes further away from the truth
you can throw the set in the sky
but the eternal majestic mount zion you can't deny
a gat, a clip, a hollow-tip with your name on it
loving to trip but one day you'll get caught up and slip
so cheap a death but my brother so precious is life
speaking the language of fratricidal sights
you do like ""cain"" did ""abel"" you love to watch your brother's blood
flow fool tell me no, spirin so cold! denial" "ap l

* Example 4:
the truth
you can throwet
and the sky to be the way i am
and what i do
for i have been a lost and lonely
sailor on your sea
run aground by trusting signals
you were sending me
the streets are filled with empty faces
nothing here is new
it's just the same in other places
i have journeyed to
i was the first across the water
the last across the land
i walked out of the silver mine
my pockets full of sand
alone inside my head
alone inside my room
i feel alone inside my head
alone inside my tiny little w
Example 5:
the silver mine
my pockets full of sand
alone inside my head
alone inside my room
i feel alone inside my head
alone inside my tiny little world
alone inside my head
alone inside my room
i feel alone inside my head
alone inside my tiny little world
alone inside my head
alone inside my room
i feel alone inside my head
alone inside my tiny little world
it's not my life in those old pictures
the ones you threw away
for i was always someone else
and always far away
walking in the darkest places
where the

* Example 6: 
the darkest places
where the mission meets
waiting for the ground to open up
beneath my feet
alone inside my head
alone inside my room
i feel alone inside my head
alone inside my tiny little world
alone inside my head
alone inside my room
i feel alone inside my head
alone inside my tiny little world"
"i'm going be a good girl
so everybody loves me
i'm gonna do what they say
let them chose the games that we play
good girl, good girl
gonna be a good girl
good dog, good girl
gonna be a good girl
good g

* Example 7:
the hotel st. bonaventure
besides i do wear a coat in the winter
and eat at beautiful restaurants
leave me alone, leave me alone!
(politics, politics..)
why you think i should wear a motorcycle helmet??
why don't you wear it?! put on some wings like a parrot
let's discuss this contract
why are you hypin up a normal female group with fat cellulite
that sound wack? most of why'all goin out like uncle tom's
like louis armstrong
wearin a tattoo and goin onstage like tracy chapman
i cancelled a big tour 

* Example 8:
the truth
you can throw the set in the sky
but the eternal majestic mount zion you can't deny
a gat, a clip, a hollow-tip with your name on it
loving to trip but one day you'll get caught up and slip
so cheap a death but my brother so precious is life
speaking the language of fratricidal sights
you do like ""cain"" did ""abel"" you love to watch your brother's blood
flow fool tell me no, spirit so cold! denial"r apare see you
standing in the doorway
standing in the doorway
i can see you
standing in 

* Example 9:
the darkest places
where the mission meets
waiting for the ground to open up
beneath my feet
alone inside my head
alone inside my room
i feel alone inside my head
alone inside my tiny little world"
"i'm going be a good girl
so everybody loves me
i'm gonna do what they say
let them chose the games that we play
good girl, good girl
gonna be a good girl
good dog, good girl
gonna be a good girl
all i want is for everyone to love me
all i want is for everyone to love me
i'll get down on my knees
i'll say

* Example 10:
the start
and you're sure, you felt it all along
you know that the heat goes on
you know that the heat goes on
times to decide, times that i've lied
problems will never be solved
which way is wrong, which could be right?
this heat will always go on
you walk tall, got your head in the clouds
you talk soft, but you're thinking aloud
and you know, exactly what you want
you box shy, you're hard to get
you got the face that i can't forget
and i know, i know the heat goes on
i know that the heat goes on

### N-Grams Found when Comparing Original Text with Machine Output: 

  n    length  sentence
---  --------  ------------------------------------------------------------------------------------------------------------------------------------
 26       132  head alone inside my tiny little world it 's not my life in those old pictures the ones you threw away for i was always someone else
 26       131  alone inside my tiny little world it 's not my life in those old pictures the ones you threw away for i was always someone else and

  n    length  sentence
---  --------  --------------------------------------------------------------------------------------------------------------------------------------
 25       130  my head alone inside my tiny little world it 's not my life in those old pictures the ones you threw away for i was always someone
 25       132  inside my tiny little world it 's not my life in those old pictures the ones you threw away for i was always someone else and always
 25       134  little world it 's not my life in those old pictures the ones you threw away for i was always someone else and always far away walking
 25       131  tiny little world it 's not my life in those old pictures the ones you threw away for i was always someone else and always far away
 25       126  tiny little world it 's not my life in those old pictures the ones you threw away for i was always someone else and always far
 25       129  my tiny little world it 's not my life in those old pictures the ones you threw away for i was always someone else and always far

  n    length  sentence
---  --------  ----------------------------------------------------------------------------------------------------------------------------------
 24       129  inside my head alone inside my tiny little world it 's not my life in those old pictures the ones you threw away for i was always
 24       130  world it 's not my life in those old pictures the ones you threw away for i was always someone else and always far away walking in

  n    length  sentence
---  --------  --------------------------------------------------------------------------------------------------------------------------------------------------
 23       128  alone inside my head alone inside my tiny little world it 's not my life in those old pictures the ones you threw away for i was
 23       146  those old pictures the ones you threw away for i was always someone else and always far away walking in the darkest places where the mission meets
 23       129  feel alone inside my head alone inside my tiny little world it 's not my life in those old pictures the ones you threw away for i
 23       129  i feel alone inside my head alone inside my tiny little world it 's not my life in those old pictures the ones you threw away for
 23       128  it 's not my life in those old pictures the ones you threw away for i was always someone else and always far away walking in the
 23       137  not my life in those old pictures the ones you threw away for i was always someone else and always far away walking in the darkest places
 23       139  my life in those old pictures the ones you threw away for i was always someone else and always far away walking in the darkest places where
 23       133  's not my life in those old pictures the ones you threw away for i was always someone else and always far away walking in the darkest
 23       130  room i feel alone inside my head alone inside my tiny little world it 's not my life in those old pictures the ones you threw away

  n    length  sentence
---  --------  -----------------------------------------------------------------------------------------------------------------------------------------------
 22       128  my room i feel alone inside my head alone inside my tiny little world it 's not my life in those old pictures the ones you threw
 22       143  in those old pictures the ones you threw away for i was always someone else and always far away walking in the darkest places where the mission
 22       140  life in those old pictures the ones you threw away for i was always someone else and always far away walking in the darkest places where the

  n    length  sentence
---  --------  ---------------------------------------------------------------------------------------------------------------------------------
 21       129  inside my room i feel alone inside my head alone inside my tiny little world it 's not my life in those old pictures the ones you

  n    length  sentence
---  --------  -----------------------------------------------------------------------------------------------------------------------------------
 20       131  alone inside my room i feel alone inside my head alone inside my tiny little world it 's not my life in those old pictures the ones

  n    length  sentence
---  --------  -----------------------------------------------------------------------------------------------------------------------------------
 19       131  head alone inside my room i feel alone inside my head alone inside my tiny little world it 's not my life in those old pictures the

  n    length  sentence
---  --------  ----------------------------------------------------------------------------------------------------------------------------------
 18       130  my head alone inside my room i feel alone inside my head alone inside my tiny little world it 's not my life in those old pictures

  n    length  sentence
---  --------  --------------------------------------------------------------------------------------------------------------------------------------
 17       134  pockets full of sand alone inside my head alone inside my room i feel alone inside my head alone inside my tiny little world it 's not
 17       128  inside my head alone inside my room i feel alone inside my head alone inside my tiny little world it 's not my life in those old

  n    length  sentence
---  --------  -------------------------------------------------------------------------------------------------------------------------------------------
 16       129  of sand alone inside my head alone inside my room i feel alone inside my head alone inside my tiny little world it 's not my life
 16       115  walked out of the silver mine my pockets full of sand alone inside my head alone inside my room i feel alone inside
 16       132  for the ground to open up beneath my feet alone inside my head alone inside my room i feel alone inside my head alone inside my tiny
 16       133  my pockets full of sand alone inside my head alone inside my room i feel alone inside my head alone inside my tiny little world it 's
 16       129  walked out of the silver mine my pockets full of sand alone inside my head alone inside my room i feel alone inside my head alone
 16       102  walked out of the silver mine my pockets full of sand alone inside my head alone inside my room i feel
 16       139  silver mine my pockets full of sand alone inside my head alone inside my room i feel alone inside my head alone inside my tiny little world
 16       108  walked out of the silver mine my pockets full of sand alone inside my head alone inside my room i feel alone
 16       123  walked out of the silver mine my pockets full of sand alone inside my head alone inside my room i feel alone inside my head
 16       136  walked out of the silver mine my pockets full of sand alone inside my head alone inside my room i feel alone inside my head alone inside
 16       118  walked out of the silver mine my pockets full of sand alone inside my head alone inside my room i feel alone inside my
 16       129  sand alone inside my head alone inside my room i feel alone inside my head alone inside my tiny little world it 's not my life in
 16       137  the silver mine my pockets full of sand alone inside my head alone inside my room i feel alone inside my head alone inside my tiny little
 16       135  mine my pockets full of sand alone inside my head alone inside my room i feel alone inside my head alone inside my tiny little world it
 16       130  alone inside my head alone inside my room i feel alone inside my head alone inside my tiny little world it 's not my life in those
 16       129  full of sand alone inside my head alone inside my room i feel alone inside my head alone inside my tiny little world it 's not my

  n    length  sentence
---  --------  -------------------------------------------------------------------------------------------------------------------------------------
 15       133  of the silver mine my pockets full of sand alone inside my head alone inside my room i feel alone inside my head alone inside my tiny
 15       132  out of the silver mine my pockets full of sand alone inside my head alone inside my room i feel alone inside my head alone inside my

  n    length  sentence
---  --------  ----------------------------------
  6        34  the set in the sky but the eternal
  6        30  set in the sky but the eternal


## Credits
[1] http://www.wildml.com/2015/09/recurrent-neural-networks-tutorial-part-1-introduction-to-rnns/
