# Web-scraping-using-bs4
Scraped petitioner name and respondent name from www.greentribunal.com

Assignment-

Now your ​ First​ ​ Task​ is:
Write a function in python called ‘get_case_status’ which takes the
following parameters:
● ‘case_type’: Integer
You are selecting some ‘case type’ in the dropdown [OA, RA etc.] but
when the form is submitted, behind the curtains, an integer is being
posted to the server (​ You can verify this using ​ ‘Postman’ ​ ).So ‘OA’ is actually 3, ‘RA’ is 4 and so on and so forth. So this
‘case_type’ is an integer that will represent the actual type of the
case.
● ‘case_num’: String
This is the ‘Case No.’ that you entered in the form.
● ‘year’: Integer
This is the ‘Year’ that you selected in the form.
Based on the input parameters, ‘get_case_status’ should first fetch the html
of the ‘Case details’ page. Then parse the page (using BeautifulSoup or
regex) and return a single dictionary with the following keys:
● ‘petitioner’: String
In the case details page, the first name is the ‘petitioner’ (the name
before ‘VS’) i.e. for this particular example ‘petitioner’ will be
‘Ramakant Gautam & Ors.’.
● ‘respondent’: String
In the case details page, the second name (after the ‘VS’) is the
‘respondent’ i.e. for the example ‘respondent’ will be ‘State of Madhya
Pradesh & Ors’
● ‘is_disposed’: Boolean
In the case details page, you will see that the ‘Case Status’ is
‘DisposedOff’. In this case ‘is_disposed’ should be True.
If the case details page shows ‘Case Status’ as anything other than
‘DisposedOff’, ‘is_disposed’ should be False.
For example: for case Appeal 1/2016 of 2016 (Case no. ‘1/2016’ and
Year ‘2016’) ‘is_disposed’ will be False.
Captcha: ​ The form you need to submit also has a captcha. Use python ​ PIL
to show the image to the user on the terminal and interactively take the
user’s input.
Note​ :● Do NOT use libraries/technologies like PhantomJS, Mechanize,
Selenium etc.
● Please follow the ‘​ PEP 0008​ ’ coding style guidelines.
● Make your code ​ as readable​ ​ as possible​ .
● Your function should be robust (use relevant error handling)
● Test your function with several cases of different case types and
years
Now write a python script (populate_db.py), which uses the
‘get_case_status’ function to fetch the ‘case details’ (the dictionary that the
above function was returning) of any 5 cases and store them in a MongoDB
collection called ‘cases’ in ‘test’ database
