import re, pyperclip

phoneRegex =  re.compile(r'''( (\()? 
                 (\d{3})
                 (\))?
                 (\s|-|\.)
                 (\d{3})
                 (\s|-|\.)
                 (\d{4})
                 (\s*(ext|x|ext.)\s*(\d{2,5}))? )''',re.VERBOSE)

emailRegex = re.compile(r'(([a-zA-Z0-9._%+_=]+)' 
                     r'([@])'
                     r'([a-zA-Z]+)'
                     r'(\.[a-zA-Z]{2,4})'
                     r'(\.)?'
                     r'([a-zA-Z]{2,4})?)'
                     r'',re.VERBOSE)

text = '''Contact Us

No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103 USA
Phone: 800.420.7240 or +1 415.863.9900 (9 a.m. to 5 p.m., M-F, PST)
Fax: +1 415.863.9950

(800)-429-4029

Reach Us by Email

General inquiries: info@nostarch.com
Media requests: media@nostarch.com
Academic requests: academic@nostarch.com (Further information)
Help with your order: info@nostarch.com
and inffoo@nostart.co.za'''

match = []

for groups in phoneRegex.findall(text):
    # print(groups)

    number = '-'.join([groups[2], groups[5], groups[7]])
    match.append(number)

for groupz in emailRegex.findall(text):
    # print(groupz)
    match.append(groupz[0])


print(match)
