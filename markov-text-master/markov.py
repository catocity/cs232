from db import Db
from gen import Generator
from parse import Parser
from sql import Sql
from rnd import Rnd
import sys
import sqlite3
import codecs
# import os # added by Catherine Chen

SENTENCE_SEPARATOR = '.'
WORD_SEPARATOR = ' '

if __name__ == '__main__':
	args = sys.argv
	usage = 'Usage: %s (parse <name> <depth> <path to txt file>|gen <name> <count>)' % (args[0], )

	if (len(args) < 3):
		raise ValueError(usage)

	mode  = args[1]
	name  = args[2]
	
	if mode == 'parse':
		if (len(args) != 5):
			raise ValueError(usage)
		
		depth = int(args[3])
		file_name = args[4]
		
		db = Db(sqlite3.connect(name + '.db'), Sql())
		db.setup(depth)
		
		txt = codecs.open(file_name, 'r', 'utf-8').read()
		Parser(name, db, SENTENCE_SEPARATOR, WORD_SEPARATOR).parse(txt)
	
	elif mode == 'gen':
		print name
		sample_count = int(args[4]) # added by Catherine Chen
		for i in range(0,sample_count): # added by Catherine Chen
			file = open(name + str(i) + ".txt", "w") # added by Catherine Chen
			count = int(args[3])
			db = Db(sqlite3.connect(name + '.db'), Sql())
			generator = Generator(name, db, Rnd())
			for i in range(0, count):
				# print(generator.generate(WORD_SEPARATOR))
				file.write(generator.generate(WORD_SEPARATOR)) # added by Catherine Chen
			file.close()
	
	else:
		raise ValueError(usage)
