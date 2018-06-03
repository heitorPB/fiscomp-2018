import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.lines  as lines
import subprocess
import glob, os

# simulation parameters
r  = [3.57, 3.666, 3.8910, 4]
x0 = [0.01, 0.2, 0.4, 0.6, 0.8, 0.99]

# compile code
compiler = "gfortran"
flags = ["-Wall", "-Wextra", "-Wconversion-extra", "-std=f2003", "-pedantic", "-fimplicit-none", "-fbacktrace", "-O3", "-march=native"]
source = "2_poincare.f90"
cmd = [compiler] + flags + [source]

print("Compiling {} with {} {}".format(source, compiler, flags))
bla = subprocess.run(cmd, check = True, stdout=subprocess.PIPE)

if bla.returncode != 0:
    print("Oh, shit")
    exit(1)


# run code
print("Running code with:")
for r_ in r:
    print("r = {}".format(r_))

    for x0_ in x0:
        print("\tx0 = {}".format(x0_))
        in_ = str(r_) + "\n" + str(x0_)

        with open("out_r{}_x{}".format(r_, x0_), mode = 'w') as outfile:
            bla = subprocess.run(["./a.out"],
                                 input=in_, encoding='ascii',
                                 check = True,
                                 stdout=outfile)


print("")
print("Plotting results")

fig = plt.figure()
fig.tight_layout()

plotIndex = 1
for r_ in r:
    data = np.loadtxt("out_r{}_x{}".format(r_, 0.4), unpack = True)
    x = data[0]
    y = data[1]
    z = data[2]

    ax = fig.add_subplot(2, 2, plotIndex, projection='3d')
    ax.scatter(x, y, z, s = 0.5, c = x + y + z, cmap = 'inferno')

    linhazinha = lines.Line2D([0], [0])
    ax.legend([linhazinha], ["r = {}".format(r_)],
              handlelength = 0, handletextpad = 0,
              fontsize = 'large', fancybox=True)

    ax.set_xlabel("$x_i$")
    ax.set_ylabel("$x_{i+1}$")
    ax.set_zlabel("$x_{i+2}$")
    plotIndex += 1

fig.suptitle("Poincaré plot for $G(x) = r x (1 - x)$")
plt.show()
fig.set_size_inches(19.18, 9.89)
fig.savefig("2_poincare.png",
            dpi = 150,
            transparent = True)


# getting rid of output files
print("getting rid of output files")
for shit in glob.glob("out_r*_x*"):
    os.remove(shit)
print(":D")