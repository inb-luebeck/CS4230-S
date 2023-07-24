import numpy as np
import matplotlib.pyplot as plt

def get_idx(n=100):
    i = np.random.randint(0, n)
    j = i
    while j==i:
        j = np.random.randint(0, n)
    return np.array([i, j])

def gerade(w1, w2, theta):
    if w1==w2 and w1=="0":
        print("Ungültige Eingabe!")
    else:
        outputstr = "0 = "
        if int(w1)==1:
            outputstr += "x1"
        elif int(w1)==-1:
            outputstr += "-x1"
        elif int(w1)!=0:
            outputstr += str(int(w1))+"x1"

        if int(w2)==1 and int(w1)!=0:
            outputstr += "+x2"
        elif int(w2)==-1:
            outputstr += "-x2"
        elif int(w2)==1:
            outputstr += "x2"
        elif int(w2)!=0:
            vz = "+" if int(w2)>0 else "-"
            outputstr += vz+str(abs(int(w2)))+"x2"

        if int(theta)!=0:
            vz = "-" if int(theta)>0 else "+"
            outputstr+=vz+str(abs(int(theta)))

        print(f"vorgeschlagene Gerade g: {outputstr}")

def setup():
    data = np.stack(np.meshgrid(np.arange(-5,6), np.arange(-5,6))).reshape([2,-1]).transpose()
    size = 11
    ij = get_idx(data.shape[0])
    pts = data[ij]
    d = pts[0]-pts[1]
    ecke1 = pts[0]
    while np.max(np.abs(ecke1))<=size:
        ecke1 += d
    ecke2 = pts[1]
    while np.max(np.abs(ecke2))<=size:
        ecke2 -= d
    ecken = np.stack([ecke1, ecke2])

    plt.figure(figsize=[7,7])
    plt.plot([0,0], [-size,size], "k")
    plt.plot([-size,size], [0,0], "k")
    for t in range(1,size):
        plt.plot([t,t], [-size,size], "k", alpha=0.1)
        plt.plot([-t,-t], [-size,size], "k", alpha=0.1)
        plt.plot([-size,size], [t,t], "k", alpha=0.1)
        plt.plot([-size,size], [-t,-t], "k", alpha=0.1)
        if t%2==0:
            plt.plot([t,t], [-0.1,0.1], "k")
            plt.text(t,-0.5, str(t), {"horizontalalignment":"center", "verticalalignment":"center"})
            plt.plot([-t,-t], [-0.1,0.1], "k")
            plt.text(-t,-0.5, str(-t), {"horizontalalignment":"center", "verticalalignment":"center"})
            plt.plot([-0.1,0.1], [t,t], "k")
            plt.text(-0.4, -t, str(-t), {"horizontalalignment":"right", "verticalalignment":"center"})
            plt.plot([-0.1,0.1], [-t,-t], "k")
            plt.text(-0.4, t, str(t), {"horizontalalignment":"right", "verticalalignment":"center"})
    plt.plot([-0.1,0,0.1], [size-0.2,size,(size-0.2)], "k")
    plt.plot([(size-0.2),size,(size-0.2)], [-0.1,0,0.1], "k")
    plt.plot([-0.1,0,0.1], [-(size-0.2),-size,-(size-0.2)], "k")
    plt.plot([-(size-0.2),-size,-(size-0.2)], [-0.1,0,0.1], "k")
    plt.text(-0.4, (size-0.2), "y", {"horizontalalignment":"center", "verticalalignment":"center"})
    plt.text(size, -0.4, "x", {"horizontalalignment":"center", "verticalalignment":"center"})
    plt.plot(ecken[:,0], ecken[:,1])
    plt.plot(data[ij,0], data[ij,1], "ro", markersize=5)
    plt.axis("equal")
    plt.xlim([-size,size])
    plt.ylim([-size,size])
    plt.axis("off")
    plt.show()

    return pts
