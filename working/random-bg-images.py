#  To return random set of n url
# python random-bg-images.py urllist.txt 5 
import random, sys
lines = open(sys.argv[1]).readlines()
np = sys.argv[2]
# print np
# print(lines)
random.shuffle(lines)
# print(xrange(len(lines)))
rurl = random.sample(xrange(len(lines)), int(np))
# print (rurl)
for line in rurl:
    print lines[line].strip()
