import pyPLUTO as pp
import numpy as np

D = pp.Load()

# Open the kh.dat file and store the variables
analysis = D.read_file("kh.dat")
logy = np.log(analysis["vy2"])
x=analysis["time"]
print("Original vy2", analysis["vy2"])
print(logy)
print(x)
# Select only the linear region
start=int(2.2/0.05)-1
end=int(5/0.05)-1

logy_fit = logy[start:end]
x_fit = x[start:end]

# Linear regression
m, c = np.polyfit(x_fit, logy_fit, 1)
print("Sigma=", m*0.5)

# Calculate growth rate
#sigma=np.gradient(np.log(analysis["vy2"]))*0.5
#print("min=", np.min(sigma))

#sumpos=0
#posno=0
#sum=0
#for i in sigma:
#  if i>0:
#    sumpos+=i
#    posno+=1
#  sum+=i

#print("Average of positives=", sumpos/posno)
#print("Total average=", sum/len(sigma))
