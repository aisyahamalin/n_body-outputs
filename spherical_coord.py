import numpy as np
import pylab as plt
# from scipy import stats
# from scipy.stats import norm

#============================================================
#the file is saved as an .npy file, use 'load' to access
#============================================================
data = np.load('model(3maglower).npy')
print("The data is: ", data)
print("The data shape is: ", data.shape)

print(" converting each column to an array ")
x = data[:,0]
y = data[:,1]
z = data[:,2]
vx = data[:,3]
vy = data[:,4]
vz = data[:,5] #note: these are arrays of values, not vectors
#============================================================

#we don't actualy need this for transformation below
vvec = np.array([vx,vy,vz]).T #transposed so we have 3 column for vx : vy : vz

#the phase space in spherical coordinates
r = np.sqrt(x**2 + y**2 + z**2)
theta = np.arccos(z/r)
phi = np.arctan(y/x)

#the velocity space in spherical coordinates
vr      = vx * np.sin(theta)*np.cos(phi) + \
          vy * np.sin(theta)*np.sin(phi) + \
          vz * np.cos(theta)
          
vtheta      = vx * np.cos(theta)*np.cos(phi) + \
              vy * np.cos(theta)*np.sin(phi) - \
              vz * np.sin(theta)
              
vphi        = - vx * np.sin(phi) + \
                vy * np.cos(phi)


fig,ax = plt.subplots(4)

#plotting all 3 in one ax 
ax[0].hist(vr, bins=100, color="red",alpha=0.5, range=(-1.5,1.5))
ax[0].hist(vtheta, bins=100, color="green",alpha=0.5,range=(-1.5,1.5))
ax[0].hist(vphi, bins=100, color="blue",alpha=0.5,range=(-1.5,1.5))
ax[0].set_title("All Histograms")
#ax[0].set_xlim()
#ax[0].set_ylim()
ax[0].set_xlabel("v_i bins")
ax[0].set_ylabel("counts in v")

ax[1].hist(vr, bins=100, color="red",alpha=0.5, range=(-1.5,1.5))
ax[1].set_title("vr histogram")

ax[2].hist(vtheta, bins=100, color="green",alpha=0.5,range=(-1.5,1.5))
ax[2].set_title("vtheta histogram")

ax[3].hist(vphi, bins=100, color="blue",alpha=0.5,range=(-1.5,1.5))
ax[3].set_title("vphi histogram")

plt.show()


print(" ")
print("    *     Calculating the velocity dispersions for CARTESIAN space  ") 
print(" ")
#============================================================
#============================================================
#to see the velocity width in vx .....
sum_vx  = sum(vx)
print("The total sum of values in vx is :", sum_vx) 

mean_vx = sum_vx / len(vx)
print("The mean vx is :", mean_vx) 

#creating a new array for {vx - mean_vx}
dum_vx = vx
dum_vx = dum_vx - mean_vx
dum_vx = dum_vx*dum_vx
print("The dummy vx is :", dum_vx) 
print("The length of dummy vx is :", len(dum_vx)) 

#summing over all dummy vx
tot_sum_dummy_vx_2 = sum(dum_vx)
print("The total sum of dummy vx is  :", tot_sum_dummy_vx_2) 

#calculating the \sigma
sd_x = ((1/len(vx)*tot_sum_dummy_vx_2))**(0.5)
print("The sd in the velocity_x is:  ", sd_x)
print(" ")
#============================================================
#============================================================
#to see the velocity width in vy .....
sum_vy  = sum(vy)
print("The total sum of values in vy is :", sum_vy) 

mean_vy = sum_vy / len(vy)
print("The mean vy is :", mean_vy) 

#creating a new array for {vy - mean_vy}
dum_vy = vy
dum_vy = dum_vy - mean_vy
dum_vy = dum_vy*dum_vy
print("The dummy vy is :", dum_vy) 
print("The length of dummy vy is :", len(dum_vy)) 

#summing over all dummy vy
tot_sum_dummy_vy_2 = sum(dum_vy)
print("The total sum of dummy vy is  :", tot_sum_dummy_vy_2) 

#calculating the \sigma
sd_y = ((1/len(vy)*tot_sum_dummy_vy_2))**(0.5)
print("The sd in the velocity_y is:  ", sd_y)
print(" ")
#============================================================
#============================================================
#to see the velocity width in vz .....
sum_vz  = sum(vz)
print("The total sum of values in vz is :", sum_vz) 

mean_vz = sum_vz / len(vz)
print("The mean vz is :", mean_vz) 

