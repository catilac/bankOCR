"""
BankOCR Kata
"""

from images import *

def each_digit(data):
    """returns string of individual digit"""
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
    """calculates checksum using formula:
        (d1+2*d2+3*d3 +..+9*d9) mod 11
        if result is 0 than the acct_num is valid"""
    chksum = 0
    acct_len = len(digitized_acct_num)
    for i, n in enumerate(xrange(acct_len, 0, -1)):
        d_n = int(digitized_acct_num[n-1])
        chksum += i*d_n

    return chksum % 11

def is_checksum_err(digitized_acct_num):
    return checksum(digitized_acct_num) == 0

def print_result(digitized_acct_num, scan_err, chksum_err):
    if scan_err:
        err_msg = "ILL"
    elif chksum_err:
        err_msg = "ERR"
    else:
        err_msg = ""

    print digitized_acct_num, err_msg

def process(acct_num):
    digitized, scan_err = scan(acct_num)
    chksum_err = False if scan_err else is_checksum_err(digitized)
    print_result(digitized, scan_err, chksum_err)


def scan(acct_num):
    """Scan the acct_num and return a 'digitized' value"""
    digitized = ""
    scan_err = False
    for digit in each_digit(acct_num):
        scanned = scan_digit(digit)
        if scanned == "?":
            scan_err = True
        digitized += scanned

    return digitized, scan_err

def scan_digit(digit):
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
