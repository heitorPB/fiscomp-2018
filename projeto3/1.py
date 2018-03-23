import numpy as np
import matplotlib.pyplot as plt
import subprocess


# simulation parameters
v0  = 1
rho0 = 0
rho1 = 1.3
rho2 = 0.6
tmax = 100
dt = 0.001
in1 = str(v0) + " " + str(rho0) + " " + str(tmax) + " " + str(dt)
in2 = str(v0) + " " + str(rho1) + " " + str(tmax) + " " + str(dt)
in3 = str(v0) + " " + str(rho2) + " " + str(tmax) + " " + str(dt)


# compile code
compiler = "gfortran"
flags = ["-Wall", "-Wextra", "-Wconversion-extra", "-std=f95", "-pedantic", "-fimplicit-none", "-fbacktrace", "-O3", "-march=native"]
source = "1.f90"
cmd = [compiler] + flags + [source]

print("Compiling {} with {} {}".format(source, compiler, flags))
bla = subprocess.run(cmd, check = True, stdout=subprocess.PIPE)

if bla.returncode != 0:
    print("Oh, shit")
    exit(1)


# run code
print("Running code with:")
print("v0 = {}".format(v0))
print("rho = {}".format(rho0))
print("tmax = {}".format(tmax))
print("dt = {}".format(dt))
with open("out_rho0", mode = 'w') as outfile:
    bla = subprocess.run(["./a.out"],
                         input=in1, encoding='ascii',
                         check = True,
                         stdout=outfile)
print("")
print("Running code with:")
print("v0 = {}".format(v0))
print("rho = {}".format(rho1))
print("tmax = {}".format(tmax))
print("dt = {}".format(dt))
with open("out_rho1", mode = 'w') as outfile:
    bla = subprocess.run(["./a.out"],
                         input=in2, encoding='ascii',
                         check = True,
                         stdout=outfile)
print("")
print("Running code with:")
print("v0 = {}".format(v0))
print("rho = {}".format(rho2))
print("tmax = {}".format(tmax))
print("dt = {}".format(dt))
with open("out_rho2", mode = 'w') as outfile:
    bla = subprocess.run(["./a.out"],
                         input=in3, encoding='ascii',
                         check = True,
                         stdout=outfile)


print("")
print("Plotting results")
fig = plt.figure()
ax = fig.add_subplot(111)

data = np.loadtxt("out_rho0", unpack = True)
T0 = data[0]
X0 = data[1]
data = np.loadtxt("out_rho1", unpack = True)
T1 = data[0]
X1 = data[1]
data = np.loadtxt("out_rho2", unpack = True)
T2 = data[0]
X2 = data[1]

ax.plot(T0,  X0, label = "$\\rho = 0$")
ax.plot(T2,  X2, label = "$\\rho = 0.6 \, kg / m^3$")
ax.plot(T1,  X1, label = "$\\rho = 1.3 \, kg / m^3$")
ax.plot([T2[0], T2[-1]], [X2[-1], X2[-1]], '--', color = 'gray', linewidth = 3, alpha = 0.2)
ax.plot([T1[0], T1[-1]], [X1[-1], X1[-1]], '--', color = 'gray', linewidth = 3, alpha = 0.2)

#ax.set_yscale('log')
#ax.set_xscale('log')
ax.legend(fontsize = 'large', fancybox=True)
ax.grid()

plt.title("Velocidade do ciclista", fontsize = 'large')
plt.ylabel("$v \, (m/s)$", fontsize = 'large')
plt.xlabel("$t \, (s)$", fontsize = 'large')
plt.text(40, 30, "$A = 1/3 \, m^2$ \n" + 
                 "$P = 400 \, W$ \n" +
                 "$m = 70  \, kg$ \n" +
                 "$v_0 = 1 \, m/s$",
                 size = 12)

plt.show()