import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic
import sqlite3
import os.path

# Check if the DB file exists, connect to it if found, otherwise create it.
if os.path.exists("ProductList.db"):
    con = sqlite3.connect("ProductList.db")
    cur = con.cursor()
else:
    con = sqlite3.connect("ProductList.db")
    cur = con.cursor()
    # Create a table for storing product information if the file does not exist.
    cur.execute(
        "create table Products (id integer primary key autoincrement, Name text, Price integer);")

# Load the design file
form_class = uic.loadUiType("ProductList3.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Initialize variables to hold product information
        self.id = 0
        self.name = ""
        self.price = 0

        # Set column widths of QTableWidget
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        
        # Set the header of QTableWidget
        self.tableWidget.setHorizontalHeaderLabels(["ProductID","Product Name", "Price"])
        
        # Double click signal processing
        self.tableWidget.doubleClicked.connect(self.doubleClick)

        # Connect returnPressed signal of line edits to focus on the next child
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())

    def addProduct(self):
        # Get input parameters
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        
        # Insert new product into the database
        cur.execute("insert into Products (Name, Price) values(?,?);",
                    (self.name, self.price))
        
        # Refresh displayed product list
        self.getProduct()
        con.commit()

    def updateProduct(self):
        # Get parameters for updating a product
        self.id = self.prodID.text()
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        
        # Update the product in the database
        cur.execute("update Products set name=?, price=? where id=?;",
                    (self.name, self.price, self.id))
        
        # Refresh displayed product list
        self.getProduct()
        con.commit()

    def removeProduct(self):
        # Get parameters for deleting a product
        self.id = self.prodID.text()
        strSQL = "delete from Products where id=" + str(self.id)
        cur.execute(strSQL)
        
        # Refresh displayed product list
        self.getProduct()
        con.commit()

    def getProduct(self):
        # Clear existing content in the table before displaying search results
        self.tableWidget.clearContents()

        # Fetch all products from the database
        cur.execute("select * from Products;")
        row = 0  # Row counter
        
        # Display products in the table
        for item in cur:
            int_as_strID = "{:10}".format(item[0])
            int_as_strPrice = "{:10}".format(item[2])
            
            # Set item ID and align it to the right
            itemID = QTableWidgetItem(int_as_strID)
            itemID.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 0, itemID)
            
            # Set product name
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
            
            # Set item price and align it to the right
            itemPrice = QTableWidgetItem(int_as_strPrice)
            itemPrice.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 2, itemPrice)
            
            row += 1

    def doubleClick(self):
        # Populate line edits with the selected product's information on double click
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())

# Create an instance of the application
app = QApplication(sys.argv)
myWindow = Window()
myWindow.show()
app.exec_()
