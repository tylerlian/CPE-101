row_len = 10
def main():
	puzzle = input("Enter puzzle: ")
	puzzle = puzzle[:-1] if len(puzzle) > 100 else puzzle
	words = input ("Put the words you want to find here: ")
	print('\n')
	display_puzzle(puzzle)
	print('\n')
	word, words = extract_words(words)
	while word:
		print(find_word(puzzle, word))
		word, words = extract_words(words)
	print (find_word(puzzle, words))

def extract_words(words):
	index = words.find(" ")
	if index == -1:
		return '', words
	return words[:index], words[index+1:] 

def display_puzzle (puzzle):
	position = 0
	for i in range(0, 10):
		new_str = puzzle [position:position+10]
		print (new_str)
		position += 10
def search_right(puzzle, word):
	index = puzzle.find(word)
	if index == -1:
		return ''
	row = index // row_len
	column = index % row_len 
	return "(FORWARD) row: %s column: %s"\
			% (row,column)
def search_left(puzzle,word):
	puzzle = reverse_string(puzzle)
	index = puzzle.find(word)
	if index == -1:
		return ''
	index = len(puzzle) - 1 -index
	row = index // row_len
	column = index % row_len 
	return "(BACKWARD) row: %s column: %s"\
			% (row,column)
def search_down(puzzle, word):
	puzzle = transpose_string(puzzle, row_len)
	index = puzzle.find(word) 
	if index == -1:
		return ''
	row = index // row_len
	column = index % row_len 
	return "(DOWN) row: %s column: %s"\
			% (column,row)
def search_up(puzzle, word):
	puzzle = transpose_string(puzzle, row_len)
	puzzle = reverse_string(puzzle)
	index = puzzle.find(word)
	if index == -1:
		return ''
	index = len(puzzle) - 1 - index 
	row = index // row_len
	column = index % row_len 
	return "(UP) row: %s column: %s"\
			% (column,row)

def find_word (puzzle, word):
	right = search_right(puzzle,word)
	left = search_left(puzzle,word)
	down = search_down(puzzle,word)
	up = search_up(puzzle,word)
	if right:
		return word + right
	if left:
		return word + left
	if up:
		return word + up
	if down:
		return word + down
	return word + " Word Not Found"

def reverse_string(string):
	my_str = ''
	length = len(string)
	for i in range(length):
		my_str += string[length - 1 -i]
	return my_str

def transpose_string(puzzle, row_len):
	my_str = ''
	t_puzzle = ''
	p = 0
	for i in range(row_len):
		for i in range(row_len):
			my_str += puzzle[p]
			p += 10
		t_puzzle += my_str
		p = p - 99
		my_str = ''
	return t_puzzle


if __name__ == '__main__':
	main()

	