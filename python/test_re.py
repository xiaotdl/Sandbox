import re
def callable(matchobject):
    print matchobject
    print matchobject.start()
    print matchobject.pos
    print matchobject.group(0)
    print matchobject.group(1)
    print dir(matchobject)
    print (matchobject.start() > 0 and '_' or '')
    return (matchobject.start() > 0 and '_' or '') + matchobject.group(1).lower()
print re.sub("([A-Z])", callable, "NameLikeThis")
# >>> name_like_this
# one-liner: 
# re.sub("([A-Z])", lambda mo: (mo.start() > 0 and '_' or '') + mo.group(1).lower(), name)

print 2 > 1 and 1 or 0
# same as ==>
# print 1 if 2 > 1 else 0
# <==


# Multiline string matching
# Ref: https://www.thegeekstuff.com/2014/07/advanced-python-regex/
s = \
"""
<p>
1 2 3
4 5 6
7 8 9
</p>
"""

print s

# == re.DOTALL ==
# By default, the '.' special character does not match newline characters.
print re.search('<p>.*</p>', s)
# >>>
# None

# The re.DOTALL flag tells python to make the '.' special character match all characters, including newline characters.
print re.search('<p>.*</p>', s, re.DOTALL)
# >>>
# <_sre.SRE_Match object at 0x7fa4690f26b0>



# == re.MULTILINE ==
# By default in python, the '^' and '$' special characters (these characters match the start and end of a line, respectively) only apply to the start and end of the entire string.
print re.search('^4 5 6', s)
# >>>
# None

# The re.MULTILINE flag tells python to make the '^' and '$' special characters match the start or end of any line within a string.
print re.search('^4 5 6', s, re.MULTILINE)
# >>>
# <_sre.SRE_Match object at 0x7fa4690f26b0>
