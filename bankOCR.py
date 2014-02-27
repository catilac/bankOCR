"""
BankOCR Kata
"""

from images import *

def each_digit(data):
    """
    Returns array of string of individual digit
    ex: 000... => [" _ | ||_|", " _ | ||_|", " _ | ||_|", ...]

    @param data: Array of scanlines ex: [[' _ ', ' _ ', ...], ['|_|', '|_|', ...],[...]]
    @type  data: Array
    @return Array of digit strings
    """
    width = 3
    row_len = 27
    return [''.join([row[n:n+width] for row in data]) for n in xrange(0,row_len,width)]

def scan_file(file_name):
    """Open file and scan entries 4 lines at a time"""
    with open(file_name, 'r') as in_file:
        acct_num = []
        for idx, line in enumerate(in_file):
            if (idx+1) % 4 == 0:
                process(acct_num)
                # clear acct_num
                acct_num = []
            else:
                acct_num.append(line)

def checksum(digitized_acct_num):
    """
    calculates checksum using formula: (d1+2*d2+3*d3 +..+9*d9) mod 11
    if result is 0 than the acct_num is valid

    @param digitized_acct_num: the scanned account number
    @type  digitized_acct_num: string
    @return the checksum
    """
    chksum = 0
    acct_len = len(digitized_acct_num)
    for i, n in enumerate(xrange(acct_len, 0, -1)):
        d_n = int(digitized_acct_num[n-1])
        chksum += i*d_n

    return chksum % 11

def is_checksum_err(digitized_acct_num):
    """
    Checks if the checksum is valid or not
    @param digitized_acct_num: the scanned account number
    @type  digitized_acct_num: string
    @return Bool
    """
    return checksum(digitized_acct_num) == 0

def print_result(digitized_acct_num, scan_err, chksum_err):
    """
    prints out the digitized number and whether or not there
    is a scan or checksum error.
    ex: 664371495 ERR

    @param digitized_acct_num: the scanned account number
    @type  digitized_acct_num: string
    @param scan_err: scan error?
    @type  scan_err: boolean
    @param chksum_err: checksum error?
    @type  chksum_err: boolean
    @return None
    """
    if scan_err:
        err_msg = "ILL"
    elif chksum_err:
        err_msg = "ERR"
    else:
        err_msg = ""

    print digitized_acct_num, err_msg

def process(acct_num):
    """
    Processes the account number

    @param acct_num: Account number
    @type  acct_num: [String, String, String]
    @return None
    """
    digitized, scan_err = scan(acct_num)
    chksum_err = False if scan_err else is_checksum_err(digitized)
    print_result(digitized, scan_err, chksum_err)


def scan(acct_num):
    """
    Scans the account number

    @param acct_num: Account number
    @type  acct_num: [String, String, String]
    @return (digitized, scan_err) - A single string representing the account, and
    whether or not there was a scanning error
    """
    digitized = ""
    scan_err = False
    for digit in each_digit(acct_num):
        scanned = scan_digit(digit)
        if scanned == "?":
            scan_err = True
        digitized += scanned

    return digitized, scan_err

def scan_digit(digit):
    """
    Converts " _ | ||_|" to "0"

    @param digit: the string representation of the scanned digit
    @type  digit: string
    @return ASCII digit or "?" if it couldn't be scanned
    """
    if digit == ZERO:
        return "0"
    elif digit == ONE:
        return "1"
    elif digit == TWO:
        return "2"
    elif digit == THREE:
        return "3"
    elif digit == FOUR:
        return "4"
    elif digit == FIVE:
        return "5"
    elif digit == SIX:
        return "6"
    elif digit == SEVEN:
        return "7"
    elif digit == EIGHT:
        return "8"
    elif digit == NINE:
        return "9"
    else:
        return "?"

if __name__ == "__main__":
    scan_file("test.dat")
