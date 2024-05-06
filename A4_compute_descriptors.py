import numpy as np

def feat2vec(codewords, features):
    vector = np.zeros(len(codewords),dtype=np.float32)
    for feature in features:
        min_dist = -1
        min_idx = -1
        for i, codeword in enumerate(codewords):
            if min_dist == -1:
                min_dist = np.linalg.norm(codeword - feature)
                min_idx = i
                continue
            dist = np.linalg.norm(codeword - feature)
            if min_dist > dist:
                min_dist = dist
                min_idx = i
        vector[min_idx] = vector[min_idx] + 1
    return vector



if __name__=="__main__":
    codewords = np.fromfile('codewords')
    codewords = codewords.reshape(-1,128)
    des = np.array([], dtype=np.float32)
    header = np.array([1000,len(codewords)],dtype=np.int32)
    df = np.zeros(len(codewords))

    for i in range(1000):
        print("computing "+str(i)+"th iteration")
        with open('./sift/sift'+str(i+100000)) as f:
            data = np.fromfile(f, dtype=np.ubyte)
            data = data.reshape(-1,128)
            vector = feat2vec(codewords=codewords,features=data)
            des = np.append(des,vector)

    # des = des.reshape(-1,128)
    # df = (des != 0).sum(axis=0)
    # idf = np.log(1001/(1+df))
    # tf_idf = des*idf
    # tf_idf = tf_idf.reshape(-1).astype(np.float32)

    with open('A4_2018310773.des', "wb") as f:
        header.tofile(f)
        des.tofile(f)
