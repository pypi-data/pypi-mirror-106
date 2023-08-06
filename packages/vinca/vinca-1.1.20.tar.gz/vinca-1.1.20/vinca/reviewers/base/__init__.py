# a basic card reviewer making use of cat and readchar
import subprocess
import readchar
import datetime
# we could refactor this into the card class and make
# a function add_grade instead of add_history
today = datetime.date.today() 

grade_dict = {'-': -3,
	      '@': -2,
	      'x': -1,
	      'q': -1,
	      'u': -1,
	      'h': 0,
	      'w': 0,
	      '1': 1,
	      '2': 2,
	      '3': 3,
	      '4': 4,
	      ' ': 3,
	      '\r': 3,
	      '\n': 3}

cont_dict = {'-': 1,
	     '@': 1,
	     'x': 1,
	     'q': 0,
	     'u': -1,
	     'h': -1,
	     'w': 0,
	     '1': 1,
	     '2': 1,
	     '3': 1,
	     '4': 1,
	     ' ': 1,
	     '\r': 1,
	     '\n': 1}

assert cont_dict.keys() == grade_dict.keys()

def review(card,mode):
	# clear screen
	# show front
	# wait for keystroke / check if mode is preview
	# show back
	# call editor(?) / add a single card
	# assign grade (incl. schedule for suspend, bury, deletion)
	# call scheduler
	# return continue value

	# save the screen; tput smcup generates an escape code
	# which tells the terminal to save the screen
	# processes like vim, top, and less use this to recover the terminal at the end

	start = datetime.datetime.now()  # begin card timer

	subprocess.run(['tput','smcup'])
	subprocess.run(['tput','civis'])

	def show_card():
		subprocess.run(['clear'])
		subprocess.run(['tput','civis'])
		subprocess.run(['cat',f'{card.path}/front'])  # view frontside
		if mode == 'review':
			char = readchar.readchar() # later I might allow adding and quitting on the frontside
		subprocess.run(['echo','\n\n']) # dividing space
		subprocess.run(['cat',f'{card.path}/back'])  # view backside
	show_card()

	char = None
	while char not in grade_dict.keys():
		if char in ['e','f','b','*']:
			subprocess.run(['tput','rmcup']) # restore terminal state so that vim does not overwrite smcup
			card.edit(mode=char)
			subprocess.run(['tput','smcup']) 
			show_card()
		char = readchar.readchar()

	grade = grade_dict[char]
	cont = cont_dict[char]

	stop = datetime.datetime.now()  # stop card timer
	elapsed_time = min(120, (stop - start).seconds)
	
	card.add_history(today, elapsed_time, grade)

	# restore terminal
	subprocess.run(['tput','rmcup'])
	subprocess.run(['tput','cvvis'])
	
	return cont
	# -1 means go back to previous card
	# 0 means exit
	# 1 means continue
