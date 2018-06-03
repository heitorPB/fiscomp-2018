import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines  as lines
import subprocess
import glob, os

r  = [0.5, 1.5, 2.0, 2.5, 3.0, 3.5, 3.666, 3.8910, 4]

print("Plotting results for ex 2a")

def G(x, r):
    return r * x * (1 - x)

fig = plt.figure()
index = 1
for r_ in r:
    x  = np.linspace(0, 1, 10001)
    g1 = G(x,  r_)
    g2 = G(g1, r_)
    g3 = G(g2, r_)
    g4 = G(g3, r_)

    ax = fig.add_subplot(3, 3, index)
    ax.plot(x, x,  label = 'x', linewidth = 3)
    ax.plot(x, g1, label = '$G^{(1)}(x)$')
    ax.plot(x, g2, label = '$G^{(2)}(x)$')
    ax.plot(x, g3, label = '$G^{(3)}(x)$')
    ax.plot(x, g4, label = '$G^{(4)}(x)$')

    linhazinha = lines.Line2D([0], [0])
    ax.legend([linhazinha], ["r = {}".format(r_)],
              handlelength = 0, handletextpad = 0,
              fontsize = 'large', fancybox=True)
    ax.grid()
    index += 1

handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels,
           fontsize = 'large', fancybox = True,
           shadow = True,
           bbox_to_anchor=(.91, .45),
           loc = 'upper right', borderaxespad=-7)
plt.title("Raízes de $G^{(i)}(x)$")
#plt.show()
fig.set_size_inches(19.18, 9.89)
plt.savefig("2a.png",
            dpi = 150,
            transparent = True)


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

x0 = .666
# run code
print("Running code")
with open("out_caos", mode = 'w') as outfile:
    bla = subprocess.run(["./a.out"],
                         input = str(x0),
                         encoding ='ascii',
                         check = True,
                         stdout=outfile)

print("Plotting results for ex 2b")

fig = plt.figure()
ax = fig.add_subplot(111)
data = np.loadtxt("out_caos", unpack = True)
x = data[1]
y = data[0]
ax.scatter(x, y, s = 0.5, c = y, cmap = 'inferno')

plt.title("CAOS")
plt.xlabel("$r$", fontsize = 'large')
plt.ylabel("População", fontsize = 'large')
fig.tight_layout()
#plt.ylim(-.1, 1.1)
#plt.show()
fig.set_size_inches(19.18, 9.89)
plt.savefig("2b.png",
            dpi = 150,
            transparent = True)
plt.xlim(3.5, 4)
plt.ylim(0.1, 1)
plt.savefig("2b_zoom.png",
            dpi = 150,
            transparent = True)

# getting rid of output files
print("getting rid of output files")
for shit in glob.glob("out_*"):
    os.remove(shit)
print(":D")