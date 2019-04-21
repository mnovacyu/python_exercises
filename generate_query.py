#!/usr/bin/env python3

"""
Generates a where clause based on inputs of workbook, sheet, column1, and column2.
Outputs to a 'Output.txt' file

Requirements:
    'pandas' and 'xlrd' pip packages

Usage:
    python3 generate_query.py -w <workbook> -s <sheet> -c1 <column1> -c2 <column2>
    
Example:
    python3 generate_query.py -w "Example.xlsx" -s "Sheet1" -c1 "ReportingPopulationName" -c2 "HRChaseID"

Sample Output:
    ===
    Workbook='Example.xlsx', Sheet='Sheet1', Column1 = 'ReportingPopulationName', Column2 = 'HRChaseID':
    ===
    (ReportingPopulationName = 'Michael' AND HRChaseID in ('Orange', 'Banana', 'Apple'))
    OR (ReportingPopulationName = 'Cynthia' AND HRChaseID in ('Carrots', 'Potato', 'Cabbage'))
    OR (ReportingPopulationName = 'Simon' AND HRChaseID in ('Car', 'House', 'Tree'))
"""

import argparse
from datetime import datetime
import pandas as pd

# Generate Query
def generate_query(workbook, sheet, column1, column2):
    x1 = pd.ExcelFile(workbook)

    # Read entire sheet
    print("Reading '%s' workbook and '%s' sheet." % (workbook, sheet))
    df = x1.parse(sheet)

    # Generate dictionary
    d = {}
    for index, row in df.iterrows():
        append = ""
        if row[column1] in d and row[column2] not in d[row[column1]]:
            d[row[column1]].append(row[column2])
        elif row[column1] not in d:
            d[row[column1]] = [row[column2]]

    # Generate query
    i = 1
    where_clause = ""
    for key in d:
        items = "("
        for item in d[key]:
            if item == d[key][-1]:
                items += "'%s')" % item
            else:
                items += "'%s', " % item
        if i == 1:
            where_clause += "(P.ReportingPopulationName = '%s' AND C.HRChaseID IN %s)\n" % (key, items)
        else:
            where_clause += "OR (P.ReportingPopulationName = '%s' AND C.HRChaseID IN %s)\n" % (key, items)
        i += 1

    # Write to output file
    with open("Output.txt", "a") as myfile:
        time = (str(datetime.now())).split('.')[0]
        myfile.write("=====\n%s\nWorkbook='%s', Sheet='%s', Column1 = '%s', Column2 = '%s':\n=====\n" % (time, workbook, sheet, column1, column2))
        
        myfile.write("%s\n\n" % where_clause)
    
    print("Where clause generated to Output.txt")

# Run it
if __name__ == "__main__":
    try:
        # Argument Parser
        parser = argparse.ArgumentParser()
        parser.add_argument("-w", "--workbook", required=False, 
            help="Name of workbook")
        parser.add_argument("-s", "--sheet", required=False, 
            help="Name of sheet")
        parser.add_argument("-c1", "--column1", required=False, 
            help="Choose first column name")
        parser.add_argument("-c2", "--column2", required=False, 
            help="Choose second column name")
        args = parser.parse_args()

        workbook = args.workbook
        sheet = args.sheet
        column1 = args.column1
        column2 = args.column2

        # Generate query
        generate_query(workbook, sheet, column1, column2)
    except Exception as e:
        print("Error: %s" % e)

