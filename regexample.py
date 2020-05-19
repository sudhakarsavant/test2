import re

str='this is my mob no +917272727272'
mobregx = re.compile(r'\+\d\d\d\d\d\d\d\d\d\d\d\d')
mob = mobregx.search(str)
print(mob)
print(mob.group())

str='this is my mob no +917272727272 and ofc no is +917272727373'
mo2=mobregx.findall(str)
for i in mo2:
    print(i)   

# output
# <re.Match object; span=(18, 31), match='+917272727272'>
# +917272727272
# +917272727272
# +917272727373

#------------------
str='this is my mob no +917272727272'
mob = re.search(r'(\+\d\d)(\d\d\d\d\d\d\d\d\d\d)',str)
print("mobile no:",mob.group())
print("Country code:", mob.group(1))
print("phone no:",mob.group(2))

#--------3rd way
def getPhoneNumber(s):
   
    mobregx = re.compile(r'(\+\d\d)(\d\d\d\d\d\d\d\d\d\d)')
    mob = mobregx.findall(str)
    if mob:
        return mob
    else:
        return None

str='this is my mob no +917272727272'
print(getPhoneNumber(str))

print('testing branch')

print('new test for checkout branching')

print('new test for checkout branching')

