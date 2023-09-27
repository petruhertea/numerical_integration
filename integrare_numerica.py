<<<<<<< HEAD
# -*- coding: utf-8 -*-


# importing various libraries
from email import message
import math
from sympy import *
import numpy as np
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDialog,
    QDoubleSpinBox,
    QFontComboBox,
    QGridLayout,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
) # see https://www.pythonguis.com/tutorials/pyqt-basic-widgets/

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import random
from tkinter import messagebox

# main window
# which inherits QMainWindow
class Window(QMainWindow):
    
    # constructor
    def __init__(self, parent=None):
        x = Symbol('x')
        super(Window, self).__init__(parent)
        fs='sin(x)'
        self.n=1

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        self.button = QPushButton('Plot dreptunghi')
        self.button1 = QPushButton('Plot trapeze')
        self.button2 = QPushButton('Plot simposon')
        # adding action to the button
        self.button.clicked.connect(self.plot)
        self.button1.clicked.connect(self.plot1)
        self.button2.clicked.connect(self.plot2)

        # creating a Vertical Box layout
        layout = QGridLayout()#QVBoxLayout()
        
        # adding tool bar to the layout
        
        # adding canvas to the layout
        layout.addWidget(self.canvas,1,0)
        
        # adding push button to the layout
        layout.addWidget(self.button,2,0)
        layout.addWidget(self.button1,3,0)
        layout.addWidget(self.button2,4,0)
        fl = QLabel('f = ')
        layout.addWidget(fl,0,1)
        self.fe = QLineEdit('1+cos(x)**2')
        layout.addWidget(self.fe,0,2)
        n1=QLabel('n = ')
        layout.addWidget(n1,1,1)
        self.ne = QLineEdit('10')
        layout.addWidget(self.ne,1,2)
        al = QLabel('a = ')
        layout.addWidget(al,2,1)
        self.ae = QLineEdit('0')
        layout.addWidget(self.ae,2,2)
        bl = QLabel('b = ')
        layout.addWidget(bl,3,1)
        self.be = QLineEdit('20')
        layout.addWidget(self.be,3,2)
        
        # widgets = [
        #     QCheckBox,
        #     QComboBox,
        #     QDateEdit,
        #     QDateTimeEdit,
        #     QDial,
        #     QDoubleSpinBox,
        #     QFontComboBox,
        #     QLCDNumber,
        #     QLabel,
        #     QLineEdit,
        #     QProgressBar,
        #     QPushButton,
        #     QRadioButton,
        #     QSlider,
        #     QSpinBox,
        #     QTimeEdit,
        # ]

        # for w in widgets:
        #     layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)
        
    def plot(self):
        self.figure.clear()
        try:
            a=int(self.ae.text())
            try:
                b=int(self.be.text())
                try:
                    n=int(self.ne.text())
                    try:
                        f=lambdify(Symbol("x"),self.fe.text())
                        h=(b-a)/n
                        x=np.linspace(a,b,n+1)
                        x_plt = np.linspace(a,b,100)
                        plt.plot(x_plt, f(x_plt))
                    
                        int_aprox=0
                        for i in range(n):
                            xval=[x[i],x[i+1],x[i+1],x[i]]
                            f_mid=f((x[i]+x[i+1])/2)
                            yval=[0,0,f_mid,f_mid]
                            plt.fill(xval,yval,color=(0.8,0.8,0.1,0.5))
                        
                            int_aprox+=f_mid
                        int_aprox=h*int_aprox
                        self.canvas.draw()
                    except Exception as e:
                        messagebox.showerror("Eroare ","f nu e valid")
                except Exception as e:
                    messagebox.showerror("Eroare ","n nu e valid")
            except Exception as e:
                    messagebox.showerror("Eroare ","b nu e valid")
        except Exception as e:
                    messagebox.showerror("Eroare ","a nu e valid")

    def plot1(self):
        self.figure.clear()
        try:
            a=int(self.ae.text())
            try:
                b=int(self.be.text())
                try:
                    n=int(self.ne.text())
                    try:
                        f=lambdify(Symbol("x"),self.fe.text())
                        h=(b-a)/n
                        x=np.linspace(a,b,n+1)
                        x_plt = np.linspace(a,b,100)
                        plt.plot(x_plt, f(x_plt))
                        int_aprox=0
                        for i in range(n):
                            xval=[x[i],x[i+1],x[i+1],x[i]]
                            f_mid=f((x[i]+x[i+1])/2)
                            yval=[0,0,f(x[i+1]),f(x[i])]
                            plt.fill(xval,yval,color=(0.2,0.3,0.8,0.5))
                            
                            int_aprox+=f_mid
                        int_aprox=h*int_aprox
                        self.canvas.draw()
                    except Exception as e:
                        messagebox.showerror("Eroare ","f nu e valid")
                except:
                    messagebox.showerror("Eroare ","n nu e valid")
            except:
                messagebox.showerror("Eroare ","b nu e valid")
        except:
            messagebox.showerror("Eroare ","a nu e valid")

    def plot2(self):
        self.figure.clear()
        try:
            a = int(self.ae.text())
            b = int(self.be.text())
            n = int(self.ne.text())
            f = lambdify(Symbol("x"), self.fe.text())
            h = (b - a) / n
            x = np.linspace(a, b, n + 1)
            int_approx = 0
            x_plt = np.linspace(a, b, 100)
            
            # Plot the function f(x)
            plt.plot(x_plt, f(x_plt))
            
            for i in range(n):
                xval = [x[i], x[i + 1], x[i + 1], x[i]]
                f_mid = f((x[i] + x[i + 1]) / 2)
                yval = [0, 0, f(x[i + 1]), f(x[i])]
                int_approx += f(x[i]) + 4 * f_mid + f(x[i + 1])
                plt.fill(xval, yval, color=(0.2, 0.3, 0.8, 0.5))
            
            int_approx = h*int_approx
            self.canvas.draw()
        except:
            messagebox.showerror("Eroare", "Input invalid")

