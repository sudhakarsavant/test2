import re
# find name & age
str ='''Rahul is 23 and Kumar is 44 Rohit is 30 and Ram is 35'''
print(str) 
# op====> Rahul is 23 and Kumar is 44 Rohit is 30 and Ram is 35

ages=re.findall(r'\d{1,3}',str)
print('Ages are :', ages)
# op====>Ages are : ['23', '44', '30', '35']

names = re.findall(r'[A-Z][a-z]*',str)
print('Names are:', names)
# op====>Names are: ['Rahul', 'Kumar', 'Rohit', 'Ram']

agedict={}
x=0
for name in names:
    agedict[name]=ages[x]
    x +=1
print(agedict)
#op---> {'Rahul': '23', 'Kumar': '44', 'Rohit': '30', 'Ram': '35'}

#   find words ---------
str2='we need to inform him with the latest information'
if re.search('inform', str2):
    print('available')
else:
    print('Not')
#op===> available

wordcount= re.findall('inform',str2)
for i in wordcount:
    print(i)
#op===> inform
#       inform

# find index------ of word return location start & end index tuple of bith words
# or  itrewords = re.finditer('inform',str2)   then  itrewords use in for loop
for i in re.finditer('inform',str2):
    loctup =i.span()
    print(loctup)
#op===> (11, 17)
#       (38, 44)

# find same endwords letter 
# words match within [] and must end eith 'at' character
str3='bat,rat,that,hat,got,mat'
allstr=re.findall('[brthgm]at',str3)
print(allstr)
# op====> ['bat', 'rat', 'hat', 'hat', 'mat']   it will not reaturn got 

# find same words don't start with letter 
# words start carret sign '^' within [] that are ignored 
str4='bat,rat,that,cat,got,mat'
ignorestr=re.findall('[^h-m]at',str4)
print(ignorestr)
# op====>['bat', 'rat','cat'] only print & other start word with h & m are ignored

# replace or substtitute string--------
str5='bat,rat,that,cat,got,mat'
repstr=re.compile('[r]at')  # fing substtitute word for replace
str5=repstr.sub('food',str5) # replace rat with food
print(str5)
# op====> bat,food,that,cat,got,mat

# dooubleslash find words----------------
randstr='hera is \\dog'
print(randstr)
# op====>hera is \dog  it will not match \\dog doubleslash 
print(re.search(r'\\dog',randstr))
# op====><re.Match object; span=(8, 12), match='\\dog'>  it will match \\dog correct 

#  replace the \n with space

tempstr='''Keep the
blue flag
in the 
sky'''
print(tempstr)
#op===>
#Keep the
#blue flag
#in the
#sky
regex=re.compile('\n') # find \n in string
tempstr=regex.sub(' ',tempstr)
print(tempstr)
#==> Keep the blue flagin the sky

randnum='12345'
print("matches",len(re.findall('\d',randnum)))  # op===>matches 5  check number between 0-9
print("matches",len(re.findall('\D',randnum)))  # op===>matches 0  check number not in between 0-9
print("matches",len(re.findall('\d{5}',randnum)))  # op===>matches 1 check number between 0-9 & check 5 how many times

randnum='12345 123 1234 123456 1234567 1234567'
print("matches",len(re.findall('\d{5,7}',randnum)))# op===>matches 5 check number between 0-9 & check 5 to 7 how many times

#\w [A-Za-z0-9_] include this 
#\W [^A-Za-z0-9_] except this 

phone= '7272727272'
if(re.search(r'\d{10}',phone)):
    print("phone is valid")
else:
    print('not valid')

phone2='423-444-4444'
if(re.search(r'\d{3}-\d{3}-\d{4}',phone2)):
    print("phone is valid")
else:
    print('not valid')

fname='sudhakar savant'
if(re.search(r'\w{2,20}\s\w{2,20}',fname)):  # \s is used for space
    print("full name is valid")
else:
    print('not valid')

# email check

email='test@gmail.com   sup.port@cranberrynx.com  123@com  @g.com'
print('match email:',len(re.findall('[\w._%+-]{1,20}@[\w.-]{1,20}[A-Za-z]{2,3}',email)))
#op===> match email: 2
mailregex = re.findall('[\w._%+-]{1,20}@[\w.-]{1,20}[A-Za-z]{2,3}',email)
print(mailregex)
#op===> ['test@gmail.com', 'sup.port@cranberrynx.com','123@com']


#"^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$",  in JSON

#web scrapping find mobile from html page data
import urllib.request
from re import findall
url ='http://www.sumit.com/...'
response = urllib.request.urlopen(url)
html=response.read()
htmlstr=html.decode()
pddata= findall('\(\d{3})\d{3}-\d{4}',htmlstr)

for i in pddata:
    print(i)

#op===> (257) 563-7401
#       (257) 562-5401
#       (257) 564-6401