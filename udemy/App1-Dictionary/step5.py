import difflib
from difflib import get_close_matches

print(get_close_matches("rain",["dog","you","push","rainn","rai","ri","raain"],n=4,cutoff=0.87))
