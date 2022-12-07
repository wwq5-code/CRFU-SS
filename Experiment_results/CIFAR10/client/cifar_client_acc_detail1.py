

import numpy as np
import matplotlib.pyplot as plt

epsilon = 3
beta = 1 / epsilon


y_bfu_back_acc =[0.9749999940395355, 0.7449999650319418, 0.30499999473492306, 0.02166666587193807, 0.008333333147068819]
y_bfu_acc = [0.9799999713897705, 0.8119999766349792, 0.5620000004768372, 0.2919999957084656, 0.1539999946951866]

y_ss_back_acc = [0.9849999845027924, 0.7799999713897705, 0.34166665251056355, 0.02999999901900689, 0.004999999888241291]
y_ss_acc = [0.9819999814033509, 0.8519999861717225, 0.7580000042915345, 0.7099999785423279, 0.6739999890327454]

y_hfu_back_acc= [0.99, 0.28999999165534973, 0.0, 0.0,0]
y_hfu_acc = [0.986,0.9868333339691162, 0.8956666588783264, 0.8953333497047424, 0.87]


x=[]
y_unl_s = []
y_unl_self_s =[]
y_nips_rkl_s =[]
y_hessian_30_s =[]
for i in range(5):
    # print(np.random.laplace(0, 1)/10+0.2)
    x.append(i)
    #y_fkl[i] = y_fkl[i*2]*100
    #y_bfu_back_acc[i] = y_bfu_back_acc[i]*100
    y_bfu_acc[i] = y_bfu_acc[i]*100
    #y_ss_back_acc[i] = y_ss_back_acc[i]*100
    y_ss_acc[i] = y_ss_acc[i]*100
    #y_hfu_back_acc[i] = y_hfu_back_acc[i]*100
    #y_hfu_acc[i] = y_hfu_acc[i]*100


plt.figure()
plt.plot(x, y_bfu_acc, color='orange',  marker='x',  label='BFU',linewidth=4,  markersize=10)
plt.plot(x, y_ss_acc, color='g',  marker='*',  label='BFU-SS',linewidth=4, markersize=10)
#plt.plot(x, y_fkl, color='g',  marker='+',  label='VRFL')
#plt.plot(x, y_hfu_acc, color='r',  marker='p',  label='HFU',linewidth=4, markersize=10)

# plt.plot(x, unl_fr, color='blue', marker='^', label='Retrain',linewidth=4, markersize=10)
# plt.plot(x, unl_br, color='orange',  marker='x',  label='BFU',linewidth=4,  markersize=10)
# plt.plot(x, unl_self_r, color='g',  marker='*',  label='BFU-SS',linewidth=4, markersize=10)
# plt.plot(x, unl_hess_r, color='r',  marker='p',  label='HFU',linewidth=4, markersize=10)

# plt.plot(x, y_unl_s, color='b', marker='^', label='Normal Bayessian Fed Unlearning',linewidth=3, markersize=8)
# plt.plot(x, y_unl_self_s, color='r',  marker='x',  label='Self-sharing Fed Unlearning',linewidth=3, markersize=8)
# #plt.plot(x, y_fkl, color='g',  marker='+',  label='VRFL')
# plt.plot(x, y_hessian_30_s, color='y',  marker='*',  label='Unlearning INFOCOM22',linewidth=3, markersize=8)


plt.grid()
leg = plt.legend(fancybox=True, shadow=True)
plt.xlabel('Epoch' ,fontsize=20)
plt.ylabel('Accuracy (%)' ,fontsize=20)
my_y_ticks = np.arange(0 ,105,20)
plt.yticks(my_y_ticks,fontsize=20)
plt.xticks(x,fontsize=20)
# plt.title('CIFAR10 IID')
plt.legend(loc='best',fontsize=20)
plt.tight_layout()
#plt.title("Fashion MNIST")
plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('cifar_client_detail_acc.png', dpi=400)
plt.show()