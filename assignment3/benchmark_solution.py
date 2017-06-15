# this file is used to benchmark a test solution with known input
'''
{
   "checkpoint_params":{
      "grad_clip":1.0,
      "dataset":"flickr8k",
      "image_encoding_size":512,
      "eval_max_images":-1,
      "drop_prob_decoder":0.5,
      "word_encoding_size":512,
      "max_epochs":30,
      "eval_batch_size":100,
      "fappend":"google",
      "generator":"lstm",
      "write_checkpoint_ppl_threshold":25.0,
      "decay_rate":0.997,
      "tanhC_version":1,
      "hidden_size":512,
      "momentum":0.0,
      "worker_status_output_directory":"/scail/u/karpathy/rnn-image-describer/status",
      "learning_rate":0.000478,
      "checkpoint_output_directory":"/scail/u/karpathy/rnn-image-describer/cv",
      "do_grad_check":0,
      "word_count_threshold":5,
      "batch_size":128,
      "regc":3.48e-07,
      "smooth_eps":1e-08,
      "solver":"rmsprop",
      "eval_period":0.5,
      "drop_prob_encoder":0.5
   },
   "imgblobs":[
      {
         "img_path":"7EGRMwN.jpg",
         "candidate":{
            "text":"a white dog is jumping over a red and white fence",
            "logprob":-11.260886048201762
         }
      },
      {
         "img_path":"89pUfSc.jpg",
         "candidate":{
            "text":"a brown dog is running through a field",
            "logprob":-7.0351893849438589
         }
      },
      ...
}
'''
import re
import json

import sys

A = ['123', '12', '1', '12']
B = ['12', '1', '12', '123']


def lcs(a, b):
    print(a)
    print(b)
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = []
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result.insert(0, a[x-1])
            x -= 1
            y -= 1
    print(result)
    return len(result)


def benchmark_s(a, b):
    set_a = set(a)
    set_b = set(b)
    sameWords = set.intersection(set_a, set_b)
    p_s = len(sameWords) / ((len(set_a) + len(set_b)) / 2)
    return p_s


def benchmark_lcs(a, b):
    p_lcs = lcs(a, b) / ((len(a) + len(b)) / 2)
    return p_lcs


def benchmark_all(s, lcs):
    return (s + lcs) / 2


DATA = int(sys.argv[1])  # 8k or 30k
tokenFileName = "Flickr8k.token.txt" if DATA == 8 else "results_20130124.token"

with open(tokenFileName) as f:
    content = f.readlines()
tokens = [x for x in content]

regex = r"(.+?\.jpg.*?)#(\d+)\t(.+?)$"
token_map = {}
for line in tokens:
    obj = re.match(regex, line)
    name = obj.group(1)
    sentence = obj.group(3).lower().replace(".", "").strip()
    if name in token_map:
        token_map[name].append(sentence)
    else:
        token_map[name] = [sentence]

# test input data
# for x in token_map.keys():
#     print(x)
#     print(token_map[x])


# read the result_struct.json file
# argv[2]: the result_struct.json file name
print("Loading {}\n".format(sys.argv[2]))
with open(sys.argv[2]) as data_file:
    parsed_json = json.load(data_file)
img_blobs = parsed_json['imgblobs']
max_bm = 0.0
min_bm = 1.0
avg_bm = 0.0
for img in img_blobs:
    file_name = img['img_path']
    sentence = img['candidate']['text']

    # calc result
    m = 0.0
    p_s = 0.0
    p_lcs = 0.0
    for x in token_map[file_name]:
        # prepare
        a = re.compile(r"\s+").split(sentence)
        b = re.compile(r"\s+").split(x)

        temp_s = benchmark_s(a, b)
        temp_lcs = benchmark_lcs(a, b)
        temp = benchmark_all(temp_s, temp_lcs)
        if temp > m:
            m = temp
            p_s = temp_s
            p_lcs = temp_lcs
    max_bm = max(max_bm, m)
    min_bm = min(min_bm, m)
    avg_bm += m
    print("{}: {} & {} -> {}".format(file_name, "%.4f" % p_s, "%.4f" % p_lcs, "%.4f" % m))
avg_bm /= len(img_blobs)
print("max: {}, min: {}, avg: {}".format(max_bm,min_bm,avg_bm))

