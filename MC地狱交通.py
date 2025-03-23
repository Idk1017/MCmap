import matplotlib.pyplot as plt
from matplotlib import rcParams

#Setting font properties
plt.rcParams['font.family']="FangSong"

#Functions
#主干道
def draw_main_lines(x1,y1,x2,y2):
    plt.plot([x1,x2],[y1,y2],marker='',color='blue',linewidth=5,label='主干道')

draw_main_lines(0,0,100,0)
draw_main_lines(0,0,0,-100)
plt.show()


