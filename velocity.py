import numpy as np
import pylab as plt
from scipy import stats
from scipy.stats import norm

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
vz = data[:,5]
#============================================================


# V space 

#============================================================
#scatter plots to see data.....
#============================================================
print("Plotting a scatter plot ")
plt.scatter(vx,vy,s=0.5,alpha=0.05)
plt.xlabel("v_x")
plt.ylabel("v_y")
plt.title("scatter plot")
plt.show()
print("The max value of vx is :", max(vx))
print("The min value of vx is :", min(vx))
print("The number of data in vx is :", len(vx))
#===================================================
#histogram plots to see data.....
#============================================================
#the built-in histogram, (not normalised!)
plt.hist(vx,bins=100,alpha=0.2,color="g",label="Histogram of vx")
plt.title("Histogram of vx")
plt.legend()
plt.show()
#============================================================
#plotting the pdf from normalised histogram
#============================================================
print("Plotting the  pdf for vx from np.histogram")
bins = np.linspace(-1,1,100)
histogram, bins = np.histogram(vx, bins=bins, density=True)
#calculating the centers of each bin
bin_centers = 0.5*(bins[1:] + bins[:-1])

plt.plot(bin_centers, histogram, '.', label="the pdf of vx, from np.histogram") #this is the theoretical pdf of data
plt.legend()
plt.show()
#============================================================



#Constructing the manual pdf of vxdata
#============================================================
#doing the first iteration, for the first bin...
#============================================================
print(" ")
print("   *   to see the pdf for vx, doing the first iteration...     ")
print(" ")
print(" ")
#creating the bin edges (how many bins we want??)
vi = np.linspace(min(vx), max(vx),100)
print("the bin edges are :", vi)
print("the length of vi is: ", len(vi))
print(" ")
#=============================================================
#find the number of counts between the i and i+1 bin in vi
#==============================================================
#find the centres of each bin (the length should be one less from the bin edges)
centers = 0.5*(vi[1:] + vi[:-1])
print("the centers are :", centers)
print("the length of centers is: ", len(centers))
print(" ")

a = np.where((vx > vi[0]) & (vx < vi[1])) #creating the array index 
#where we find the index, for when the data is between the specified width
print("the index array is :", a)
print(" ")

dN = len(a[0]) #how many are there within this width
print("the count within the width is :", dN)
print(" ")
#===========================================================

dr = vi[1] - vi[0] #width of the bin 
print("the dr is :", dr)
print(" ")

dndr = (dN/dr)
fac = (len(vi)) #* (4*np.pi*centers[0]**2)
v = dndr* (1/fac)

print("the normalised number density is :", v)
print(" ")

print(" ")
print("   * starting the loop ......to compute over all centres..     ")
print(" ")
print(" ")
#loop skeleton======================================================

#construct pdf array to fill
pdf_vx = np.zeros(len(vi) -1)

for i in range(len(vi) - 1):
  a = np.where((vx > vi[i]) & (vx < vi[i+1]))
  print("the index array is :", a)

  dN = len(a[0])
  print("the dN is :", dN)

  dr = vi[i+1] - vi[i]
  print("the dr is :", dr)

  dndr = (dN/dr)
  fac = (len(vx)) #* (4*np.pi*centers[i]**2)
  v = dndr* (1/fac)
  print("the v is :", v)

  pdf_vx[i] = v 
#======================================================================

plt.plot(bin_centers, histogram, '.', label="the pdf of vx, from np.histogram") 
plt.scatter(centers,pdf_vx,s=0.5,label="manual pdf") #the manually calculated pdf
plt.xlabel("vi (bins)")
plt.ylabel("pdf for vx")
plt.legend()
plt.title("The pdf for vx")
plt.show()

r = np.sqrt(x**2 + y**2 + z**2)

print(" ")
print("    *     Calculating the velocity dispersions  ") 
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

#============================================================
#============================================================




























