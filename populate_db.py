#!/usr/bin/python
# -*- coding: utf-8 -*-
from case_details import *
import pymongo
connection = pymongo.Connection()

db = connection['test']
employees = db['cases']

var = get_case_status('3', '496/2015', '2015')

# ....get_case_status('3', '325/2015', '2015'),
# ....get_case_status('3', '400/2015', '2015'),
# ....get_case_status('3', '420/2015', '2015'),
# ....get_case_status('5', '450/2015', '2015')

info = {'petitioner': var['petitioner'], 'respondent': var['respondent'
        ], 'is_disposed': var['is_disposed']}

cases.insert(info)

cursor = test.cases.find()
for case in test.cases.find():
    print case

			
