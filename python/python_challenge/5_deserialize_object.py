import pickle
import requests

url = "http://www.pythonchallenge.com/pc/def/banner.p"
r = requests.get(url)
# pickle.load() unpickles a pickled file
# pickle.loads() unpickles a string(which might be read from a file);
# pickle.dump() pickles to a file
# pickle.dumps() pickles to a string.
data = pickle.loads(r.content)
print data

for line in data:
    print ''.join(item[0] * item[1] for item in line)

# >>>
#               #####                                                                      #####
#                ####                                                                       ####
#                ####                                                                       ####
#                ####                                                                       ####
#                ####                                                                       ####
#                ####                                                                       ####
#                ####                                                                       ####
#                ####                                                                       ####
#       ###      ####   ###         ###       #####   ###    #####   ###          ###       ####
#    ###   ##    #### #######     ##  ###      #### #######   #### #######     ###  ###     ####
#   ###     ###  #####    ####   ###   ####    #####    ####  #####    ####   ###     ###   ####
#  ###           ####     ####   ###    ###    ####     ####  ####     ####  ###      ####  ####
#  ###           ####     ####          ###    ####     ####  ####     ####  ###       ###  ####
# ####           ####     ####     ##   ###    ####     ####  ####     #### ####       ###  ####
# ####           ####     ####   ##########    ####     ####  ####     #### ##############  ####
# ####           ####     ####  ###    ####    ####     ####  ####     #### ####            ####
# ####           ####     #### ####     ###    ####     ####  ####     #### ####            ####
#  ###           ####     #### ####     ###    ####     ####  ####     ####  ###            ####
#   ###      ##  ####     ####  ###    ####    ####     ####  ####     ####   ###      ##   ####
#    ###    ##   ####     ####   ###########   ####     ####  ####     ####    ###    ##    ####
#       ###     ######    #####    ##    #### ######    ###########    #####      ###      ######
