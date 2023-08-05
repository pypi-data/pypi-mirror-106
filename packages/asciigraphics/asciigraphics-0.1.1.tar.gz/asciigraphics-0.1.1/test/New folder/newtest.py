import asciigraphics as a
import time
a.createcanvas(100,100,False)
plt = a.figure(10,10,80,80,[0,31],[0,650],5,100,2)
k=[[30,400],[20,150]]
plt.line(k,[2,2],4)
a.draw()
input()