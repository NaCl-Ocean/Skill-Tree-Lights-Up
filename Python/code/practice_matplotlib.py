from matplotlib import pyplot  as plt
from matplotlib.legend_handler import HandlerLine2D
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import numpy as np
from matplotlib import colors



# fig = plt.figure()
# ax = fig.add_axes((0,0,0.5,0.5))
#
# ax.set_xlabel('x axis')
# fig.tight_layout()
# plt.show()

fig7, f7_axs = plt.subplots(ncols=3, nrows=3)
gs = f7_axs[0, 0].get_gridspec()
# remove the underlying axes
for ax in f7_axs[1:, -1]:
    ax.remove()
axbig = fig7.add_subplot(gs[1:, -1])
axbig.annotate('Big Axes \nGridSpec[1:, -1]', (0.1, 0.5),
               xycoords='axes fraction', va='center')

fig7.tight_layout()

#
# fontsize = 24
# ax.locator_params(nbins=3)
# ax.set_xlabel('x-label', fontsize=fontsize)
# ax.set_ylabel('y-label', fontsize=fontsize)
# ax.set_title('Title', fontsize=fontsize)
# plt.show()


line_1, = f7_axs[0,0].plot([1,2,3],[4,5,6],linestyle = '-',visible = True,marker='.',color ='xkcd:gold',
                  markeredgecolor = 'g',markeredgewidth = 4)
plt.show()
# line_2, = ax.plot([1,2,3],[6,5,4],linestyle='--')

# line_1.set_label('test_1')
# line_2.set_label('test_2')
# yaxis = ax.yaxis
# xaxis = ax.xaxis

# tick
# for tick in yaxis.get_major_ticks():
#     tick.label1.set_visible(True)
#     tick.label2.set_visible(True)
#     tick.tick1line.set_visible(True)
#     tick.tick2line.set_visible(True)
#
# for tick in xaxis.get_major_ticks():
#     tick.label1.set_visible(True)
#     tick.label2.set_visible(True)
#     tick.tick1line.set_visible(True)
#     tick.tick2line.set_visible(True)

# legend_1 = ax.legend([(line_1,line_2)],['test'],loc='upper right',bbox_to_anchor=(0.6,1))
# legend_1.set_label('legend_1')
# ax.add_artist(legend_1)
# legend_2 = ax.legend()


cmap = cm.get_cmap('viridis',512)
new_cmap = ListedColormap(cmap(np.linspace(0.25,0.75,256)))
print((new_cmap(np.linspace(0,0.5,128))))
print(len(new_cmap.colors))

LinearSegmentedColormap.from_list('cmap1',['black','cyan','ivory'])

bounds = np.array([-0.25, -0.125, 0, 0.5, 1])
norm = colors.BoundaryNorm(boundaries=bounds, ncolors=4)
print(norm([-0.2,-0.15,-0.02, 0.3, 0.8, 0.99]))






