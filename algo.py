"""
	Algorithms for ad-hoc text analysis.

	This module provides 2 main classes for text analysis :
	- Fragment
	- Analyzer

	[ The Fragment class ] is used to describe and anotate short fragment
	of text. It gives a way of abstraction over words or short sentences
	and their meaning.

	[ The Analyzer class ] uses the Fragment class to process a long text,
	estimate the general meaning of it and eventually compare a text to
	a given context.
"""


class Fragment:
	"""
		A class to describe and anotate short fragment of text (words).
	"""

	# == TYPES FOR FRAGMENTS ==
	_type_0 = "TYPE_0"	# type for fragment to ignore
	_type_1 = "TYPE_1" 	# type for emojis
	_type_2 = "TYPE_2" 	# type for other fragments
	# ... more to implement
	# =========================

	
	def __init__(self, txt : str):
		"""
			Constructor for class Fragment.

			ARGUMENTS:
			txt -- the text of the fragment
		"""

		# text of the fragment
		self.txt 	= txt
		# type of the fragment
		self.type 	= self._get_type(txt)

	
	def _is_emoji(self, txt : str):
		return (
				txt == "XD"
			or 	txt == "xD"
			or 	txt == "Xd"
			or 	txt == ";)"
			or 	txt == ":)"
			or 	txt == ":("
			or 	txt == ";("
			or 	txt == "X("
			or 	txt == "X)"
			or 	txt == "x)"
			or 	txt == "x("
			or 	txt == "^^"
			)


	def _get_type(self, txt : str):
		"""
			Get the type of text fragment.
		"""

		# TODOS
		# -> better type determination

		if self._is_emoji(txt):
			return Fragment._type_1
		elif len(txt) <= 2:
			return Fragment._type_0
		else:
			return Fragment._type_2

		#elif self._is_emoji(txt):
		#	return Fragment._type_3
		#elif self._is_emoji(txt):
		#	return Fragment._type_3


	
	def __str__(self):
		s = "txt  : {} \ntype : {}".format(self.txt, self.type)
		return s


class Analyzer:
	"""
		A class to perform text analysis.
	"""

	def __init__(self, txt):
		"""
			Constructor of Analyzer class.
			
			ARGUMENTS:
			txt -- the string to analyze
		"""

		self.txt = txt

	
	def _is_blank(self, char : str):
		"""
			Predicate to detect if a character is blank.
		""" 
		
		return (
				char == ' '
			or	char == '\n'
			or 	char == '\r'
			or 	char == '\t'
			)

	
	def explode(self):
		"""
			Explode the text in several fragments
			and return an iterator on them.
			See class Fragment for more details.
		"""
		
		char_buff = ""

		for char in self.txt:
			if not self._is_blank(char):
				# skip blank character
				char_buff += char
			else:
				# return an iterator on fragments
				yield Fragment(char_buff)
				char_buff = ""

		# end of the text, return last fragment
		yield Fragment(char_buff)
