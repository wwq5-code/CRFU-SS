import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = ['$\\beta$ = 0.1', '$\\beta$ = 0.5', '$\\beta$ = 1', '$\\beta$ = 1.5', '$\\beta$ = 2']
unl_fr = [10, 10, 10, 10, 10]
unl_br = [7, 5, 5, 3, 2, ]
unl_self_r = [6, 4, 4, 3, 2]
# unl_hess_r = [,  3, 9, 10]

x = np.arange(len(labels))  # the label locations
width = 0.6  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)


plt.subplots()
plt.bar(x - width / 4, unl_fr, width=0.148, label='Retrain', hatch='/')
plt.bar(x - 0, unl_br, width=0.148, label='BFU', hatch='**')
plt.bar(x + width / 4, unl_self_r, width=0.148, label='BFU-SS', hatch='++')
# plt.bar(x + width / 2 - width / 8, unl_hess_r, width=0.148, label='HFU', hatch='-')
# Add some text for labels, title and custom x-axis tick labels, etc.
plt.ylabel('Running Time', fontsize=20)
# ax.set_title('Performance of Different Users n')
plt.xticks(x, labels, fontsize=20)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 11, 1)
plt.yticks(my_y_ticks, fontsize=20)
# ax.set_yticklabels(my_y_ticks,fontsize=15)

plt.legend(loc='upper right', fontsize=15)

# ax.bar_label(rects1, padding=1)
# ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)

plt.tight_layout()

plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('mnist_rt_ur_bar.png', dpi=400)
plt.show()
