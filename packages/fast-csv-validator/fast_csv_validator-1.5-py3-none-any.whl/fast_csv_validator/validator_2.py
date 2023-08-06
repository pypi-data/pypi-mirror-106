#!/usr/bin/python
import re
import sys
import xlsxwriter
import os
from six.moves import urllib


def create_file(filename, row_seq):
    #create a file containing the rows
    file = open(filename, "w+")
    file.seek(0, 0)
    file.writelines(row_seq)


def validate():
    param = len(sys.argv)
    if param != 2:
        print("should accept a file as parameter")
        exit(1)
    else:
        url = sys.argv[1]
        if url.startswith('http'):
            filename = url.split('/')[-1]
            (filenamebase, extension) = os.path.splitext(filename)
            save_path = os.path.join(os.getcwd(), filename)
            urllib.request.urlretrieve(url, save_path)
            url = save_path
        else:
            (path, filename) = os.path.split(url)
            (filenamebase, extension) = os.path.splitext(filename)
    total = 0
    table = {}
    number = 0
    standard_seq = list()
    non_standard_seq = list()
    #rule_comma = r'\,'
    #rule_stroke = r'\|'
    # when set the double quotation as the text qualifier
    #rule_comma_with_text_qualifier = r'\".*?\"'


    with open(url, 'r') as reader:
        for line in reader:
            total = total + 1
            #new_line = re.sub(rule_comma_with_text_qualifier , "" , line)
            occurances = re.findall(r'\"', line)
            count = len(occurances)
            if count > 0:
                result = count % 2 
                if result is not 0:
                    standard_seq.append(line)
                else:
                    non_standard_seq.append("line("+str(total) + ")\t" + line)
                if count in table:
                    table[count] += 1
                else:
                    table[count] = 1

    #print("the expected line delimiter number is %d"%number)


    create_file(filenamebase + "_standard.csv", standard_seq)
    create_file(filenamebase + "_non_standard.csv", non_standard_seq)

if __name__ == "__main__":
    validate()
