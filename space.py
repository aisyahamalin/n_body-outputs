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

#X, Y, Z space ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#============================================================
#scatter plots to see data.....
#============================================================
print("Plotting a scatter plot ")
plt.scatter(x,y,s=0.5,alpha=0.05)
plt.xlabel("x")
plt.ylabel("y")
plt.title("scatter plot")
plt.show()
plt.scatter(x,z,s=0.5,alpha=0.05)
plt.xlabel("x")
plt.ylabel("z")
plt.title("scatter plot")
plt.show()
plt.scatter(y,z,s=0.5,alpha=0.05)
plt.xlabel("y")
plt.ylabel("z")
plt.title("scatter plot")
plt.show()
print("The max value of x is :", max(x))
print("The min value of x is :", min(x))
#============================================================
#histogram and pdf plots to see data.....
#============================================================
#the actual histogram, (not normalised!)
plt.hist(x,bins=100,alpha=0.2,color="g",label="Histogram of x")
plt.hist(y,bins=100,alpha=0.5,color="r",label="Histogram of y")
plt.hist(z,bins=100,alpha=0.3,color="m",label="Histogram of z")
plt.title("Histograms of x,y,z")
plt.legend()
plt.show()
#============================================================
#plotting the pdf from normalised histogram
#============================================================
print("Plotting the pdf for x using np.histogram")
bins = np.linspace(-30,30,100)
histogram, bins = np.histogram(x, bins=bins, density=True)
#calculating the centers of each bin
bin_centers = 0.5*(bins[1:] + bins[:-1])
plt.plot(bin_centers, histogram, '.', label="the pdf of x, derived from np.histogram") #this is the pdf of data
plt.legend()
plt.show()
#============================================================


# R space ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print(" ")
print("   *  radius r data manipulation ")
print(" ")
#============================================================
#defining the radius
#============================================================
rdata = np.sqrt(x**2+y**2+z**2)
print("The radius r is: ", rdata)
print("The number of data in r is :", len(rdata))
print("The max value of r is :", max(rdata))
print("The min value of r is :", min(rdata))
#============================================================
#============================================================
#basic histogram plot to see radius data counts
#============================================================
print("Plotting a basic histogram for r, to see the counts")
plt.hist(rdata,bins=100)
plt.xlabel("Ri' (bins) [r' [units of: r/a]]")
plt.ylabel("counts")
plt.title("The histogram for rdata")
plt.show()
#============================================================


#============================================================
#============================================================
#Constructing a 'manual' pdf of rdata, using its underlying histogram
#============================================================
#============================================================

#doing the first iteration, for the first bin...
#============================================================
print(" ")
print("   *   to see the pdf for radius, doing the first iteration...     ")
print(" ")
print(" ")
#creating the bin edges (how many bins we want??)
ri = np.linspace(min(rdata), max(rdata),100)
print("the bin edges are :", ri)
print("the length of ri is: ", len(ri))
print(" ")
#=============================================================
#find the number of stars between the i and i+1 bin in ri
#==============================================================
#find the centres of each bin (the length should be one less from the bin edges)
centers = 0.5*(ri[1:] + ri[:-1])
print("the centers are :", centers)
print("the length of centers is: ", len(centers))
print(" ")

a = np.where((rdata > ri[0]) & (rdata < ri[1])) #creating the array index 
#where we find the index, for when the data is between the specified width
print("the index array is :", a)
print(" ")

dN = len(a[0]) #how many are there within this width
print("the count within the width is :", dN)
print(" ")
#===========================================================

dr = ri[1] - ri[0] #width of the bin 
print("the dr is :", dr)
print(" ")

dndr = (dN/dr)
fac = (len(rdata)) * (4*np.pi*centers[0]**2)
v = dndr* (1/fac)

print("the normalised number density is :", v)
print(" ")

print(" ")
print("   * starting the loop ......to compute over all centres..     ")
print(" ")
print(" ")
#loop skeleton======================================================

#construct pdf array to fill
pdf_r = np.zeros(len(ri) -1)

for i in range(len(ri) - 1):
  a = np.where((rdata > ri[i]) & (rdata < ri[i+1]))
  print("the index array is :", a)

  dN = len(a[0])
  print("the dN is :", dN)

  dr = ri[i+1] - ri[i]
  print("the dr is :", dr)

  dndr = (dN/dr)
  fac = (len(rdata)) * (4*np.pi*centers[i]**2)
  v = dndr* (1/fac)
  print("the v is :", v)

  pdf_r[i] = v 
#======================================================================
#print("the pdf is :", pdf_r)
print("the pdf shape is:", pdf_r.shape)
#print("the pdf type is :", type(pdf_r))
#print("the centers are: ", centers)
print("the centers.shape :", centers.shape)
#print("the centers type is :", type(centers))

plt.plot(centers,pdf_r)
plt.xlabel("Ri (bins)[r' [units of: r/a]]")
plt.ylabel("pdf [per bin^3")
plt.title("The 'manual' pdf for rdata")
plt.show()

#The pdf from np.histogram
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
print("Plotting the pdf for r")
bins_theo = np.linspace(min(rdata), max(rdata),100)
histogram, bins_theo = np.histogram(rdata, bins=bins_theo, density=True)

#calculating the centers of each bin
bin_centers_theo = 0.5*(bins_theo[1:] + bins_theo[:-1])
histogram = histogram/(4*np.pi*bin_centers_theo**2) #cuz the built-in doesn't have the 4pi*r**2 factor!!!
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

plt.plot(centers,pdf_r,color='r',label="manual pdf")
plt.plot(bin_centers_theo, histogram, label="pdf from np.histogram") #this is the pdf of data using the built-in package
plt.legend()
plt.show()

#==================================================================
#NOTE: so far have calculate the pdf (via 2 methods)
#Mow to compare to the hernquist density profile!
#=================================================================
print(" ")
print("  *    Plotting the theoretical Hernquist density profile " )


#what is the actual total mass? taken as a unit, i.e. @Rmax, will have a mass of 1.
M_tot = 1.

#function for Hernquist density profile (the analytical solution)
def rho(r) :   return r**(-g)/(2*np.pi) * (1. + r**a )**((g-b)/a)  
a = 1.0
b = 4.0
g = 1.0

rho_r = rho(centers)

plt.plot(centers,pdf_r,color='r',label="pdf")

plt.plot(centers,rho_r,color='b',label="Hernquist density profile")

plt.yscale("log")
plt.xscale("log")
plt.xlabel("log Ri' / log (r/a)")
plt.ylabel("log (pdf or rho) ")
plt.legend()
plt.show()



