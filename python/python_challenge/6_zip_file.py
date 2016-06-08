import re
import zipfile
import requests


# download the zip file
r = requests.get("http://www.pythonchallenge.com/pc/def/channel.zip")
with open("channel.zip", 'w') as f:
    f.write(r.content)

# unzip the zip file
# with zipfile.ZipFile ("channel.zip") as myzip:
#     myzip.extractall("channel")
zip = zipfile.ZipFile("channel.zip", 'r')

s = zip.read("readme.txt")
print s
# >>>
# welcome to my zipped list.
# hint1: start from 90052
# hint2: answer is inside the zip

m = re.match(".*hint1: start from (\d+)", s, re.DOTALL)
if m:
    next_file = m.group(1) + '.txt'
    print "starting from file: " + next_file
    # >>>
    # starting from file: 90052.txt
else:
    raise Exception("Didn't match starting file from: " + s)

comments = []
s = zip.read(next_file)
print s
comments.append(zip.getinfo(next_file).comment)
while True:
    # re.DOTALL flag tells python to make the '.' special character match all characters, including newline characters.
    m = re.match(".*Next nothing is (\d+)", s, re.DOTALL)
    if m:
        next_file = m.group(1) + '.txt'
        s = zip.read(next_file)
        print s
        comments.append(zip.getinfo(next_file).comment)
    else:
        print ''.join(comments)
        raise Exception("No match: " + s)

# >>>
# Collect the comments.
# ****************************************************************
# ****************************************************************
# **                                                            **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
# **                                                            **
# ****************************************************************
#  **************************************************************


# >>>
# it's in the air. look at the letters.


# >>>
# http://www.pythonchallenge.com/pc/def/oxygen.html
