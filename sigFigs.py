
'''
Implementation of significant digits and associated concepts.
'''
 
import math
 
def isNumeric(x):
 
    '''Checks to see if x represents a numeric value by converting
    into unicode and utilizing the isnumeric() method.'''
 
    # first convert the number into a string
    strRep = str(x)
 
    # first make a unicode version so we can ensure we're dealing with
    # something that represents a numeric value:
    uRep = unicode(strRep)
    if ('.' in uRep) and all([x.isnumeric() for x in uRep.split('.')]):
        return True # there's a decimal and everything to the right
                    # and left of it is numeric
    else:
        return uRep.isnumeric()
 
def mostSigDigit(x):
 
    '''Returns the most significant digit in x.'''
 
    assert isNumeric(x), 'x must be numeric!'
 
    # number the digits:
    enumeratedChars = list(enumerate(str(x)))
 
    nonZeroChars = [x for x in enumeratedChars if (x[1] != '0') and (x[1] != '.')]
    return nonZeroChars[0][1]
 
def leastSigDigit(x):
 
    '''Returns the least significant significant digit in x.'''
 
    assert isNumeric(x), 'x must be numeric!'
 
    # number the digits:
    enumeratedChars = list(enumerate(str(x)))
 
    nonZeroChars = [x for x in enumeratedChars if (x[1] != '0') and (x[1] != '.')]
    mostSignificantDigit = nonZeroChars[0]
 
    leastSignificantDigit = None
    if '.' in [x[1] for x in enumeratedChars]:
        leastSignificantDigit = enumeratedChars[-1]
    else:
        leastSignificantDigit = nonZeroChars[-1]
     
    # here we have a pair so just return the value:
    return leastSignificantDigit[1]
 
def numSigDigits(x):
 
    '''Returns the number of significant digits in x.'''
 
    assert isNumeric(x), 'x must be numeric!'
 
    # number the digits:
    enumeratedChars = list(enumerate(str(x)))
 
    nonZeroChars = [x for x in enumeratedChars if (x[1] != '0') and (x[1] != '.')]
    mostSignificantDigit = nonZeroChars[0]
 
    leastSignificantDigit = None
    if '.' in [x[1] for x in enumeratedChars]:
        leastSignificantDigit = enumeratedChars[-1]
    else:
        leastSignificantDigit = nonZeroChars[-1]
 
    enumedSignificantDigits = [x for x in enumeratedChars[mostSignificantDigit[0]:leastSignificantDigit[0] + 1]]
 
    numDigits = len(enumedSignificantDigits)
    if '.' in [x[1] for x in enumeratedChars]:
        numDigits -= 1
     
    return numDigits
 
def round_sigfigs(num, sig_figs):
 
    """Round to specified number of sigfigs.
 
    >>> round_sigfigs(0, sig_figs=4)
    0
    >>> int(round_sigfigs(12345, sig_figs=2))
    12000
    >>> int(round_sigfigs(-12345, sig_figs=2))
    -12000
    >>> int(round_sigfigs(1, sig_figs=2))
    1
    >>> '{0:.3}'.format(round_sigfigs(3.1415, sig_figs=2))
    '3.1'
    >>> '{0:.3}'.format(round_sigfigs(-3.1415, sig_figs=2))
    '-3.1'
    >>> '{0:.5}'.format(round_sigfigs(0.00098765, sig_figs=2))
    '0.00099'
    >>> '{0:.6}'.format(round_sigfigs(0.00098765, sig_figs=3))
    '0.000988'
    """
    assert isNumeric(num), 'x must be numeric!'
 
    if num != 0:
        return round(num, -int(math.floor(math.log10(abs(num))) - (sig_figs - 1)))
    else:
        return 0  # Can't take the log of 0
 
if __name__ == '__main__':
 
    import decimal
    numberList = ['976.45', '84000', '0.0094', '301.07', '4.000', '10', '5280', '400']
 
    for eachNum in map(lambda x: decimal.Decimal(str(x)), numberList):
 
        originalNumStr = str(eachNum)
        nsdStr = ":".join(['numSigDigits', str(numSigDigits(eachNum))])
        msdStr = ":".join(['mostSigDigit', str(mostSigDigit(eachNum))])
        lsdStr = ":".join(['leastSigDigit', str(leastSigDigit(eachNum))])
        roundedNumStr = ":".join(['rounded', str(round_sigfigs(eachNum, 2))])
 
        resultStr = "; ".join([originalNumStr, nsdStr, msdStr, lsdStr, roundedNumStr])
 
        print (resultStr)
