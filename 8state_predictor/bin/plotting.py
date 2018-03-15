import matplotlib.pyplot as plt
import numpy as np
filename = open('../results/testing_results/decisiontree_crossvalidation.txt','r')
emptylist = []
Min_samples_split = []
WINDOWS = []
CV = []
DEVIATION = []
for lines in filename:
    emptylist.append(lines.split())
for lines in (emptylist[0::4]):
    #print (lines)
    Min_samples_split.append(lines[1])
#print(Min_samples_split)
for lines in (emptylist[1::4]):

    WINDOWS.append(lines[2])
#print(WINDOWS)

for lines in (emptylist[2::4]):

    CV.append(lines[2])
#print(CV)
    
for lines in (emptylist[3::4]):

    DEVIATION.append(lines[2])
#print(DEVIATION)
filename.close()

#print(Min_samples_split, WINDOWS, CV, DEVIATION)
results_cv1 = list(map(float, CV[0:9]))
results_dev1 = list(map(float, DEVIATION[0:9]))
results_win1 = list(map(int, WINDOWS[0:9]))

results_cv2 = list(map(float, CV[9:18]))
results_dev2 = list(map(float, DEVIATION[9:18]))
results_win2 = list(map(int, WINDOWS[9:18]))

results_cv3 = list(map(float, CV[18:27]))
results_dev3 = list(map(float, DEVIATION[18:27]))
results_win3 = list(map(int, WINDOWS[18:27]))

results_cv4 = list(map(float, CV[27:36]))
results_dev4 = list(map(float, DEVIATION[27:36]))
results_win4 = list(map(int, WINDOWS[27:36]))

results_cv5 = list(map(float, CV[36:45]))
results_dev5 = list(map(float, DEVIATION[36:45]))
results_win5 = list(map(int, WINDOWS[36:45]))

results_cv6 = list(map(float, CV[45:54]))
results_dev6 = list(map(float, DEVIATION[45:54]))
results_win6 = list(map(int, WINDOWS[45:54]))

results_cv7 = list(map(float, CV[54:63]))
results_dev7 = list(map(float, DEVIATION[54:63]))
results_win7 = list(map(int, WINDOWS[54:63]))

results_cv8 = list(map(float, CV[63:72]))
results_dev8 = list(map(float, DEVIATION[63:72]))
results_win8 = list(map(int, WINDOWS[63:72]))

results_cv9 = list(map(float, CV[72:81]))
results_dev9 = list(map(float, DEVIATION[72:81]))
results_win9 = list(map(int, WINDOWS[72:81]))

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

line1 = ax.errorbar(results_win1, results_cv1, yerr=results_dev1, capsize=4, label='Min_samples_split 2', linestyle = '--')
line2 = ax.errorbar(results_win2, results_cv2, yerr=results_dev2, capsize=4, label='Min_samples_split 3', linestyle = '-.')
line1 = ax.errorbar(results_win3, results_cv3, yerr=results_dev3, capsize=4, label='Min_samples_split 4', linestyle = ':')
line1 = ax.errorbar(results_win4, results_cv4, yerr=results_dev4, capsize=4, label='Min_samples_split 5')
line1 = ax.errorbar(results_win5, results_cv5, yerr=results_dev5, capsize=4, label='Min_samples_split 6')
line1 = ax.errorbar(results_win6, results_cv6, yerr=results_dev6, capsize=4, label='Min_samples_split 7')
line1 = ax.errorbar(results_win7, results_cv7, yerr=results_dev7, capsize=4, label='Min_samples_split 8')
line1 = ax.errorbar(results_win8, results_cv8, yerr=results_dev8, capsize=4, label='Min_samples_split 9')
line1 = ax.errorbar(results_win9, results_cv9, yerr=results_dev9, capsize=4, label='Min_samples_split 10')

#ax.set_xticks(x)
ax.set_title("Decision trees cross-validation scores according to window length")
ax.set_ylim(0.30, 0.50)
ax.set_xlabel("Window Size")
ax.set_ylabel("CV score")
ax.legend(loc='upper right')
plt.show()

