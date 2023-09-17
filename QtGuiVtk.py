import sys
import random
from PyQt6 import QtCore, QtWidgets, QtGui

import PyQt6.QtCore
import vtk

from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 553)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.gridlayout = QtWidgets.QGridLayout(self.centralWidget)
        self.vtkWidget = QVTKRenderWindowInteractor(self.centralWidget)
        self.gridlayout.addWidget(self.vtkWidget, 0, 0, 1, 1)
        #MainWindow.setCentralWidget(self.centralWidget)

class MyWidget0(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ren = vtk.vtkRenderer()
        self.ui.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.ui.vtkWidget.GetRenderWindow().GetInteractor()

        # Create source
        source = vtk.vtkSphereSource()
        source.SetCenter(0, 0, 0)
        source.SetRadius(5.0)

        # Create a mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(source.GetOutputPort())

        # Create an actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        self.ren.AddActor(actor)

        #
        # self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "??"]
        #
        # self.button = QtWidgets.QPushButton("Click me!")
        # self.text = QtWidgets.QLabel("Hello World")
        # self.text.setAlignment(QtCore.Qt.AlignCenter)
        #
        # self.layout = QtWidgets.QVBoxLayout()
        # self.layout.addWidget(self.text)
        # self.layout.addWidget(self.button)
        # self.setLayout(self.layout)
        #
        # self.button.clicked.connect(self.magic)


    def magic(self):
        self.text.setText(random.choice(self.hello))

    def print_inf(self):
        print(PyQt6.__version__)
        print(QtCore.__version__)

class MyWidget(QVTKRenderWindowInteractor):
    def __init__(self):
        super().__init__()





def QVTKRenderWidgetConeExample():



    """A simple example that uses the QVTKRenderWindowInteractor class."""

    # every QT app needs an app
    app = QtWidgets.QApplication(['QVTKRenderWindowInteractor'])

    # create the widget
    widget = MyWidget()#QVTKRenderWindowInteractor()
    widget.Initialize()
    widget.Start()
    # if you don't want the 'q' key to exit comment this.
    widget.AddObserver("ExitEvent", lambda o, e, a=app: a.quit())

    ren = vtk.vtkRenderer()
    widget.GetRenderWindow().AddRenderer(ren)

    #source = vtk.vtkConeSource()
    #source.SetResolution(8)
    # Create source
    source = vtk.vtkSphereSource()
    source.SetCenter(0, 0, 0)
    source.SetRadius(5.0)


    coneMapper = vtk.vtkPolyDataMapper()
    coneMapper.SetInputConnection(source.GetOutputPort())

    coneActor = vtk.vtkActor()
    coneActor.SetMapper(coneMapper)

    ren.AddActor(coneActor)

    # show the widget
    widget.show()
    # start event processing
    app.exec()

if __name__ == "__main__":


    # app = QtWidgets.QApplication([])
    #
    # widget = MyWidget()
    # widget.print_inf()
    # widget.resize(800, 600)
    # widget.show()
    #
    # sys.exit(app.exec_())
    QVTKRenderWidgetConeExample()