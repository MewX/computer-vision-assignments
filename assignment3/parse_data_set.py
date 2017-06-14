import json

# take input: [img dir] [train img list] [sentences file]
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
