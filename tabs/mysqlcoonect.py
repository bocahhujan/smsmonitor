# Copyright (c) 2010 Shelltoad Computing <info@shelltoad.com>
#
# This file is part of the "AT Command Toolkit" application.
#
# The "AT Command Toolkit" is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

"""
Module containing the "Basic Info" commands class/widget.
"""

# 3rd party modules

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
import platform
import sys

class MysqlcoonectWidget(QWidget):
    """
    Defines the GUI and behaviour of the "Basic Info" commands widget.
    """
    TITLE = 'Database Conection'
    #db 	= QSqlDatabase.addDatabase("QMYSQL")
    if(platform.system() != 'Linux'):
        app = QApplication(sys.argv)

    settings = QSettings('mjnapp', 'smsmonitor')
    dbc = QSqlDatabase.addDatabase("QMYSQL")

    def __init__(self, parent=None):
            """
            Initialize the interface widgets.
            """
            QWidget.__init__(self, parent)

            # Create the buttons

            self.con_btn = QPushButton( QIcon(':/images/database_connect.png'), self.tr('Connected'))
            self.dis_tton = QPushButton( QIcon(':/images/disconnect.png') , self.tr('Disconnected'))
            self.dis_tton.setEnabled(False)
            self.server = QLineEdit()
            self.server.setText(self.settings.value('server').toString())
            self.db = QLineEdit()
            self.db.setText(self.settings.value('dbname').toString())
            self.username = QLineEdit()
            self.username.setText(self.settings.value('username').toString())
            self.password = QLineEdit()
            self.password.setText(self.settings.value('password').toString())
            self.password.setEchoMode(QLineEdit.Password)

            # Create the button groupbox & layout

            button_box = QFormLayout();
            button_box.addRow(self.tr("&Server :"), self.server);
            button_box.addRow(self.tr("&Database :"), self.db);
            button_box.addRow(self.tr("&Username :"), self.username);
            button_box.addRow(self.tr("&Password :"), self.password);
            button_box.addRow(self.dis_tton,self.con_btn);


            # Create main layout
            container = QHBoxLayout()
            container.addStretch()
            container.addLayout(button_box)
            container.addStretch()
            self.setLayout(container)

            # Connect widgets
            self.connect(self.con_btn, SIGNAL('clicked()'), self.connectDb)
            self.connect(self.dis_tton, SIGNAL('clicked()'), self.connectCloss)

    def connectDb(self):
        #get settings
        server = str(self.server.text())
        dbname = str(self.db.text())
        username = str(self.username.text())
        password = str(self.password.text())

        self.settings.setValue('server' , server )
        self.settings.setValue('dbname' , dbname )
        self.settings.setValue('username' , username )
        self.settings.setValue('password' , password )

        if(server == "" and dbname == "" and username == "" and password == ""):
            self.showdialog('Mohon isi Setting Database dengan bennar')
        else:
            self.dbc.setHostName(server)
            self.dbc.setDatabaseName(dbname)
            self.dbc.setUserName(username)
            self.dbc.setPassword(password)
            self.dbstatus = self.dbc.open()
            if(self.dbstatus != True ):
                connection = self.dbc.connectionName();
                self.dbc.removeDatabase(connection);
                self.showdialog('Error Connect to Databases')
            else:
                self.server.setEnabled(False)
                self.db.setEnabled(False)
                self.username.setEnabled(False)
                self.password.setEnabled(False)
                self.con_btn.setEnabled(False)
                self.dis_tton.setEnabled(True)

            print self.dbstatus;


    def connectCloss(self):
        self.dbc.close()
        connection = self.dbc.connectionName();
        rmcon = QSqlDatabase().removeDatabase(connection);
        self.server.setEnabled(True)
        self.db.setEnabled(True)
        self.username.setEnabled(True)
        self.password.setEnabled(True)
        self.con_btn.setEnabled(True)
        self.dis_tton.setEnabled(False)

    def showdialog(slef , text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle("Database Coonect")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)


        retval = msg.exec_()
        print "value of pressed message box button:", retval

    def insert(self , qry ):
        if(self.dbc.open()):
            qr = QSqlQuery()
            print "Print Query : "+qry ;
            print qr.exec_(qry)



if __name__ == '__main__':
    from standalone import run_standalone
    run_standalone(MysqlcoonectWidget)
