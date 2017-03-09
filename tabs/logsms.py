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
import sys

class LogsmsWidget(QWidget):
    """
    Defines the GUI and behaviour of the "Basic Info" commands widget.
    """
    TITLE = 'Log SMS'
    def __init__(self, terminal ,parent=None):
            """
            Initialize the interface widgets.
            """
            QObject.__init__(self)
            QWidget.__init__(self, parent)

            self.terminal = terminal
            self.terminal.updateadd.connect(self.additemRow)

            self.tableWidget = QTableWidget(self)
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setRowCount(0)
            item = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(0, item)
            item = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(1, item)
            item = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(2, item)
            item = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(3, item)
            itemadd = self.tableWidget.horizontalHeaderItem(0)
            itemadd.setText("No HP")
            itemadd = self.tableWidget.horizontalHeaderItem(1)
            itemadd.setText( "Tgl")
            itemadd = self.tableWidget.horizontalHeaderItem(2)
            itemadd.setText("Jam")
            itemadd = self.tableWidget.horizontalHeaderItem(3)
            itemadd.setText("Pesan")
            #creat grid layout
            veticalbox = QVBoxLayout()
            veticalbox.addWidget(self.tableWidget)

            # Create main layout
            container = QHBoxLayout()
            container.addLayout(veticalbox)
            self.setLayout(container)

            #self.additemRow('+62876767862','17/02/28' , '15:47:58+28' , 'testing testing testing')

    def additemRow(self , nohp , tgl , jam , pesan):
        rowPosition = self.tableWidget.rowCount()
        #print str(rowPosition)+ " , " + str(nohp) +" , "+ tgl +" , "+ jam +" , "+ pesan
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(rowPosition , 0, QTableWidgetItem(str(nohp)))
        self.tableWidget.setItem(rowPosition , 1, QTableWidgetItem(str(tgl)))
        self.tableWidget.setItem(rowPosition , 2, QTableWidgetItem(str(jam)))
        self.tableWidget.setItem(rowPosition , 3, QTableWidgetItem(str(pesan)))

if __name__ == '__main__':
    from standalone import run_standalone
    run_standalone(LogsmsWidget)
