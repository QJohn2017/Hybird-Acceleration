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
px_y = np.loadtxt(directory+'px2d.txt')
py_y = np.loadtxt(directory+'py2d.txt')
xx_y = np.loadtxt(directory+'xx2d.txt')
yy_y = np.loadtxt(directory+'yy2d.txt')
workx2d_y = np.loadtxt(directory+'workx2d.txt')
worky2d_y = np.loadtxt(directory+'worky2d.txt')
fieldex_y = np.loadtxt(directory+'fieldex2d.txt')
fieldey_y = np.loadtxt(directory+'fieldey2d.txt')
fieldbz_y = np.loadtxt(directory+'fieldbz2d.txt')
gg_y = (px_y**2+py_y**2+1)**0.5
R_y  = gg_y-px_y


directory = './txt_new/'
px_x = np.loadtxt(directory+'px2d.txt')
py_x = np.loadtxt(directory+'py2d.txt')
xx_x = np.loadtxt(directory+'xx2d.txt')
yy_x = np.loadtxt(directory+'yy2d.txt')
workx2d_x = np.loadtxt(directory+'workx2d.txt')
worky2d_x = np.loadtxt(directory+'worky2d.txt')
fieldex_x = np.loadtxt(directory+'fieldex2d.txt')
fieldey_x = np.loadtxt(directory+'fieldey2d.txt')
fieldbz_x = np.loadtxt(directory+'fieldbz2d.txt')
gg_x = (px_x**2+py_x**2+1)**0.5
R_x  = gg_x-px_x


color_y = np.zeros_like(R_y[:,0])
color_x = np.zeros_like(R_x[:,0])

phi_x = np.zeros_like(gg_x[:,0])

inject_px = np.zeros_like(gg_x[:,0]) 
inject_py = np.zeros_like(gg_x[:,0]) 
inject_x  = np.zeros_like(gg_x[:,0])
inject_y  = np.zeros_like(gg_x[:,0])




for i in range(0,color_x.size):
   phi_xi = (np.linspace(5.0,49.9,450)-xx_x[i,:])%1.0
   # color_x[i] = R_x[i,np.argmax( (abs(yy_x[i,:])>-0.16*xx_x[i,:]+4.0) & (abs(yy_x[i,:])<3.2)  )]
   # inject_px[i] = px_x[i,np.argmax( (abs(yy_x[i,:])>-0.16*xx_x[i,:]+4.0) & (abs(yy_x[i,:])<3.2)  )]
   # inject_py[i] = py_x[i,np.argmax( (abs(yy_x[i,:])>-0.16*xx_x[i,:]+4.0) & (abs(yy_x[i,:])<3.2)  )]
   # inject_x[i]  = xx_x[i,np.argmax( (abs(yy_x[i,:])>-0.16*xx_x[i,:]+4.0) & (abs(yy_x[i,:])<3.2)  )] 
   # inject_y[i]  = yy_x[i,np.argmax( (abs(yy_x[i,:])>-0.16*xx_x[i,:]+4.0) & (abs(yy_x[i,:])<3.2)  )] 
   if yy_x[i,0] > 0:
       #color_x[i] = phi_x[i,np.argmax( yy_x[i,:]<0  )]
       phi_x[i] = phi_xi[np.argmax( yy_x[i,:]<0  )]
       inject_px[i] = px_x[i,np.argmax( yy_x[i,:]<0  )]
       inject_py[i] = py_x[i,np.argmax( yy_x[i,:]<0  )]
       inject_x[i]  = xx_x[i,np.argmax( yy_x[i,:]<0  )]
       inject_y[i]  = yy_x[i,np.argmax( yy_x[i,:]<0  )]
   elif yy_x[i,0] <  0:
       #color_x[i] = phi_x[i,np.argmax( yy_x[i,:]<0  )]
       phi_x[i] = phi_xi[np.argmax( yy_x[i,:]>0  )]
       inject_px[i] = px_x[i,np.argmax( yy_x[i,:]>0  )]
       inject_py[i] = py_x[i,np.argmax( yy_x[i,:]>0  )]
       inject_x[i]  = xx_x[i,np.argmax( yy_x[i,:]>0  )]
       inject_y[i]  = yy_x[i,np.argmax( yy_x[i,:]>0  )]

   
inject_gg = (inject_px**2+inject_py**2+1.0)**0.5

print(color_y)

plt.scatter(inject_px, inject_py, c=phi_x, norm=colors.Normalize(vmin=0, vmax=1), s=20, cmap='rainbow', edgecolors='black', alpha=0.4)
cbar=plt.colorbar()
cbar.set_label(r'$\phi\ [2\pi]$ for injecting time',fontdict=font)
#   plt.legend(loc='upper right')
#    plt.xlim(-200,600)
#    plt.ylim(-200,600)
plt.xlabel(r'$p_x [m_ec]$',fontdict=font)
plt.ylabel(r'$p_y [m_ec]$',fontdict=font)
#plt.xticks(fontsize=20); plt.yticks(fontsize=20);
#plt.title('electron at y='+str(round(y[n,0]/2/np.pi,4)),fontdict=font)
#plt.show()
#lt.figure(figsize=(100,100))
fig = plt.gcf()
fig.set_size_inches(8, 6.5)
fig.savefig('./inject_cross_px_py.png',format='png',dpi=160)
plt.close("all")

plt.scatter(inject_x, inject_y, c=phi_x, norm=colors.Normalize(vmin=0, vmax=1), s=20, cmap='rainbow', edgecolors='black', alpha=0.4)
cbar=plt.colorbar()
cbar.set_label(r'$x$-$y$ for injecting time',fontdict=font)
#   plt.legend(loc='upper right')
#    plt.xlim(-200,600)
#    plt.ylim(-200,600)
plt.xlabel(r'$x [\lambda_0]$',fontdict=font)
plt.ylabel(r'$y [\lambda_0]$',fontdict=font)
me/michael/conductor/jpg_new/inject_comb0452.png' 
#plt.xticks(fontsize=20); plt.yticks(fontsize=20);
#plt.title('electron at y='+str(round(y[n,0]/2/np.pi,4)),fontdict=font)
#plt.show()
#lt.figure(figsize=(100,100))
fig = plt.gcf()
fig.set_size_inches(8, 6.5)
fig.savefig('./inject_cross_x_y.png',format='png',dpi=160)
