import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines  as lines
import subprocess
import glob, os

# simulation parameters
N0   = 1000
tau  = 0.666
dt   = 0.0001
tmax = 10 * tau

# number of runs
Ntimes = 42


# compile code
compiler = "gfortran"
flags = ["-Wall", "-Wextra", "-Wconversion-extra", "-std=f2003", "-pedantic", "-fimplicit-none", "-fbacktrace", "-O3", "-march=native"]
source = "2_decaimento.f90"
cmd = [compiler] + flags + [source]

print("Compiling {} with {} {}".format(source, compiler, flags))
bla = subprocess.run(cmd, check = True, stdout=subprocess.PIPE)

if bla.returncode != 0:
    print("Oh, shit")
    exit(1)

# run code
print("")
print("N0 = {}".format(N0))
print("tau = {}".format(tau))
print("dt = {}".format(dt))
print("tmax = {}".format(tmax), end = '\n\n')
print("Running code {} times:".format(Ntimes))
inp = str(N0) + " " + str(tau) + " " + str(dt) + " " + str(tmax)
for run in range(Ntimes):
    print("{}/{}\r".format(run, Ntimes), end = '')
    with open("out_{}".format(run), mode = 'w') as outfile:
        bla = subprocess.run(["./a.out"],
                             input = inp,
                             encoding ='ascii',
                             check = True,
                             stdout=outfile)
print("\n")
print("Plotting")

fig = plt.figure()
ax = fig.add_subplot(111)

X = []
Y = []

for data in glob.glob("out_*"):
    x, y = np.loadtxt(data, unpack = True)
    ax.plot(x, y, '-.', linewidth = 0.85, alpha = 0.3)
    X.append(x)
    Y.append(y)

# each data*.txt has a different number of lines, so we need to know the
# biggest one and append zeros to other N(t).

# get max time
max_x = 0
XX = []
for item in X:
    if max_x < item[-1]:
        max_x = item[-1]
        XX = item

YY = []
# append zeros to all Y values
for item in Y:
    YY.append(np.append(item, np.zeros(XX.size - item.size)))

# calculate average
Y_avg = np.mean(YY, axis = 0)
Y_std = np.std(YY, axis = 0)

# plot average
ax.plot(XX, Y_avg, color = 'green', linewidth = 2.5, label = "Average")
ax.fill_between(XX, Y_avg - Y_std, Y_avg + Y_std, color = 'green', alpha = 0.35)

# plot the exact solution
y = np.exp(-XX / tau) * N0
ax.plot(XX, y, '--', color = 'black', linewidth = 2.0, label = "Exact")

# plot sigma
ax.plot(XX, Y_std, linewidth = 2.5, color = 'orange', label = "$\sigma(t /\\tau)$")

ax.grid()
ax.legend()

plt.title("Radioactive decay of {} samples".format(Ntimes), fontsize = 22)
plt.xlabel("$t / \\tau$", fontsize = 18)
plt.ylabel("$N(t / \\tau)$", fontsize = 18)

plt.xlim(0, 4 * tau)

fig.tight_layout()
#plt.show()
fig.set_size_inches(19.18, 9.89)

plt.savefig("2_decay.png",
            dpi = 150,
            transparent = True)
print("saved 2_decay.png")
ax.set_yscale('log')
plt.ylim(1, N0)
plt.savefig("2_decay_log.png",
            dpi = 150,
            transparent = True)
print("saved 2_decay_log.png")

# getting rid of output files
print("getting rid of output files")
for shit in glob.glob("out_*"):
    os.remove(shit)
print(":D")