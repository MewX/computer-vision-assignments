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


def lcs(S, T):
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_list = list()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_list = list()
                    longest = c
                    lcs_list.append(S[i-c+1:i+1])
                elif c == longest:
                    lcs_list.append(S[i-c+1:i+1])

    return len(lcs_list)


def benchmark(a, b):
    set_a = set(a)
    set_b = set(b)
    sameWords = set.intersection(set_a, set_b)
    p_s = len(sameWords) / ((len(set_a) + len(set_b)) / 2)

    # p_lcs = lcs(a, b) / ((len(a) + len(b)) / 2)
    p_lcs = 1
    return p_s * p_lcs


DATA = int(sys.argv[1])  # 8k or 30k
tokenFileName = "Flickr8k.token.txt" if DATA == 8 else "results_20130124.token"

with open(tokenFileName) as f:
    content = f.readlines()
tokens = [x for x in content]

regex = r"(.+?\.jpg.*?)#(\d+)\t(.+?)$"
token_map = {}
for line in tokens:
    # print("{} - {}\n".format(regex, line))
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
for img in img_blobs:
    file_name = img['img_path']
    sentence = img['candidate']['text']

    # calc result
    m = 0.0
    for x in token_map[file_name]:
        temp = benchmark(sentence, x)
        m = max(temp, m)
    print("{}: {}".format(file_name, "%.4f" % m))
    # print("{}: {}\n".format(file_name, sentence))


# parse prediction results
# build image ~ text table
# fake longest common substring
# average benchmark: percentage of matched words * LCS/avg length
