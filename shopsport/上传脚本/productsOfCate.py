import os
import pymysql

#遍历文件夹，返回文件夹下面的所有文件
def listDir(rootDir):
    file_list = []
    for filename in os.listdir(rootDir):
        filename = os.path.join(rootDir, filename)
        if os.path.isfile(filename):
            file_list.append(filename)
    return file_list

#遍历文件夹，返回文件夹下面的所有子文件夹
def getDir(root):
    dirs_list = []
    for dirName in os.listdir(root):
        dirName = os.path.join(root, dirName)
        if os.path.isdir(dirName):
            dirs_list.append(dirName)
    return dirs_list

#连接数据库插入值
def insert(rootDir):
    parentCate = rootDir.split('\\')[-1]
    file_list = listDir(rootDir)

    # 打开数据库连接
    db = pymysql.connect("202.195.167.248", "root", "root", "market")
    print("链接成功")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    print("准备执行插入语句")
    # SQL 插入语句


    for file in file_list:

        sql = "INSERT INTO market_products(product_img, belongtocategory_id) VALUES(\'%s\', \'%s\');" %('products_img/'+os.path.basename(file), parentCate)
        print(sql)

        try:
        # 执行sql语句

            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            print("ok")
        except:
            # 如果发生错误则回滚
            db.rollback()
            print('error')


    # 关闭数据库连接
    db.close()