# driver code
if __name__ == '__main__':
    
    
    
    # creating apyqt5 application
    app = QApplication(sys.argv)

    # creating a window object
    main = Window()
    
    # showing the window
    main.show()

    # loop
    sys.exit(app.exec_())
=======
# -*- coding: utf-8 -*-


# importing various libraries
from email import message
import math
from sympy import *
import numpy as np
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDialog,
    QDoubleSpinBox,
    QFontComboBox,
    QGridLayout,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
) # see https://www.pythonguis.com/tutorials/pyqt-basic-widgets/

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import random
from tkinter import messagebox

# main window
# which inherits QMainWindow
class Window(QMainWindow):
    
    # constructor
    def __init__(self, parent=None):
        x = Symbol('x')
        super(Window, self).__init__(parent)
        fs='sin(x)'
        self.n=1

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        self.button = QPushButton('Plot dreptunghi')
        self.button1 = QPushButton('Plot trapeze')
        self.button2 = QPushButton('Plot simposon')
        # adding action to the button
        self.button.clicked.connect(self.plot)
        self.button1.clicked.connect(self.plot1)
        self.button2.clicked.connect(self.plot2)

        # creating a Vertical Box layout
        layout = QGridLayout()#QVBoxLayout()
        
        # adding tool bar to the layout
        
        # adding canvas to the layout
        layout.addWidget(self.canvas,1,0)
        
        # adding push button to the layout
        layout.addWidget(self.button,2,0)
        layout.addWidget(self.button1,3,0)
        layout.addWidget(self.button2,4,0)
        fl = QLabel('f = ')
        layout.addWidget(fl,0,1)
        self.fe = QLineEdit('1+cos(x)**2')
        layout.addWidget(self.fe,0,2)
        n1=QLabel('n = ')
        layout.addWidget(n1,1,1)
        self.ne = QLineEdit('10')
        layout.addWidget(self.ne,1,2)
        al = QLabel('a = ')
        layout.addWidget(al,2,1)
        self.ae = QLineEdit('0')
        layout.addWidget(self.ae,2,2)
        bl = QLabel('b = ')
        layout.addWidget(bl,3,1)
        self.be = QLineEdit('20')
        layout.addWidget(self.be,3,2)
        
        # widgets = [
        #     QCheckBox,
        #     QComboBox,
        #     QDateEdit,
        #     QDateTimeEdit,
        #     QDial,
        #     QDoubleSpinBox,
        #     QFontComboBox,
        #     QLCDNumber,
        #     QLabel,
        #     QLineEdit,
        #     QProgressBar,
        #     QPushButton,
        #     QRadioButton,
        #     QSlider,
        #     QSpinBox,
        #     QTimeEdit,
        # ]

        # for w in widgets:
        #     layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)
        
    def plot(self):
        self.figure.clear()
        try:
            a=int(self.ae.text())
            try:
                b=int(self.be.text())
                try:
                    n=int(self.ne.text())
                    try:
                        f=lambdify(Symbol("x"),self.fe.text())
                        h=(b-a)/n
                        x=np.linspace(a,b,n+1)
                        x_plt = np.linspace(a,b,100)
                        plt.plot(x_plt, f(x_plt))
                    
                        int_aprox=0
                        for i in range(n):
                            xval=[x[i],x[i+1],x[i+1],x[i]]
                            f_mid=f((x[i]+x[i+1])/2)
                            yval=[0,0,f_mid,f_mid]
                            plt.fill(xval,yval,color=(0.8,0.8,0.1,0.5))
                        
                            int_aprox+=f_mid
                        int_aprox=h*int_aprox
                        self.canvas.draw()
                    except Exception as e:
                        messagebox.showerror("Eroare ","f nu e valid")
                except Exception as e:
                    messagebox.showerror("Eroare ","n nu e valid")
            except Exception as e:
                    messagebox.showerror("Eroare ","b nu e valid")
        except Exception as e:
                    messagebox.showerror("Eroare ","a nu e valid")

    def plot1(self):
        self.figure.clear()
        try:
            a=int(self.ae.text())
            try:
                b=int(self.be.text())
                try:
                    n=int(self.ne.text())
                    try:
                        f=lambdify(Symbol("x"),self.fe.text())
                        h=(b-a)/n
                        x=np.linspace(a,b,n+1)
                        x_plt = np.linspace(a,b,100)
                        plt.plot(x_plt, f(x_plt))
                        int_aprox=0
                        for i in range(n):
                            xval=[x[i],x[i+1],x[i+1],x[i]]
                            f_mid=f((x[i]+x[i+1])/2)
                            yval=[0,0,f(x[i+1]),f(x[i])]
                            plt.fill(xval,yval,color=(0.2,0.3,0.8,0.5))
                            
                            int_aprox+=f_mid
                        int_aprox=h*int_aprox
                        self.canvas.draw()
                    except Exception as e:
                        messagebox.showerror("Eroare ","f nu e valid")
                except:
                    messagebox.showerror("Eroare ","n nu e valid")
            except:
                messagebox.showerror("Eroare ","b nu e valid")
        except:
            messagebox.showerror("Eroare ","a nu e valid")

    def plot2(self):
        self.figure.clear()
        try:
            a=int(self.ae.text())
            try:
                b=int(self.be.text())
                try:
                    n=int(self.ne.text())
                    try:
                        f=lambdify(Symbol("x"),self.fe.text())
                        h = (b-a)/n
                        x = np.linspace(a,b,n+1)    
                        int_approx = 0
                        x_plt = np.linspace(a, b, 100)
                        plt.plot = (x_plt,f(x_plt))
                        
                        for i in range(n):
                            xval = [x[i], x[i+1],x[i+1],x[i]]
                            f_mid = f((x[i]+x[i+1])/2)
                            yval = [0,0,f(x[i+1]),f(x[i])]
                            int_approx += f(x[i])+4*f((x[i]+x[i+1])/2)+f(x[i+1])/6
                            plt.fill(xval, yval, color = (0.2, 0.3, 0.8, 0.5))
                        
                        int_approx = h*int_approx
                        self.canvas.draw()
                    except:
                        messagebox.showerror("Eroare ","f nu e valid")
                except:
                    messagebox.showerror("Eroare ","n nu e valid")
            except:
                messagebox.showerror("Eroare ","b nu e valid")
        except:
            messagebox.showerror("Eroare ","a nu e valid")

# driver code
if __name__ == '__main__':
    
    
    
    # creating apyqt5 application
    app = QApplication(sys.argv)

    # creating a window object
    main = Window()
    
    # showing the window
    main.show()

    # loop
    sys.exit(app.exec_())
>>>>>>> a42eec80ffdda53ce3a56150aaee4ad4129750d8