#creating a new array for {vz - mean_vz}
dum_vz = vz
dum_vz = dum_vz - mean_vz
dum_vz = dum_vz*dum_vz
print("The dummy vz is :", dum_vz) 
print("The length of dummy vz is :", len(dum_vz)) 

#summing over all dummy vx
tot_sum_dummy_vz_2 = sum(dum_vz)
print("The total sum of dummy vz is  :", tot_sum_dummy_vz_2) 

#calculating the \sigma
sd_z = ((1/len(vz)*tot_sum_dummy_vz_2))**(0.5)
print("The sd in the velocity_z is:  ", sd_z)
print(" ")
#==========================================================================
#==========================================================================

print(" ")
print("    *     Calculating the velocity dispersions for SPHERICAL space  ") 
print(" ")
#==========================================================================
#==========================================================================
#to see the velocity width in vr .....
sum_vr  = sum(vr)
print("The total sum of values in vr is :", sum_vr) 

mean_vr = sum_vr / len(vr)
print("The mean vr is :", mean_vr) 

#creating a new array for {vr - mean_vr}
dum_vr = vr
dum_vr = dum_vr - mean_vr
dum_vr = dum_vr*dum_vr
print("The dummy vr is :", dum_vr) 
print("The length of dummy vr is :", len(dum_vr)) 

#summing over all dummy vr
tot_sum_dummy_vr_2 = sum(dum_vr)
print("The total sum of dummy vr is  :", tot_sum_dummy_vr_2) 

#calculating the \sigma
sd_r = ((1/len(vr)*tot_sum_dummy_vr_2))**(0.5)
print("The sd in the velocity_r is:  ", sd_r)
print(" ")
#============================================================
#============================================================
#to see the velocity width in vtheta .....
sum_vtheta  = sum(vtheta)
print("The total sum of values in vtheta is :", sum_vtheta) 

mean_vtheta = sum_vtheta / len(vtheta)
print("The mean vtheta is :", mean_vtheta) 

#creating a new array for {vtheta - mean_vtheta}
dum_vtheta = vtheta
dum_vtheta = dum_vtheta - mean_vtheta
dum_vtheta = dum_vtheta*dum_vtheta
print("The dummy vtheta is :", dum_vtheta) 
print("The length of dummy vtheta is :", len(dum_vtheta)) 

#summing over all dummy vtheta
tot_sum_dummy_vtheta_2 = sum(dum_vtheta)
print("The total sum of dummy vtheta is  :", tot_sum_dummy_vtheta_2) 

#calculating the \sigma
sd_theta = ((1/len(vtheta)*tot_sum_dummy_vtheta_2))**(0.5)
print("The sd in the velocity_theta is:  ", sd_theta)
print(" ")
#============================================================
#============================================================
#to see the velocity width in vphi .....
sum_vphi  = sum(vphi)
print("The total sum of values in vphi is :", sum_vphi) 

mean_vphi = sum_vphi / len(vphi)
print("The mean vphi is :", mean_vphi) 

#creating a new array for {vphi - mean_vphi}
dum_vphi = vphi
dum_vphi = dum_vphi - mean_vphi
dum_vphi = dum_vphi*dum_vphi
print("The dummy vphi is :", dum_vphi) 
print("The length of dummy vphi is :", len(dum_vphi)) 

#summing over all dummy vphi
tot_sum_dummy_vphi_2 = sum(dum_vphi)
print("The total sum of dummy vphi is  :", tot_sum_dummy_vphi_2) 

#calculating the \sigma
sd_phi = ((1/len(vphi)*tot_sum_dummy_vphi_2))**(0.5)
print("The sd in the velocity_phi is:  ", sd_phi)
print(" ")
#============================================================
#============================================================



plt.scatter(r,vx,s=0.2)
plt.xlabel("radius r' [units of: r/a]")
plt.ylabel("vx")
plt.show()

plt.scatter(r,vr,s=0.2)
plt.xlabel("radius r' [units of: r/a]")
plt.ylabel("vr")
plt.show()

#the theoretical <v_r^2> (radial velocity dispersion)

# def sigma_vr(r) :
#     a = 1.
#     factor =  (12.*r*((r+a)**3)/(a**4))*(np.log((r+a)/r)) - ((r/(r+a))*(25. + 52.0*(r/a) + 42.*((r/a)**2) + 12.*((r/a)**3)))
#     return ((1./(12.*a))*factor)


# #
# vel_rad_disp = sigma_vr(centers)



























