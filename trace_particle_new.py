import sdf
#import matplotlib
#matplotlib.use('agg')
#import matplotlib.pyplot as plt
import numpy as np
#from numpy import ma
#from matplotlib import colors, ticker, cm
#from matplotlib.mlab import bivariate_normal
#from optparse import OptionParser
#import os
#from colour import Color

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
#print 'electric field unit: '+str(exunit)
#print 'magnetic field unit: '+str(bxunit)
#print 'density unit nc: '+str(denunit)

font = {'family' : 'monospace',  
        'color'  : 'black',  
    	'weight' : 'normal',  
        'size'   : 20,  
       }  


from_path='./Data_new/'
to_path='./txt_new/'

data = sdf.read(from_path+"0499.sdf",dict=True)
grid_x = data['Grid/Particles/subset_high_e/electron'].data[0]/wavelength
grid_y = data['Grid/Particles/subset_high_e/electron'].data[1]/wavelength
work_x = data['Particles/Time_Integrated_Work_x/subset_high_e/electron'].data
work_y = data['Particles/Time_Integrated_Work_y/subset_high_e/electron'].data
px = data['Particles/Px/subset_high_e/electron'].data/(m0*v0)
py = data['Particles/Py/subset_high_e/electron'].data/(m0*v0)
gg = (px**2+py**2+1)**0.5
part13_id = data['Particles/ID/subset_high_e/electron'].data
part13_id = part13_id[ (grid_x>20) & (grid_x<50) & (abs(grid_y) < 3.2) ]
print('part13_id size is ',part13_id.size,' max ',np.max(part13_id),' min ',np.min(part13_id))


data = sdf.read(from_path+"0050.sdf",dict=True)
grid_x = data['Grid/Particles/subset_high_e/electron'].data[0]/wavelength
part00_id = data['Particles/ID/subset_high_e/electron'].data
part00_id = part00_id[ ( grid_x>5 ) ]
part13_id = np.intersect1d(part00_id,part13_id)
print('after intersect 0000.sdf part_id size is ',part13_id.size,' max ',np.max(part13_id),' min ',np.min(part13_id))


######### Parameter you should set ###########
start   =  50  # start time
stop    =  499  # end time
step    =  1  # the interval or step

#  if (os.path.isdir('jpg') == False):
#    os.mkdir('jpg')
######### Script code drawing figure ################
for n in range(start,stop+step,step):
    #### header data ####
    data = sdf.read(from_path+str(n).zfill(4)+".sdf",dict=True)
    header=data['Header']
    time=header['time']
    if ( n==start ):
        part_id = data['Particles/ID/subset_high_e/electron'].data
    else:
        part_id = np.intersect1d(data['Particles/ID/subset_high_e/electron'].data, part_id)
    print('Particle_ID size is ',part_id.size,' max ',np.max(part_id),' min ',np.min(part_id))

part_id = np.intersect1d(part_id,part13_id)
print('After intersecting with 0013.sdf')
print('Particle_ID size is ',part_id.size,' max ',np.max(part_id),' min ',np.min(part_id))


######### Parameter you should set ###########
start   =  50  # start time
stop    =  499  # end time
step    =  1  # the interval or step

px_2d = np.zeros([part_id.size,stop-start+1])
py_2d = np.zeros([part_id.size,stop-start+1])
xx_2d = np.zeros([part_id.size,stop-start+1])
yy_2d = np.zeros([part_id.size,stop-start+1])
work_x_2d = np.zeros([part_id.size,stop-start+1])
work_y_2d = np.zeros([part_id.size,stop-start+1])
field_ex_2d = np.zeros([part_id.size,stop-start+1])
field_ey_2d = np.zeros([part_id.size,stop-start+1])
field_bz_2d = np.zeros([part_id.size,stop-start+1])
for n in range(start,stop+step,step):
    #### header data ####
    data = sdf.read(from_path+str(n).zfill(4)+".sdf",dict=True)
    px = data['Particles/Px/subset_high_e/electron'].data/(m0*v0)
    py = data['Particles/Py/subset_high_e/electron'].data/(m0*v0)
    grid_x = data['Grid/Particles/subset_high_e/electron'].data[0]/wavelength
    grid_y = data['Grid/Particles/subset_high_e/electron'].data[1]/wavelength
    work_x = data['Particles/Time_Integrated_Work_x/subset_high_e/electron'].data
    work_y = data['Particles/Time_Integrated_Work_y/subset_high_e/electron'].data
    temp_id = data['Particles/ID/subset_high_e/electron'].data
    field_ex = data['Particles/field_ex/subset_high_e/electron'].data/exunit
    field_ey = data['Particles/field_ey/subset_high_e/electron'].data/exunit
    field_bz = data['Particles/field_bz/subset_high_e/electron'].data/bxunit

    px = px[np.in1d(temp_id,part_id)]
    py = py[np.in1d(temp_id,part_id)]
    grid_x = grid_x[np.in1d(temp_id,part_id)]
    grid_y = grid_y[np.in1d(temp_id,part_id)]
    work_x = work_x[np.in1d(temp_id,part_id)]
    work_y = work_y[np.in1d(temp_id,part_id)]
    field_ex = field_ex[np.in1d(temp_id,part_id)]
    field_ey = field_ey[np.in1d(temp_id,part_id)]
    field_bz = field_bz[np.in1d(temp_id,part_id)]

    temp_id = temp_id[np.in1d(temp_id,part_id)]


    for ie in range(part_id.size):
        px_2d[ie,n-start] = px[temp_id==part_id[ie]]
        py_2d[ie,n-start] = py[temp_id==part_id[ie]]
        xx_2d[ie,n-start] = grid_x[temp_id==part_id[ie]]
        yy_2d[ie,n-start] = grid_y[temp_id==part_id[ie]]
        work_x_2d[ie,n-start] = work_x[temp_id==part_id[ie]]
        work_y_2d[ie,n-start] = work_y[temp_id==part_id[ie]]
        field_ex_2d[ie,n-start] = field_ex[temp_id==part_id[ie]]
        field_ey_2d[ie,n-start] = field_ey[temp_id==part_id[ie]]
        field_bz_2d[ie,n-start] = field_bz[temp_id==part_id[ie]]
    print('finised '+str(round(100.0*(n-start+step)/(stop-start+step),4))+'%')

np.savetxt(to_path+'px2d.txt',px_2d)
np.savetxt(to_path+'py2d.txt',py_2d)
np.savetxt(to_path+'xx2d.txt',xx_2d)
np.savetxt(to_path+'yy2d.txt',yy_2d)
np.savetxt(to_path+'workx2d.txt',work_x_2d)
np.savetxt(to_path+'worky2d.txt',work_y_2d)
np.savetxt(to_path+'fieldex2d.txt',field_ex_2d)
np.savetxt(to_path+'fieldey2d.txt',field_ey_2d)
np.savetxt(to_path+'fieldbz2d.txt',field_bz_2d)




