import pyPLUTO as pp
import numpy as np

D = pp.Load()

# Open the kh.dat file and store the variables
analysis = D.read_file("kh.dat")

# Calculate growth rate
sigma=np.gradient(np.log(analysis["vy2"]))*0.5
print("min=", np.min(sigma))

sumpos=0
posno=0
sum=0
for i in sigma:
  if i>0:
    sumpos+=i
    posno+=1
  sum+=i

print("Average of positives=", sumpos/posno)
print("Total average=", sum/len(sigma))
