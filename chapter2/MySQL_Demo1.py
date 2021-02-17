import pymysql

conn = pymysql.Connect(host='localhost', user='root', password='123456scf',
                       db='student', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
c = conn.cursor()
c.execute('SELECT VERSION()')

print(c.fetchone())

conn.close()
