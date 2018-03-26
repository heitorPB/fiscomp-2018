import numpy as np
import matplotlib.pyplot as plt
import subprocess
import os


# simulation parameters
# a and alpha from https://en.wikipedia.org/wiki/Atmospheric_pressure#Altitude_variation
theta = [10, 40, 60, 90]
m     = 1
L     = 1
g     = 10
dt    = 1e-2
tmax  = 15


# compile code
compiler = "gfortran"
flags = ["-Wall", "-Wextra", "-Wconversion-extra", "-std=f2003",
         "-pedantic", "-fimplicit-none", "-fbacktrace", "-O3",
         "-march=native"]
source = "3.f90"
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
    inputx = str(t) + n + str(m) + n + str(L) + n + str(g) + n + str(dt) + n + str(tmax)
    print("Running code with:")
    print("theta = {}".format(t))
    print("m     = {}".format(m))
    print("L     = {}".format(L))
    print("g     = {}".format(g))
    print("dt    = {}".format(dt))
    print("tmax  = {}".format(tmax))
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
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 3)
ax3 = fig.add_subplot(2, 2, 2)
ax4 = fig.add_subplot(2, 2, 4)

# colors:
cores = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink',
         'gray', 'olive', 'cyan']
dicores = {theta[i]: cores[i] for i in range(0, len(theta))}

for t in theta:
    data = np.loadtxt("out_theta{}".format(t), unpack = True)
    x  = data[0]
    y  = data[1] * 180 / np.pi
    e1 = data[2]
    e2 = data[3]

    # Euler-Cromer:
    yc  = data[4] * 180 / np.pi
    ec1 = data[5]
    ec2 = data[6]

    ax1.plot(x, y, label = "$\\theta_0 = {}$".format(t))
    ax2.plot(x, e1 + e2)
    ax3.plot(x, yc)
    ax4.plot(x, ec1 + ec2)

#ax1.set_yscale('log')
#ax1.set_xscale('log')
#ax1.legend(fontsize = 'large', fancybox=True)
ax1.grid()
ax1.set_ylabel("$\\theta \, (^\\circ)$", fontsize = 'large')
#ax1.set_ylim(-3, 3)
ax1.set_title("Método de Euler")

ax2.grid()
ax2.set_ylabel("$E \, (J)$", fontsize = 'large')
ax2.set_xlabel("$t \, (s)$", fontsize = 'large')

ax3.set_title("Método de Euler-Cromer")
ax3.grid()

ax4.grid()
ax4.set_xlabel("$t \, (s)$", fontsize = 'large')

fig.suptitle("Pêndulo Simples", fontsize = 'x-large')
fig.legend(fontsize = 'large', fancybox = True,
           bbox_to_anchor=(.91, .7),
           loc = 'upper right', borderaxespad=-7)
fig.text(.91, .5, fontsize = 'large',
         s = "$m  = {} \, kg$\n".format(m) +
             "$L  = {} \, m$\n".format(L) +
             "$g  = {} \, m/s^{}$\n".format(g, "2") +
             "$dt = {} \, s$".format(dt)
        )
plt.show()

# remove output files
for t in theta:
    os.remove("out_theta{}".format(t))