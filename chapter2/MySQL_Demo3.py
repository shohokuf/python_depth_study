import pymysql

# 打开数据库连接
db = pymysql.Connect(host='localhost', user='root', password='123456scf', db='student', charset='utf8',
                     cursorclass=pymysql.cursors.DictCursor)

# 使用cursor()方法获取操作游标
c = db.cursor()
# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE "
try:
    # 执行SQL语句
    c.execute(sql)
    # 获取所有记录列表
    results = c.fetchall()
    print(results)
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
