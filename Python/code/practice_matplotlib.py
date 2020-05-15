from matplotlib import pyplot  as plt
import matplotlib

plt.ioff()
fig = plt.figure()
fig,(ax1,ax2) = plt.subplots(1,2)
line_1, = ax1.plot([1,2,3],[4,5,6],linestyle = '-',visible = 'False',marker='.',
                    markeredgecolor = 'g',markeredgewidth = 4)
print(ax1.lines)
print(line_1.get_alpha())

line_1.set_label('test')
print(line_1.get_label())
line_1.set_visible(False)
yaxis = ax1.yaxis
xaxis = ax1.xaxis
for tick in yaxis.get_major_ticks():
    tick.label1.set_visible(True)
    tick.label2.set_visible(True)
    tick.tick1line.set_visible(True)
    tick.tick2line.set_visible(True)

for tick in xaxis.get_major_ticks():
    tick.label1.set_visible(True)
    tick.label2.set_visible(True)
    tick.tick1line.set_visible(True)
    tick.tick2line.set_visible(True)


plt.show()




