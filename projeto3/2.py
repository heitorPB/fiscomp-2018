import numpy as np
import matplotlib.pyplot as plt
import subprocess


# simulation parameters
# a and alpha from https://en.wikipedia.org/wiki/Atmospheric_pressure#Altitude_variation
v0    = 666
theta = [10, 20, 30, 40, 45, 50, 60, 70, 80]
gamma = 4e-5
a     = 0.00973848
alpha = 3.508
T0    = 300
dt    = 0.001


# compile code
compiler = "gfortran"
flags = ["-Wall", "-Wextra", "-Wconversion-extra", "-std=f2003", "-pedantic", "-fimplicit-none", "-fbacktrace", "-O3", "-march=native"]
source = "2.f90"
cmd = [compiler] + flags + [source]

print("Compiling {} with {} {}".format(source, compiler, flags))
bla = subprocess.run(cmd, check = True, stdout=subprocess.PIPE)

if bla.returncode != 0:
    print("Oh, shit")
    exit(1)
print("")


# run code
for t in theta:
    n = " "
    inputx = str(v0) + n + str(t) + n + str(gamma) + n + str(a) + n + str(alpha) + n + str(T0) + n + str(dt)
    print("Running code with:")
    print("v0      = {}".format(v0))
    print("theta   = {}".format(t))
    print("gamma/m = {}".format(gamma))
    print("a       = {}".format(a))
    print("alpha   = {}".format(alpha))
    print("T0      = {}".format(T0))
    print("dt      = {}".format(dt))
    #print(inputx)

    with open("out_theta{}".format(t), mode = 'w') as outfile:
        bla = subprocess.run(["./a.out"],
                             input=inputx, encoding='ascii',
                             check = True,
                             stdout=outfile)
    print("")


print("")
print("Plotting results")
fig = plt.figure()
ax = fig.add_subplot(111)

for t in theta:
    data = np.loadtxt("out_theta{}".format(t), unpack = True)
    x = data[0]
    y = data[1]
    ax.plot(x, y, label = "$\\theta = {}$".format(t))

#ax.set_yscale('log')
#ax.set_xscale('log')
ax.legend(fontsize = 'large', fancybox=True)
ax.grid()

plt.title("Trajetória do projétil", fontsize = 'large')
plt.ylabel("$y \, (m)$", fontsize = 'large')
plt.xlabel("$x \, (m)$", fontsize = 'large')
plt.text(12e3, 13e3, "$T_0       = {} \, K   $\n".format(T0) + 
                     "$a         = {} \, K/m $\n".format(a) +
                     "$\\alpha   = {} \,     $\n".format(alpha) +
                     "$\\gamma/m = {} \, m^{}$\n".format(gamma, "{-1}") +
                     "$v_0       = {} \, m/s $".format(v0),
                     size = 12)

plt.show()