#coding=utf-8
import sys

word_dict = {}

idf_dict = {}

def read_idf_file_func(idf_file_fd):
    with open(idf_file_fd, 'r') as fd:
        for line in fd:
            ss = line.strip().split('\t')
            if len(ss) != 2:
                print(1)
                continue
            token = ss[0].strip()
            idf_score = ss[1].strip()
            idf_dict[token] = float(idf_score)
            

def mapper_func(idf_file_fd):
    read_idf_file_func(idf_file_fd)
    
    for line in sys.stdin:
        ss = line.strip().split('\t')
        file_name = ss[0].strip()
        file_context = ss[1].strip()
        word_list = file_context.split(' ')
        
        for word in word_list:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        
        for k,v in word_dict.items():
            if k not in idf_dict:
                continue
            
            print(file_name,k,float(v / len(word_list)),idf_dict[k],float(v / len(word_list)) * idf_dict[k])
        
if __name__ == "__main__":
    module = sys.modules[__name__]
    func = getattr(module,sys.argv[1])
    args = None
    if len(sys.argv) > 1:
        args = sys.argv[2:]
    func(*args)
