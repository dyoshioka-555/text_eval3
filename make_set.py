import os
import random

root = "texts/"
METHOD = ["origin", "cvae", "cvae_bow", "cvae_attn"]
N_SET = 5
random.seed(0)

text_lists = {}
for method in METHOD:
    with open(root + method + ".txt", "r") as f:
        texts0 = []
        texts1 = []
        for sent in f.readlines():
            if method == "origin":
                if not int(sent.split("\t")[0]):
                    texts0.append(sent.split("\t")[1].strip().replace(" ", ""))
                if int(sent.split("\t")[0]):
                    texts1.append(sent.split("\t")[1].strip().replace(" ", ""))
            else:
                if int(sent.split("\t")[0]):
                    texts0.append(sent.split("\t")[1].strip().replace(" ", ""))
                if not int(sent.split("\t")[0]):
                    texts1.append(sent.split("\t")[1].strip().replace(" ", ""))
    text_lists[method] = {0: texts0, 1: texts1}

# print(len(text_lists["origin"][0]))
# print(len(text_lists["origin"][1]))
rand_num0 = random.sample(range(len(text_lists["origin"][0])), 50)
rand_num0.sort()
# print(rand_num0)
#rand_num1 = random.sample(range(len(text_lists["origin"][1])), 50)
#rand_num1.sort()
rand_num1 = sorted(
        [
            34,
            73,
            435,
            1023,
            1088,
            1143,
            1267,
            1329,
            1665,
            1862,
            86,
            103,
            145,
            148,
            167,
            176,
            276,
            329,
            339,
            382,
            455,
            575,
            618,
            620,
            660,
            923,
            934,
            952,
            986,
            1010,
            1015,
            1021,
            1036,
            1263,
            1343,
            1409,
            1528,
            1609,
            1645,
            1719,
            2081,
            2122,
            2155,
            2421,
            2478,
            2556,
            2571,
            2601,
            1764,
            894,
        ]
    )


for method in METHOD:
    text0 = [text_lists[method][0][i] for i in rand_num0]
    text1 = [text_lists[method][1][i] for i in rand_num1]
    text_lists[method] = {0: text0, 1: text1}
    #print(text_lists[method][0])

for n_set in range(N_SET):
    file_paths = []
    for method in METHOD:
        os.makedirs(f"texts/set{n_set + 1}", exist_ok=True)
        texts = [text_lists[method][0][(n_set + 1) + N_SET * i - 1] for i in range(10)]
        # print(texts)
        texts.extend(
            [text_lists[method][1][(n_set + 1) + N_SET * i - 1] for i in range(10)]
        )

        with open(f"texts/set{n_set + 1}/{method}.list", mode="w") as f:
            for text in texts:
                f.write(text + "\n")
