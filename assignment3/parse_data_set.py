import json

# take input: [img dir] [train img list] [sentences file]
import re
import sys

'''
JSON format:
{
    images: [
        {
            split: "train", # train/dev/test
            sentences: ["", "", ...]
        }
    ],
    ...
}
'''


regex = "^(.*?\.jpg)#(\d+)\t(.*?)$"
with open(sys.argv[1]) as f:
    content = f.readlines()
tokens = [x for x in content]

token_map = {}
for line in tokens:
    obj = re.match(regex, line)
    name = obj.group(1)
    sentence = obj.group(3).lower().replace(".", "").strip()
    if name in token_map:
        token_map[name].append(sentence)
    else:
        token_map[name] = [sentence]

# TODO: this code is not finished
