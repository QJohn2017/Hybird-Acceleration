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
import matplotlib.colors as mcolors 

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
start   =  50  # start time
stop    =  499  # end time
step    =  1  # the interval or step

to_path = './jpg_new/'


directory = './txt_new/'
px = np.loadtxt(directory+'px2d.txt')
py = np.loadtxt(directory+'py2d.txt')
xx = np.loadtxt(directory+'xx2d.txt')
yy = np.loadtxt(directory+'yy2d.txt')
workx2d = np.loadtxt(directory+'workx2d.txt')
worky2d = np.loadtxt(directory+'worky2d.txt')
fieldex = np.loadtxt(directory+'fieldex2d.txt')
fieldey = np.loadtxt(directory+'fieldey2d.txt')
fieldbz = np.loadtxt(directory+'fieldbz2d.txt')
gg = (px**2+py**2+1)**0.5
R  = gg-px

theta = np.arctan2(py,px)*180.0/np.pi


inject_color = np.zeros_like(gg[:,0])

for i in range(0,inject_color.size):
     inject_color[i] = R[i,np.argmax( (xx[i,:]>5.0) & (abs(yy[i,:])<3.2)  )]

for n in range(start,stop+step,step):
    range_max=3.0
    range_min=0.3

    plt.subplot(2,3,1)
    plt.scatter(xx[:,n-start], yy[:,n-start], c=inject_color, norm=colors.LogNorm(vmin=range_min, vmax=range_max), s=20, cmap='rainbow', edgecolors='None', alpha=0.6)
    cbar=plt.colorbar()
    cbar.set_label(r'$R$',fontdict=font)
    #   plt.legend(loc='upper right')
    plt.xlim(3,18)
    plt.ylim(-6.5,6.5)
    plt.xlabel(r'$x\ [\lambda_0]$',fontdict=font)
    plt.ylabel(r'$y\ [\lambda_0]$',fontdict=font)
    #plt.xticks(fontsize=20); plt.yticks(fontsize=20);
    #plt.title('electron at y='+str(round(y[n,0]/2/np.pi,4)),fontdict=font)

    plt.subplot(2,3,2)
    plt.scatter(px[:,n-start], py[:,n-start], c=inject_color, norm=colors.LogNorm(vmin=range_min, vmax=range_max), s=20, cmap='rainbow', edgecolors='None', alpha=0.6)
    cbar=plt.colorbar()
    cbar.set_label(r'$R$',fontdict=font)
    #   plt.legend(loc='upper right')
    plt.xlim(-10,350)
    plt.ylim(-35,35)
    plt.xlabel(r'$p_x [m_ec]$',fontdict=font)
    plt.ylabel(r'$p_y [m_ec]$',fontdict=font)
    #plt.xticks(fontsize=20); plt.yticks(fontsize=20);
    #plt.title('electron at y='+str(round(y[n,0]/2/np.pi,4)),fontdict=font)

    plt.subplot(2,3,3)
    plt.scatter(workx2d[:,n-start], worky2d[:,n-start], c=inject_color, norm=colors.LogNorm(vmin=range_min, vmax=range_max), s=20, cmap='rainbow', edgecolors='None', alpha=0.6)
    cbar=plt.colorbar()
    cbar.set_label(r'$R$',fontdict=font)
    #   plt.legend(loc='upper right')
    plt.xlim(-200,350)
    plt.ylim(-200,350)
    plt.xlabel(r'$work_x$',fontdict=font)
    plt.ylabel(r'$work_y$',fontdict=font)
    #plt.xticks(fontsize=20); plt.yticks(fontsize=20);
    #plt.title('electron at y='+str(round(y[n,0]/2/np.pi,4)),fontdict=font)

    plt.subplot(2,3,4)
    plt.scatter(n*0.1-xx[:,n-start], py[:,n-start], c=inject_color, norm=colors.LogNorm(vmin=range_min, vmax=range_max), s=20, cmap='rainbow', edgecolors='None', alpha=0.6)
    cbar=plt.colorbar()
    cbar.set_label(r'$R$',fontdict=font)
    #   plt.legend(loc='upper right')
    plt.xlim(0,5)
    plt.ylim(-40,40)
    plt.xlabel(r'$\phi\ [2\pi]$',fontdict=font)
    plt.ylabel(r'$p_y\ [m_ec]$',fontdict=font)
    #plt.xticks(fontsize=20); plt.yticks(fontsize=20);
    #plt.title('electron at y='+str(round(y[n,0]/2/np.pi,4)),fontdict=font)

    plt.subplot(2,3,5)
    plt.scatter(theta[:,n-start], gg[:,n-start], c=inject_color, norm=colors.LogNorm(vmin=range_min, vmax=range_max), s=20, cmap='rainbow', edgecolors='None', alpha=0.6)
    cbar=plt.colorbar()
    cbar.set_label(r'$R$',fontdict=font)
    #   plt.legend(loc='upper right')
    plt.xlim(-30,30)
    plt.ylim(0,350)
    plt.xlabel(r'$\theta\ [degree]$',fontdict=font)
    plt.ylabel(r'$\gamma$',fontdict=font)
    #plt.xticks(fontsize=20); plt.yticks(fontsize=20);
    #plt.title('electron at y='+str(round(y[n,0]/2/np.pi,4)),fontdict=font)

    plt.subplot(2,3,6)
    plt.scatter(n*0.1-xx[:,n-start], px[:,n-start], c=inject_color, norm=colors.LogNorm(vmin=range_min, vmax=range_max), s=20, cmap='rainbow', edgecolors='None', alpha=0.6)
    cbar=plt.colorbar()
    cbar.set_label(r'$R$',fontdict=font)
    #   plt.legend(loc='upper right')
    plt.xlim(0,5)
    plt.ylim(0,350)
    plt.xlabel(r'$\phi\ [2\pi]$',fontdict=font)
    plt.ylabel(r'$p_x\ [m_ec]$',fontdict=font)
    #plt.xticks(fontsize=20); plt.yticks(fontsize=20);
    #plt.title('electron at y='+str(round(y[n,0]/2/np.pi,4)),fontdict=font)




    fig = plt.gcf()
    fig.set_size_inches(30, 17)
    fig.savefig(to_path+'inject_comb'+str(n).zfill(4)+'.png',format='png',dpi=80)
    plt.close("all")
    
    print('finised '+str(round(100.0*(n-start+step)/(stop-start+step),4))+'%')

