class data_bank:

    def __init__(self, desired_length, characters):
        self.length = desired_length

        # all ascii characters in a string and split to an array
        ascii_chars_raw = '!	"	#	$	%	&	(	)	*	+	,	-	.	/	0	1	2	3	4	5	6	7	8	9	:	;	<	=	>	?	@	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z	[	\	]	^	_	`	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z	{	|	}	~'
        self.chars = ascii_chars_raw.split('\t')
        if int(characters) == 2:
            self.chars = self.chars[63:89]

    def get_char_list(self):
        return self.chars

    def calculate_permutations(self):
        # calculates the amount of permutations for strings of given length
        return int(self.length) * int(len(self.chars))

    def calculate_size_approximation(self):
        # calculates the appromximate size of strings about to be created
        single_char_size_approx = len(self.chars[0].encode('utf-8'))
        x = int(self.length) * int(single_char_size_approx)
        return self.calculate_permutations() * x

    def get_char(self, position_in_char_array):
        return self.chars[position_in_char_array]
