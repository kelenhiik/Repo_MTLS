import matplotlib.pyplot as plt
import numpy as np
filename = open('../results/testing_results/RFC_crossvalidation_PSSM.txt','r')
emptylist = []
nestimators = []
minsplit = []
WINDOWS = []
CV = []
DEVIATION = []
for lines in filename:
    emptylist.append(lines.split())
for lines in (emptylist[0::5]):
    #print (lines)
    nestimators.append(lines[1])
#print(nestimators[189:252])###############300
#print(nestimators[252:315])##################350

for lines in (emptylist[1::5]):
    #print(lines)
    WINDOWS.append(lines[2])
#print(WINDOWS[189:252])############9 of 7, go in sevens

for lines in (emptylist[2::5]):
    #print(lines)
    minsplit.append(lines[1])
#print(minsplit[189:252])############7 of 9s


for lines in (emptylist[3::5]):
    #print(lines)
    CV.append(lines[2])
#print(CV)

for lines in (emptylist[4::5]):
    #print(lines)
    DEVIATION.append(lines[2])
#print(DEVIATION)

filename.close()



results_cv1 = list(map(float, CV[252:259]))
results_dev1 = list(map(float, DEVIATION[252:259]))
results_win1 = list(map(int, minsplit[252:259]))
#print(minsplit[189:196]) #2345678
#print(WINDOWS[189:196]) #55555555
#print (CV[189:196])
results_cv2 = list(map(float, CV[259:266]))
results_dev2 = list(map(float, DEVIATION[259:266]))
results_win2 = list(map(int, minsplit[259:266]))
#print(minsplit[259:266])#2345678
#print(WINDOWS[259:266])#7777777
#print(CV[196:203])

results_cv3 = list(map(float, CV[266:273]))
results_dev3 = list(map(float, DEVIATION[266:273]))
results_win3 = list(map(int, minsplit[266:273]))
#print(results_cv3,results_win3)
#9
results_cv4 = list(map(float, CV[273:280]))
results_dev4 = list(map(float, DEVIATION[273:280]))
results_win4 = list(map(int, minsplit[273:280]))
#print(results_cv4,results_win4)
#11

results_cv5 = list(map(float, CV[280:287]))
results_dev5 = list(map(float, DEVIATION[280:287]))
results_win5 = list(map(int, minsplit[280:287]))
#13
#print(results_cv5,results_win5)

results_cv6 = list(map(float, CV[287:294]))
results_dev6 = list(map(float, DEVIATION[287:294]))
results_win6 = list(map(int, minsplit[287:294]))
#15
#print(results_cv6,results_win6)
results_cv7 = list(map(float, CV[294:301]))
results_dev7 = list(map(float, DEVIATION[294:301]))
results_win7 = list(map(int, minsplit[294:301]))
#print(results_cv7,results_win7)
#print(results_cv7,results_win7)
#17
results_cv8 = list(map(float, CV[301:308]))
results_dev8 = list(map(float, DEVIATION[301:308]))
results_win8 = list(map(int, minsplit[301:308]))
#19
#print(results_cv8,results_win8)

results_cv9 = list(map(float, CV[308:315]))
results_dev9 = list(map(float, DEVIATION[308:315]))
results_win9 = list(map(int, minsplit[308:315]))
#21
#print(results_cv9,results_win9)

#print(results_cv9,results_win9)
#plt.figure()
#plt.title("Decision trees cross-validation scores according to window length with a min_samples_split " + str(Min_samples_split[0]) )
#plt.xlabel("Window Size")
#plt.ylabel("CV score")
#plt.xticks(np.arange(20))

#plt.plot(WINDOWS[0:9], CV[0:9] , 'o-', label='mean')
plt.show()

fig, ax = plt.subplots()
#print(CV[0:9])
#print(DEVIATION[0:9])

line1 = ax.errorbar(results_win1, results_cv1, yerr=results_dev1, capsize=4, label='Window size: 5', linestyle = '--')
line2 = ax.errorbar(results_win2, results_cv2, yerr=results_dev2, capsize=4, label='Window size: 7', linestyle = '-.')
line1 = ax.errorbar(results_win3, results_cv3, yerr=results_dev3, capsize=4, label='Window size: 9', linestyle = ':')
line1 = ax.errorbar(results_win4, results_cv4, yerr=results_dev4, capsize=4, label='Window size: 11')
line1 = ax.errorbar(results_win5, results_cv5, yerr=results_dev5, capsize=4, label='Window size: 13')
line1 = ax.errorbar(results_win6, results_cv6, yerr=results_dev6, capsize=4, label='Window size: 15')
line1 = ax.errorbar(results_win7, results_cv7, yerr=results_dev7, capsize=4, label='Window size: 17')


line1 = ax.errorbar(results_win8, results_cv8, yerr=results_dev8, capsize=4, label='Window size: 19')
line1 = ax.errorbar(results_win9, results_cv9, yerr=results_dev9, capsize=4, label='Window size: 21')

#ax.set_xticks(x)
ax.set_title("RFC cross-validation PSFM. N-estimators: 350.")
ax.set_ylim(0.56, 0.65)
ax.set_xlim(1.95, 9)
ax.set_xlabel("The minimum number of samples needed for splitting.")
ax.set_ylabel("CV score")
ax.legend(loc='upper right')
plt.show()

