from PyQt5 import QtCore, QtGui, QtWidgets
from report_view import Ui_report_view
from create_report_view import Ui_reportCreateView
#from main_view import Ui_MainWindow

class function(object):
    global Ui_MainWindow
    global total_cost

    def returnObj(self,object): #COPY OF MAIN VIEW INSTANCE
        global Ui_MainWindow #Declared again to edit value
        Ui_MainWindow = object

    def addtoCart(self, object,item):
        global total_cost  #Declared again to edit value
        rowCount = Ui_MainWindow.cart_table.rowCount()
        Ui_MainWindow.cart_table.insertRow(rowCount)
        Ui_MainWindow.cart_table.setItem(rowCount - 1, 0, QtWidgets.QTableWidgetItem(item.text()))
        rowCount = rowCount + 1
        # total_cost += ITEM COSTS   TO BE EDITED ----------------------------------------------------------------------
        # Ui_MainWindow.total_table.setItem(main_view.total_table.rowCount()-1, 1, QtWidgets.QTableWidgetItem(total_cost)) REMOVE COMMENT ONCED TOTAL COST IS DEFINED


    def deleteItem(self,row):
        global total_cost
        item_cost = Ui_MainWindow.cart_table.itemAt(row-1,1)
        #total_cost = total_cost - str(item_cost)
        # main_view.total_table.setItem(main_view.total_table.rowCount()-1, 1, QtWidgets.QTableWidgetItem(total_cost)) REMOVE COMMENT ONCED TOTAL COST IS DEFINED

        Ui_MainWindow.cart_table.removeRow(row-1)

    def report(self):
        Ui_MainWindow.window = QtWidgets.QMainWindow()
        Ui_MainWindow.ui = Ui_reportCreateView()
        Ui_MainWindow.ui.setupUi(Ui_MainWindow.window)
        Ui_MainWindow.window.show()

    def total(self):
        return total_cost

