import sys

for line in sys.stdin:
    ss = line.strip().split('\t')
    file_name = ss[0].strip()
    file_context = ss[1].strip()
    word_list = file_context.split(' ')

    word_set = set()
    for word in word_list:
        word_set.add(word)

    for word in word_set:
        print '\t'.join([word, '1'])


