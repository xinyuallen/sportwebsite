from productsOfCate import listDir, getDir, insert

#文件夹名
root = r"C:\Users\yongt\Desktop\products"

file_list = []
dirs = getDir(root)
sonDirs = []
for dir in dirs:
    sonDirs.extend(getDir(dir))

for sonDir in sonDirs:
    insert(sonDir)










