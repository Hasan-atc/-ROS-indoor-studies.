# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robot_kontrol.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 400)
        MainWindow.setMinimumSize(QtCore.QSize(540, 400))
        MainWindow.setMaximumSize(QtCore.QSize(540, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.etiket_konum = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.etiket_konum.setFont(font)
        self.etiket_konum.setObjectName("etiket_konum")
        self.gridLayout_2.addWidget(self.etiket_konum, 6, 2, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.etiket_lineer = QtWidgets.QLabel(self.centralwidget)
        self.etiket_lineer.setObjectName("etiket_lineer")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.etiket_lineer)
        self.line_lineer = QtWidgets.QLineEdit(self.centralwidget)
        self.line_lineer.setReadOnly(True)
        self.line_lineer.setObjectName("line_lineer")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_lineer)
        self.gridLayout_2.addLayout(self.formLayout, 1, 2, 1, 1)
        self.etiket_kontrol = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.etiket_kontrol.setFont(font)
        self.etiket_kontrol.setObjectName("etiket_kontrol")
        self.gridLayout_2.addWidget(self.etiket_kontrol, 2, 0, 1, 1)
        self.etiket_hiz = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.etiket_hiz.setFont(font)
        self.etiket_hiz.setObjectName("etiket_hiz")
        self.gridLayout_2.addWidget(self.etiket_hiz, 0, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setObjectName("start")
        self.verticalLayout_2.addWidget(self.start)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 5, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.etiket_x = QtWidgets.QLabel(self.centralwidget)
        self.etiket_x.setObjectName("etiket_x")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.etiket_x)
        self.line_x = QtWidgets.QLineEdit(self.centralwidget)
        self.line_x.setReadOnly(True)
        self.line_x.setObjectName("line_x")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_x)
        self.etiket_y = QtWidgets.QLabel(self.centralwidget)
        self.etiket_y.setObjectName("etiket_y")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.etiket_y)
        self.line_y = QtWidgets.QLineEdit(self.centralwidget)
        self.line_y.setReadOnly(True)
        self.line_y.setObjectName("line_y")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_y)
        self.gridLayout_2.addLayout(self.formLayout_2, 7, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.birinciyuk = QtWidgets.QPushButton(self.centralwidget)
        self.birinciyuk.setObjectName("birinciyuk")
        self.horizontalLayout.addWidget(self.birinciyuk)
        self.birincibosaltma = QtWidgets.QPushButton(self.centralwidget)
        self.birincibosaltma.setObjectName("birincibosaltma")
        self.horizontalLayout.addWidget(self.birincibosaltma)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ikinciyuk = QtWidgets.QPushButton(self.centralwidget)
        self.ikinciyuk.setObjectName("ikinciyuk")
        self.horizontalLayout_2.addWidget(self.ikinciyuk)
        self.ikincibosaltma = QtWidgets.QPushButton(self.centralwidget)
        self.ikincibosaltma.setObjectName("ikincibosaltma")
        self.horizontalLayout_2.addWidget(self.ikincibosaltma)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robot Kontrol Arayüzü"))
        self.etiket_konum.setText(_translate("MainWindow", "Konum Göstergesi"))
        self.etiket_lineer.setText(_translate("MainWindow", "Tur Bilgisi:"))
        self.etiket_kontrol.setText(_translate("MainWindow", "Robot Kontrol"))
        self.etiket_hiz.setText(_translate("MainWindow", "Tur Göstergesi"))
        self.start.setText(_translate("MainWindow", "Başlangıç Noktası"))
        self.etiket_x.setText(_translate("MainWindow", "Konum X (m):"))
        self.etiket_y.setText(_translate("MainWindow", "Konum Y (m):"))
        self.birinciyuk.setText(_translate("MainWindow", "Boş Tur"))
        self.birincibosaltma.setText(_translate("MainWindow", "Boş Tur 2. Senaryo"))
        self.ikinciyuk.setText(_translate("MainWindow", "Yüklü Tur"))
        self.ikincibosaltma.setText(_translate("MainWindow", "Yüklü Tur 2. Senaryo"))
        
        
        rospy.init_node("robot_arayuz")
        self.pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
        self.hiz_mesaji = Twist()
        rospy.Subscriber("odom",Odometry,self.odomCallback)
        
        self.line_lineer.setText(str(""))
        self.line_x.setText(str(0.0))
        self.line_y.setText(str(0.0))
        self.birinciyuk.clicked.connect(self.bostur)
        self.birincibosaltma.clicked.connect(self.bostur_2)
        self.ikinciyuk.clicked.connect(self.yuklutur)
        self.ikincibosaltma.clicked.connect(self.yuklutur_2)
        self.start.clicked.connect(self.base)
        
    def odomCallback(self,mesaj):
        self.line_x.setText(str(round(mesaj.pose.pose.position.x,4)))
        self.line_y.setText(str(round(mesaj.pose.pose.position.y,4)))
    
    def hareket(self, x, y):
        self.istemci = actionlib.SimpleActionClient("/move_base", MoveBaseAction)
        self.istemci.wait_for_server()
        self.hedef = MoveBaseGoal()
        self.hedef.target_pose.header.frame_id = "map"
        
        self.x = float(x)
        self.y = float(y)
        
        self.hedef.target_pose.pose.position.x = self.x # hedefin x koordinatı
        self.hedef.target_pose.pose.position.y = self.y # hedefin y kordinatı
        self.hedef.target_pose.pose.orientation.w = 1.0
        
        self.istemci.send_goal(self.hedef)
        self.istemci.wait_for_result()
        

    
    def bostur(self):
        self.hareket(2,0)
        self.hareket(2,-2)
        self.hareket(-1.5,-2)
        self.hareket(-1.75,0)
        self.hareket(-1.5,2)
        self.hareket(2,2)
        self.hareket(2,0)
        self.line_lineer.setText(str("Boş Tur Tamamlandı"))
        self.base
        
    def bostur_2(self):
        self.hareket(-1.5, 0)
        self.hareket(-1.5, 2)
        self.hareket(2, 2)
        self.hareket(2, 0)
        self.hareket(2,-2)
        self.hareket(-1.5,-2)
        self.hareket(-1.5,0)
        self.line_lineer.setText(str("Bos Tur 2 Tamamlandı"))
        self.base
        
    def yuklutur(self):
        self.hareket(2,0)
        self.hareket(-1,0)
        self.hareket(-1.5,0)
        self.hareket(-1,2)
        self.hareket(2,0)
        self.hareket(1.5,-2)
        self.hareket(-0.5,-2)
        self.hareket(1,-2)
        self.hareket(2,0)
        self.hareket(1,2)
        self.hareket(0.5,2)
        self.line_lineer.setText(str("Yüklü Tur Tamamlandı"))
        self.base
    
    def yuklutur_2(self):
        self.hareket(-1.5,0)
        self.hareket(-1,0)
        self.hareket(2,0)
        self.hareket(1,-2)
        self.hareket(-1.5,0)
        self.hareket(0.5,2)
        self.hareket(1,2)
        self.hareket(-0.5,2)
        self.hareket(-1.5,0)
        self.hareket(-0.5,-2)
        self.hareket(1.5,-2)
        self.line_lineer.setText(str("Yüklü Tur 2 Tamamlandı"))
        self.base
        
    def base(self):
        self.hareket(0, 0)
        self.line_lineer.setText(str("Başlangıç Noktasına Dönüldü"))
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
