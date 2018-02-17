import numpy as np
import matplotlib.pyplot as plt
import subprocess


compiler = "gfortran"
flags = ["-Wall", "-Wextra", "-Wconversion-extra", "-std=f95", "-pedantic", "-fimplicit-none", "-fbacktrace", "-O3", "-march=native"]
source = "03.f90"
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
T = data[0]
X = data[1]

ax.plot(T,  X, label = "Positive Root")
ax.plot(T, -X, label = "Negative Root")

#ax.set_yscale('log')
#ax.set_xscale('log')
ax.legend(fontsize = 'large')
ax.grid()
plt.title("Roots of $m - \\tanh(m/T)$", fontsize = 'large')
plt.ylabel("$m_\pm$", fontsize = 'large')
plt.xlabel("$T/T_c$", fontsize = 'large')

plt.show()