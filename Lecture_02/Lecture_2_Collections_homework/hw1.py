"""
check_data function takes two parameters - path to a file and a list of functions (validators).
You should:
- read data from file data.txt
- validate each line according to rules. Each rule is a function, that performs some specific check
- write a report to txt file and return absolute path to that file. For each line you should report 
it if it doesn't conform with at least one rule, plus add a reason - the name of a validator that
doesn't pass (if there are more than one failed rules, get the name of the first one that fails)

Valid line should have 5 elements in this order:
email, amount, currency, account, date

You should also implement at least two rules:
- validate_line should check if a line has 5 elements
- validate_date should check if a date is valid. In our case valid date will be anything that follows
the pattern DDDD-DD-DD (four digits - two digits - two digits). Date always exists in a line, even 
if this line is corrupted in some other way.
Feel free to add more rules!

For example, input lines:
foo@example.com 729.83 EUR accountName 2021-01:0
bar@example.com 729.83 accountName 2021-01-02
baz@example.com 729.83 USD accountName 2021-01-02

check_data(filepath, [validate_date, validate_line])

output lines:
foo@example.com 729.83 EUR accountName 2021-01:0 validate_date
bar@example.com 729.83 accountName 2021-01-02 validate_line
"""
from typing import Callable, Iterable
import re
import os

filepath = 'data.txt'


def validate_line(line: str) -> bool:
    """Check if the line consists of 5 elements"""
    return len(line.split(" ")) == 5


def validate_date(date: str) -> bool:
    """Check if the date is in format DDDD-DD-DD"""
    checked_str = date.split(" ")[-1:]
    return bool(re.fullmatch("\d{4}-\d{2}-\d{2}", *checked_str))


def check_data(file_path: str, validators: Iterable[Callable]) -> str:
    with open(file_path, 'r') as data_file, open('output_file.txt', 'w+') as output_file:
        for line in data_file:
            line = line.strip()
            for validator in validators:
                if not validator(line):
                    output_file.write(f"{line} {validator.__name__}\n")
                    break
    return os.path.abspath('output_file.txt')
