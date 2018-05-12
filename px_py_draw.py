import sdf
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
#from numpy import ma
from matplotlib import colors, ticker, cm
from matplotlib.mlab import bivariate_normal
from optparse import OptionParser
import os


######## Constant defined here ########
pi        =     3.1415926535897932384626
q0        =     1.602176565e-19 # C
m0        =     9.10938291e-31  # kg
v0        =     2.99792458e8    # m/s^2
kb        =     1.3806488e-23   # J/K
mu0       =     4.0e-7*pi       # N/A^2
epsilon0  =     8.8541878176203899e-12 # F/m
h_planck  =     6.62606957e-34  # J s
wavelength=     1.0e-6
frequency =     v0*2*pi/wavelength

exunit    =     m0*v0*frequency/q0
bxunit    =     m0*frequency/q0
denunit    =     frequency**2*epsilon0*m0/q0**2
print('electric field unit: '+str(exunit))
print('magnetic field unit: '+str(bxunit))
print('density unit nc: '+str(denunit))

font = {'family' : 'monospace',  
        'style'  : 'normal',
        'color'  : 'black',  
	    'weight' : 'normal',  
        'size'   : 14,  
       }  
######### Parameter you should set ###########
start   =  0  # start time
stop    =  849  # end time
step    =  1  # the interval or step


directory = './tacc_worky_txt/'
px_y = np.loadtxt(directory+'px2d.txt')
py_y = np.loadtxt(directory+'py2d.txt')
xx_y = np.loadtxt(directory+'xx2d.txt')
yy_y = np.loadtxt(directory+'yy2d.txt')
workx2d_y = np.loadtxt(directory+'workx2d.txt')
worky2d_y = np.loadtxt(directory+'worky2d.txt')
fieldex_y = np.loadtxt(directory+'field2dex.txt')
fieldey_y = np.loadtxt(directory+'field2dey.txt')
fieldbz_y = np.loadtxt(directory+'field2dbz.txt')
gg_y = (px_y**2+py_y**2+1)**0.5


directory = './tacc_workx_txt/'
px_x = np.loadtxt(directory+'px2d.txt')
py_x = np.loadtxt(directory+'py2d.txt')
xx_x = np.loadtxt(directory+'xx2d.txt')
yy_x = np.loadtxt(directory+'yy2d.txt')
workx2d_x = np.loadtxt(directory+'workx2d.txt')
worky2d_x = np.loadtxt(directory+'worky2d.txt')
fieldex_x = np.loadtxt(directory+'field2dex.txt')
fieldey_x = np.loadtxt(directory+'field2dey.txt')
fieldbz_x = np.loadtxt(directory+'field2dbz.txt')
gg_x = (px_x**2+py_x**2+1)**0.5

number=400

tt = np.linspace(5.0,89.9,850)


#  if (os.path.isdir('jpg') == False):
#    os.mkdir('jpg')
######### Script code drawing figure ################
for n in range(start,stop+step,step):
    #### header data ####
    plt.subplot(2,1,1)
    color_index_y = gg_y[:,-1]
    plt.scatter(px_y[:,n], py_y[:,n], c=color_index_y, s=20, cmap='autumn_r', edgecolors='None')
    cbar=plt.colorbar()
    cbar.set_label(r'$\gamma$ for work_y',fontdict=font)

    color_index_x = gg_x[:,-1]
    plt.scatter(px_x[:,n], py_x[:,n], c=color_index_x, s=20, cmap='winter_r', edgecolors='None')
    cbar=plt.colorbar()
    cbar.set_label(r'$\gamma$ for work_x',fontdict=font)
       
 #   plt.legend(loc='upper right')
    plt.xlim(-5,45)
    plt.ylim(-8,8)
    plt.xlabel('P_x',fontdict=font)
    plt.ylabel('P_y',fontdict=font)
    #plt.xticks(fontsize=20); plt.yticks(fontsize=20);
    #plt.title('electron at y='+str(round(y[n,0]/2/np.pi,4)),fontdict=font)

    plt.subplot(2,1,2)
    color_index_y = gg_y[:,-1]
    plt.scatter(px_y[:,n], py_y[:,n], c=color_index_y, s=20, cmap='autumn_r', edgecolors='None')

    color_index_x = gg_x[:,-1]
    plt.scatter(px_x[:,n], py_x[:,n], c=color_index_x, s=20, cmap='winter_r', edgecolors='None')
       
 #   plt.legend(loc='upper right')
    plt.xlim(-5,505)
    plt.ylim(-40,40)
    plt.xlabel('P_x',fontdict=font)
    plt.ylabel('P_y',fontdict=font)
    #plt.xticks(fontsize=20); plt.yticks(fontsize=20);
    #plt.title('electron at y='+str(round(y[n,0]/2/np.pi,4)),fontdict=font)

    #plt.show()
    #lt.figure(figsize=(100,100))
    fig = plt.gcf()
    fig.set_size_inches(10, 13)
    fig.savefig('./fig_px_py/theta'+str(n).zfill(4)+'.png',format='png',dpi=80)
    plt.close("all")

    print('finised '+str(round(100.0*(n-start+step)/(stop-start+step),4))+'%')
