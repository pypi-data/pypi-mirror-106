import math
from decimal import Decimal
from decimal import getcontext
import pint
import numpy as np
import pandas as pd
import operator
from pprint import pprint
units = pint.UnitRegistry()

# https://colab.research.google.com/drive/1embO7TP1xdfOuG4saScgP4hbWwa1st30#scrollTo=VOuCZ1Z5yi-9
def divide( numerator , denominator , precision ):
    return Decimal( numerator / denominator ).quantize( Decimal( f'0.{"1".zfill( precision )}' ) )

def test():
	print( divide( float( 3.3 ) , 5 , 7 ) )