import numpy as np
import matplotlib.pyplot as plt
import statistics
from statistics import mode

absorbtionArr = [4380, 4500, 4900,5900,6000,6700,8900]
knownArr = [3524,3815, 3820,3825,3832, 3838,3934,3968,4308,4227,4340,4861,5167, 5172, 5183,5890, 5896,6563]

#guess a line is a known
#put into redshift
#add one, mult by a known, see if it equals an absorption
r=50
results = []
Zresults = []

for i in range(len(absorbtionArr)):
    for j in range(len(knownArr)):
        z = (absorbtionArr[i] - knownArr[j])/knownArr[j]
        zMult = 1+z
        #We've found the redshift, now let's apply it
        for k in range(len(knownArr)):
            for l in range(len(absorbtionArr)):
                if np.absolute((zMult * knownArr[k]) - absorbtionArr[l]) < r and k!=j and l!=i:
                    results.append([absorbtionArr[i],knownArr[j],z])
                    Zresults.append(round(z,3))

uniqZesults = list(set(Zresults))

# for i in range(len(results)):
#     print(results[i])

# for i in range(len(Zresults)):
#     print(Zresults[i])

resultsRange = max(Zresults) - min(Zresults)
binAmount = int(np.ceil(resultsRange/0.05))
# print(binAmount)


plt.hist(x=Zresults, bins=binAmount)


# print(uniqZesults)

# for i in range(len(Zresults)):
#     print(Zresults[i])

print(mode(Zresults))
plt.title("Redshift guess successes")
plt.xlabel("Redshift (z)")
plt.ylabel("Number of results")

# print("hi")

# for i in range(len(Zresults)):
#     k = np.absolute(0.38-Zresults[i])
#     k=round(k,2)
#     print(k)

# for i in range(len(Zresults)):
#     k = np.absolute(0.38-Zresults[i])
#     print(k)

#z=0.138


plt.show()