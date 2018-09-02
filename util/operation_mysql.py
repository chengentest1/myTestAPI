import configparser
import pymysql
import sys

sys.path.append('..')

class user:
    def __init__(self):
        cf=configparser.ConfigParser()
        cf.read('../dataconfig/db.conf',encoding='utf-8')
        self.conn=pymysql.connect(host=cf.get('local','db_host'),
                                  port=int(cf.get('local','db_port')),
                                  user=cf.get('local','db_user'),
                                  passwd=cf.get('local','db_passwd'),
                                  db=cf.get('local','db_name'),
                                  charset='utf8')
        self.cur=self.conn.cursor()


    def __del__(self):
        self.cur.close()
        self.conn.close()

    def getAll(self):
        self.cur.execute('select * from user')
        result=[]
        for item in self.cur.fetchall():
            result.append(dict(zip(('id','name','passwd'),item)))
        return result
    def getUserById(self,id):
        self.cur.execute('select * from user where id=%d' %int(id))
        result=self.cur.fetchone()
        if result:
            return dict(zip('id','name','passwd'),result)
        else:
            return None
    def do_sql(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()
    def del_user(self,name):
        self.cur.execute("delete from user where name='%s'" %name)
        self.conn.commit()

if __name__=="__main__":
    ki=user().del_user('cheng')
    print(ki)