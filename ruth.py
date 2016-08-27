import sys

questions = [
  ('I dont feel particularly pleased with the way I am.', False),
  ('I am intensely interested in other people.', True),
  ('I feel that life is very rewarding.', True),
  ('I have very warm feelings towards almost everyone.', True),
  ('I rarely wake up feeling rested.', False),
  ('Im not particularly optimistic about the future.', False),
  ('I find most things amusing.', True),
  ('I am always committed and involved.', True),
  ('Life is good.', True),
  ('I dont think that the world is a good place.', False),
  ('I laugh a lot.', True),
  ('I am well satisfied with everything in my life.', True),
  ('I dont think I look attractive.', False),
  ('Theres a gap between what I would like to do and what I have done.', False),
  ('I am very happy.', True),
  ('I find beauty in some things.', True),
  ('I always have a cheerful effect on others.', True),
  ('I can find time for everything I want to do.', True),
  ('I feel that Im not especially in control of my life.', False), 
  ('I feel able to take anything on.', True),
  ('I feel fully mentally alert. ', True),
  ('I often experience joy and elation. ', True),
  ('I dont find it easy to make decisions.', False),  
  ('I dont have a particular sense of meaning and purpose in my life.', False), 
  ('I feel I have a great deal of energy. ', True),
  ('I usually have a positive influence on events. ', True),
  ('I dont have fun with other people.', False), 
  ('I dont feel particularly healthy.', False), 
  ('I dont have particularly happy memories of the past.', False), 
]

def is_acceptable_answer(ans):
	acceptable_answers = ['1', '2', '3', '4', '5', '6', 'quit']
	return ans in acceptable_answers


# %s == interpret as string <-- default to this
# %d == interpret as integer
# %f == interpret as decimal
def run_survey():
	score = 0
	index = 0

  # Ask questions
	for question, inverse_score in questions:
		# Print question to screen
		print 'Rate 1 (Strongly Disagree) - 6 (Strongly Agree) or "quit" to exit'
		print '(%d/%d): %s' % (index + 1, len(questions), question)

		answer = ''
		while True: 
			# Wait for user to input answer
			answer = sys.stdin.readline().strip()
			if not is_acceptable_answer(answer):
				print 'please enter a value between 1 and 6'
			else:
				break

    # User asked to exit early
		if answer == 'quit':
			print 'Goodbyes'
			sys.exit(0)

		# Print user's answer to screen
		print 'you entered: %s\n' % answer 

    # Don't forget to increment index
		index += 1

    # Compute score
		numerical_answer = int(answer)
		if inverse_score:
			score += 6 - (numerical_answer - 1)
		else:
			score += numerical_answer

	return float(score) / len(questions) 



# boiler plate, never changes
if __name__ == "__main__":
	print 'Hello, what is your name?'
	user = sys.stdin.readline().strip()

	score = run_survey()
	print 'Your score today is %.2f' % score