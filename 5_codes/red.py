import sys
import math

current_word = None
doc_cnt = 508
count_pool = []
sum = 0

for line in sys.stdin:
    ss = line.strip().split('\t')
    if len(ss) != 2:
        continue

    word, val = ss
    if current_word == None:
        current_word = word
    if current_word != word:
        for count in count_pool:
            sum += count

        idf_score = math.log(float(doc_cnt) / (float(sum) + 1))
        print '\t'.join([current_word, str(idf_score)])

        current_word = word
        count_pool = []
        sum = 0

    count_pool.append((int(val)))

for count in count_pool:
    sum += count

idf_score = math.log(float(doc_cnt) / (float(sum) + 1))
print '\t'.join([current_word, str(idf_score)])

