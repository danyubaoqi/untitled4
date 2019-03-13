# 创建一个类，用来通过sql语句查询结果实例化对象用
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:root@/mydata"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Example(db.Model):
    __tablename__="example"
    id=db.Column("id",db.Integer,primary_key=True)
    data=db.Column("data",db.VARCHAR)


