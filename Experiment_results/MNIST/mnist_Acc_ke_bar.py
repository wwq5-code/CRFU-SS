import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = ['$K_e$ = 1', '$K_e$ = 2', '$K_e$ = 3', '$K_e$ = 4', '$K_e$ = 5']
unl_fr = [97.5, 97.5 , 97.5, 97.5, 97.5]
unl_br = [97.44, 97.6, 97.3, 95.6, 89]
unl_self_r = [97.48, 97.68, 97.4, 97.2, 96.1]
unl_hess_r = [97.5,  97.3, 97.5, 97.453, 97]

x = np.arange(len(labels))  # the label locations
width = 0.6  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)


plt.subplots()
plt.bar(x - width / 2 + width / 8, unl_fr, width=0.148, label='Retrain', hatch='/')
plt.bar(x - width / 8, unl_br, width=0.148, label='BFU', hatch='**')
plt.bar(x + width / 8, unl_self_r, width=0.148, label='BFU-SS', hatch='++')
plt.bar(x + width / 2 - width / 8, unl_hess_r, width=0.148, label='HFU', hatch='-')
# Add some text for labels, title and custom x-axis tick labels, etc.
plt.ylabel('Accuracy (%)', fontsize=20)
# ax.set_title('Performance of Different Users n')
plt.xticks(x, labels, fontsize=20)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 110, 20)
plt.yticks(my_y_ticks, fontsize=20)
# ax.set_yticklabels(my_y_ticks,fontsize=15)

plt.legend(loc='lower right', fontsize=15)

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
plt.savefig('mnist_Acc_ke_bar.png', dpi=400)
plt.show()
