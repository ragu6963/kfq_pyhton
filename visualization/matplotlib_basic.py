# %%
# %matplotlib inline
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# %%
import warnings

warnings.filterwarnings("ignore")

# %%
mpl.rcParams["axes.unicode_minus"] = True
# %%
plt.plot([1, 2, 3, 4], [1, 2, 3, 4], "o")
plt.ylabel("y")
plt.xlabel("x")
plt.show()

# %%
plt.plot([1.5, 2.5, 3.5, 4.5], "o")
plt.ylabel("y")
plt.xlabel("x")
plt.show()

# %%
plt.plot([1.5, 2.5, 3.5, 4.5], "go--")
plt.ylabel("y")
plt.xlabel("x")
plt.show()

# %%
plt.plot(
    [1.5, 2.5, 3.5, 4.5], color="red", marker="o", linestyle="dashed", linewidth=2, markersize=20
)

# %%
 t = np.arange(0.,5.,0.2)
 t
# %%
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show()
# %%
data = {'a':np.arange(50),
        'c':np.arange(50),
        'd':np.arange(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 10
data

# %%
plt.scatter('a','b',c='c',s='d',marker='^',data=data)
plt.minorticks_on()
plt.show()
# %%
names=['group_a','group_b','group_c']
values=[1,10,100]

plt.figure(figsize=(9,5))

plt.subplot(231)
plt.bar(names,values)
plt.subplot(232)
plt.scatter(names,values)
plt.subplot(233)
plt.plot(names,values)
plt.subplot(234)
plt.bar(names,values)
plt.subplot(235)
plt.scatter(names,values)
plt.subplot(236)
plt.plot(names,values)
# %%
mu,sigma = 100,15
x = mu + sigma * np.random.randn(100000)

n,bins,patches = plt.hist(x,50,density=1,facecolor='g',alpha=0.75)


# %%
ax  = plt.subplot(111)
t = np.arange(0,5.0,0.01)
s = np.cos(2*np.pi*t)
line = plt.plot(t,s,lw=2)
plt.annotate('local max',xy=(2,1),xytext=(3,1.5),
            arrowprops=dict(facecolor='black',shrink=0.05))


# %%
import matplotlib.font_manager as fm
path = "C:\\Users\\admin\\AppData\\Local\\Microsoft\\Windows\\Fonts\\NanumBarunGothic.ttf"
fontprop = fm.FontProperties(fname=path, size=12)
N = 5
menMeans = (20,35,30,35,27)
womenMeans = (25,32,34,20,25)
menStd = (2,3,4,1,2)
womenStd = (3,5,2,3,3)
ind=np.arange(N)
width=0.35

p1 = plt.bar(ind,menMeans,width=width,yerr=menStd,)
p2 = plt.bar(ind,womenMeans,width=width,yerr=menStd,bottom=menMeans)

plt.ylabel("점수",fontproperties=fontprop)
plt.xlabel("그룹",fontproperties=fontprop)

plt.xticks(ind,('G1','G2','G3','G4','G5'))
plt.yticks(np.arange(0,81,10))

font_name = fm.FontProperties(fname=path).get_name()
plt.legend((p1[0],p2[0]),('남자','여자'),prop = fontprop)


# plt.legend(prop=fontprop,loc='upper right')

# %%

# %%
