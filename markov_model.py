from markov_python.cc_markov import MarkovChain

mc = MarkovChain()
mc.add_file("training_data/artist_10.txt")


print mc.generate_text(20)