import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines  as lines
import subprocess
import glob, os

# simulation parameters
r  = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 3.666, 3.8910]
x0 = [0.2, 0.4, 0.6, 0.8]
eps = 0.001

# compile code
compiler = "gfortran"
flags = ["-Wall", "-Wextra", "-Wconversion-extra", "-std=f2003", "-pedantic", "-fimplicit-none", "-fbacktrace", "-O3", "-march=native"]
source = "1.f90"
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
        in_ = str(r_) + "\n" + str(x0_) + "\n" + str(eps)

        with open("out_r{}_x{}".format(r_, x0_), mode = 'w') as outfile:
            bla = subprocess.run(["./a.out"],
                                 input=in_, encoding='ascii',
                                 check = True,
                                 stdout=outfile)

print("")
print("Plotting results")
def plota(eixo_x, legenda_y, nome):
    fig = plt.figure()
    subplotIndex = 1
    for r_ in r:
        ax = fig.add_subplot(3, 3, subplotIndex)

        for x0_ in x0:
            data = np.loadtxt("out_r{}_x{}".format(r_, x0_), unpack = True)
            x = data[eixo_x]
            i = data[1]

            ax.plot(i, x, label = "$x_0 = {}$".format(x0_))

        #ax.set_yscale('log')
        #ax.set_xscale('log')
        #ax.legend(fontsize = 'large', fancybox=True)
        linhazinha = lines.Line2D([0], [0])
        ax.legend([linhazinha], ["r = {}".format(r_)],
                  handlelength = 0, handletextpad = 0,
                  fontsize = 'large', fancybox=True)
        ax.grid()

        if subplotIndex == 1 or subplotIndex == 4 or subplotIndex == 7:
            plt.ylabel(legenda_y, fontsize = 'large')
        if subplotIndex == 7 or subplotIndex == 8 or subplotIndex == 9:
            plt.xlabel("$i$", fontsize = 'large')
        subplotIndex += 1

    fig.suptitle("População normalizada", fontsize = 'large')
    # only last ax legend!
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels,
               fontsize = 'large', fancybox = True,
               shadow = True,
               bbox_to_anchor=(.91, .45),
               loc = 'upper right', borderaxespad=-7)
    #plt.show()
    fig.set_size_inches(19.18, 9.89)
    plt.savefig(nome,
                dpi = 150,
                transparent = True)

plota(0, "$x_i$", "1b.png")
plota(2, "$d_i$", "1c.png")


# getting rid of output files
print("getting rid of output files")
for shit in glob.glob("out_r*_x*"):
    os.remove(shit)
print(":D")