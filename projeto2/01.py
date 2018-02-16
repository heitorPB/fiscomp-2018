import numpy as np
import matplotlib.pyplot as plt
import subprocess


compiler = "gfortran"
flags = ["-Wall", "-Wextra", "-Wconversion-extra", "-std=f95", "-pedantic", "-fimplicit-none", "-fbacktrace", "-O3", "-march=native"]
source = "01.f90"
cmd = [compiler] + flags + [source]

print("Compiling {} with {} {}".format(source, compiler, flags))
bla = subprocess.run(cmd, check = True, stdout=subprocess.PIPE)
#print(bla)

if bla.returncode != 0:
    print("Oh, shit")
    exit(1)

print("Running code")
with open("out", mode = 'w') as outfile:
    bla = subprocess.run(["./a.out", ">>", "out"], check = True, stdout=outfile)

print("Plotting results")
fig = plt.figure()
ax = fig.add_subplot(111)

data = np.loadtxt("out", unpack = True)
#print(data)
h  = data[0]
y1 = data[1]
y2 = data[2]
y3 = data[3]
y4 = data[4]

ax.plot(h, y1, label = "$f'_f(1)$")
ax.plot(h, y2, label = "$f'_t(1)$")
ax.plot(h, y3, label = "$f'_{3s}(1)$")
ax.plot(h, y4, label = "$f''_{3s}(1)$")

ax.set_yscale('log')
ax.set_xscale('log')
ax.legend(fontsize = 'large')
ax.grid()
plt.title("Difference between exact and numerical approximation", fontsize = 'large')
plt.ylabel("$\epsilon$", fontsize = 'large')
plt.xlabel("$h$", fontsize = 'large')

plt.show()