class data_bank:

    def __init__(self, desired_length, characters):
        self.length = desired_length

        # all ascii characters in a string and split to an array
        ascii_chars_raw = '!	"	#	$	%	&	(	)	*	+	,	-	.	/	0	1	2	3	4	5	6	7	8	9	:	;	<	=	>	?	@	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z	[	\	]	^	_	`	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z	{	|	}	~'
        self.chars = ascii_chars_raw.split('\t')
        if int(characters) == 2:
            self.chars = self.chars[63:89]
        elif int(characters) == 3:
            self.chars = ['a','b','c','d']

    def get_char_list(self):
        return self.chars

    def calculate_combinations(self):
        # calculates the amount of permutations for strings of given length
        return int(self.length) ** int(len(self.chars))

    def calculate_size_approximation(self):
        # calculates the appromximate size of strings about to be created
        single_char_size_approx = len(self.chars[0].encode('utf-8'))
        x = int(self.length) * int(single_char_size_approx)
        return self.calculate_combinations() * x

    def get_char(self, position_in_char_array):
        return self.chars[position_in_char_array]

    def get_combinations(self, length):
        last_element = self.chars[-1] # get the last element of the list
        print('last last_element ' + last_element)
        word_as_list = [self.get_char(0)] * int(length) # creates an array that has the firs character of the list as a value of all elements

        def check_if_last(char, current_position): # give current character and the index of the element in the generated list
            position = current_position
            if char == last_element: # if the inspected character is the last on the list of charaters
                word_as_list[current_position] = self.get_char(0) # set the current character to the first character of the list for re-loop

                # next assign the value for next element in the word
                # this is done by getting the index of the next element of the list in the character pool, increasing the index by one and then
                # calling the class methdo 'get_char()'
                try:
                    word_as_list[current_position +1] = self.get_char(self.chars.index(word_as_list[current_position +1]) + 1) # jesus fuck my eyes
                    print(word_as_list)
                except Exception as e:
                    print("Error: " + str(e))

            if position + 1 > len(word_as_list) - 1:
                return " "
            else :
                check_if_last(word_as_list[current_position +1], int(position) + 1) # what the fuck  what is recursion?

        def check_if_all_last(word_as_list):
            x = 0
            for char in word_as_list:
                if char == last_element:
                    x += 1
            if x == len(word_as_list):
                return True
            else:
                return False
        x = 0
        while x < 50: # this is the actual condition: check_if_all_last(word_as_list) == False:
            for char in self.chars:
                word_as_list[0] = char
                check_if_last(word_as_list[0], 0)
            x += 1
