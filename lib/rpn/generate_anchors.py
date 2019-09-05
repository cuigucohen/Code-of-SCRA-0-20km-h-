import numpy as np
def generate_anchors():
    x_ctr=(38-1)/2
    y_ctr=(28-1)/2
    z1=np.array([[12,12],[14,11],[15,10]])
    z1_shape=np.arange(z1.shape[0])
    np.random.shuffle(z1_shape)
    z11=z1[z1_shape[0:2]]
    w1=z11[0,0]
    h1=z11[0,1]
    w2=z11[1,0]
    h2=z11[1,1]
    z2 = np.array([[41, 41], [45, 36], [50, 34]])
    z2_shape = np.arange(z2.shape[0])
    np.random.shuffle(z2_shape)
    z12 = z2[z2_shape[0:2]]
    w3 = z12[0, 0]
    h3 = z12[0, 1]
    w4 = z12[1, 0]
    h4 = z12[1, 1]
    z3 = np.array([[76, 76], [86, 69], [94, 63]])
    z3_shape = np.arange(z3.shape[0])
    np.random.shuffle(z3_shape)
    z13 = z3[z3_shape[0:2]]
    w5 = z13[0, 0]
    h5 = z13[0, 1]
    w6 = z13[1, 0]
    h6 = z13[1, 1]
    z4 = np.array([[41, 41], [45, 36], [50, 34]])
    z4_shape = np.arange(z4.shape[0])
    np.random.shuffle(z4_shape)
    z14 = z4[z4_shape[0:2]]
    w7 = z14[0, 0]
    h7 = z14[0, 1]
    w8 = z14[1, 0]
    h8 = z14[1, 1]
    z5 = np.array([[76, 76], [86, 69], [94, 63]])
    z5_shape = np.arange(z5.shape[0])
    np.random.shuffle(z5_shape)
    z15 = z5[z5_shape[0:2]]
    w9 = z15[0, 0]
    h9 = z15[0, 1]
    w10 = z15[1, 0]
    h10 = z15[1, 1]
    z6 = np.array([[151, 151], [169, 135], [186, 124]])
    z6_shape = np.arange(z6.shape[0])
    np.random.shuffle(z6_shape)
    z16 = z6[z6_shape[0:2]]
    w11 = z16[0, 0]
    h11 = z16[0, 1]
    w12 = z16[1, 0]
    h12 = z16[1, 1]
    z7 = np.array([[76, 76], [94, 63], [108, 54]])
    z7_shape = np.arange(z7.shape[0])
    np.random.shuffle(z7_shape)
    z17 = z7[z7_shape[0:2]]
    w13 = z17[0, 0]
    h13 = z17[0, 1]
    w14 = z17[1, 0]
    h14 = z17[1, 1]
    z8 = np.array([[151, 151], [186, 124], [215, 108]])
    z8_shape = np.arange(z8.shape[0])
    np.random.shuffle(z8_shape)
    z18 = z8[z8_shape[0:2]]
    w15 = z18[0, 0]
    h15 = z18[0, 1]
    w16 = z18[1, 0]
    h16 = z18[1, 1]
    z9 = np.array([[306, 306], [375, 250], [433, 216]])
    z9_shape = np.arange(z9.shape[0])
    np.random.shuffle(z9_shape)
    z19 = z9[z9_shape[0:2]]
    w17 = z19[0, 0]
    h17 = z19[0, 1]
    w18 = z19[1, 0]
    h18 = z19[1, 1]
    w_all = [w1, w2, w3, w4, w5, w6, w7, w8, w9,w10, w11, w12, w13, w14, w15, w16, w17, w18]
    h_all = [h1, h2, h3, h4, h5, h6, h7, h8, h9,h10, h11, h12, h13, h14, h15, h16, h17, h18]
    # print(w_all,h_all)
    anchors = np.vstack([anchor(w_all, h_all, x_ctr, y_ctr, i) for i in range(18)])
    return (anchors)


def anchor(w_all, h_all, x_ctr, y_ctr, i):
    anchor = np.hstack((x_ctr - 0.5 * (w_all[i] - 1),
                        y_ctr - 0.5 * (h_all[i] - 1),
                        x_ctr + 0.5 * (w_all[i] - 1),
                        y_ctr + 0.5 * (h_all[i] - 1)))
    return anchor

if __name__ == '__main__':
    import time
    t = time.time()
    a = generate_anchors()
    print time.time() - t
    print a
    from IPython import embed; embed()
