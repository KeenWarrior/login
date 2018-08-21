from peewee import SqliteDatabase,Model,CharField,PrimaryKeyField
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QToolBar,QLineEdit
db=SqliteDatabase("login.db")
class Base(Model):
    class Meta:
        database=db
class second(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tit = "Login Page"
        self.top = 100
        self.bot = 80
        self.wid = 1000
        self.hei = 650
        self.new1()
    def new1(self):

        self.line1=QLineEdit(self)
        self.line1.setGeometry(380,380,220,25)
        self.line2 = QLineEdit(self)
        self.line2.setEchoMode(QLineEdit.Password)
        self.line2.setGeometry(380, 430, 220, 25)
        self.pushh1=QPushButton("Login",self)
        self.pushh1.setGeometry(380,515,220,25)
        self.pushh1.clicked.connect(self.con)

        self.labal=QLabel("Username / Email",self)
        self.labal.setGeometry(380,270,200,200)
        self.labal1 = QLabel("Password", self)
        self.labal1.setGeometry(380, 320, 200, 200)
        self.setWindowTitle(self.tit)
        self.setGeometry(self.top,self.bot,self.wid,self.hei)
        self.show()

    def con(self):
        username =self.line1.text()
        password = self.line2.text()

        Log.create(username=username, password=password)


class Log(Base):
    id=PrimaryKeyField()
    username=CharField()
    password=CharField()

db.connect()
db.create_tables([Log])

# h1=Log.create()
app=QApplication([])
wind=second()

app.exec()
