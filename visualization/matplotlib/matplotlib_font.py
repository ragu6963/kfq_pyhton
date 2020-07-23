# %%
import platform

platform.platform()

# %%
import sys

sys.version_info

# %%
import matplotlib

print("버전 : ", matplotlib.__version__)
print("설치 위치 : ", matplotlib.__file__)
print("설정: ", matplotlib.get_configdir())
print("캐시 : ", matplotlib.get_cachedir())


# %%
import warnings

warnings.filterwarnings("ignore")

# %%
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm

# %%
matplotlib.font_manager._rebuild()

# %%
print("설정 파일 위치:", matplotlib.matplotlib_fname())


# %%
fm.findSystemFonts(fontpaths=None, fontext="ttf")[:10]


# %%
fm.fontManager.ttflist[:10]
# %%
[(f.name, f.fname) for f in fm.fontManager.ttflist if "Nanum" in f.name][:10]

# %%
path = "C:\\Users\\admin\\AppData\\Local\\Microsoft\\Windows\\Fonts\\NanumBarunGothic.ttf"
fontprop = fm.FontProperties(fname=path, size=12)
plt.plot([1, 2, 3, 4])
plt.title("테스트", fontproperties=fontprop)
plt.xlabel("테스트", fontproperties=fontprop)
plt.ylabel("테스트", fontproperties=fontprop)

# %%
print("설정 파일 위치: ", matplotlib.matplotlib_fname())
# %%
print("폰트 사이즈")
print(plt.rcParams["font.size"])
print("폰트 글꼴")
print(plt.rcParams["font.family"])

# %%
plt.rcParams["font.family"] = "NanumBarunGothic"
plt.rcParams["font.size"] = 20
plt.rcParams["figure.figsize"] = (14, 4)

# %%
plt.plot([1, 2, 3, 4])
plt.title("테스트")
plt.xlabel("테스트")
plt.ylabel("테스트")
plt.style.use("seaborn-pastel")
plt.show()
