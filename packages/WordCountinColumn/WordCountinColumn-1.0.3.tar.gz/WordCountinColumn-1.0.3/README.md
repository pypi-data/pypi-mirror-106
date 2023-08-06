[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![PyPI version](https://badge.fury.io/py/WordCountinColumn.svg)](https://badge.fury.io/py/WordCountinColumn)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

Count total number of appearance of words in a given pandas series'

- **Examples:** https://github.com/HindyDS/Word-Count-in-Column/blob/main/word_count_in_col%20example.ipynb
- **Email:** hindy888@hotmail.com
- **Source code:** https://github.com/HindyDS/Word-Count-in-Column/blob/main/WordCountinColumn/WordCountinColumn/__init__.py
- **Bug reports:** https://github.com/HindyDS/Word-Count-in-Column/issues

The fit method only requires a single argument to run:

- col: a pandas series
this will return a python dictionary that contains all the words or string of the given pandas series as keys, and the word counts of those words as values.

The count_frequency method only requires a single argument to run:

- row: a cell in pandas dataframe
this returns a python dictionary that contains all the words or string of the given cell of a pandas series as keys, and the word counts of those words as values.


The dict_op method requires three arguments to run:

- op(str): operation ('+', '-', '*', '/', '**', '//')
- dict1(dictionary): python dictionary
- dict2(dictionary): python dictionary


If you have any ideas for this packge please don't hesitate to bring forward!