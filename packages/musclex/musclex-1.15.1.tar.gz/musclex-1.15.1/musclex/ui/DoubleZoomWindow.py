"""
Copyright 1999 Illinois Institute of Technology

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL ILLINOIS INSTITUTE OF TECHNOLOGY BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Except as contained in this notice, the name of Illinois Institute
of Technology shall not be used in advertising or otherwise to promote
the sale, use or other dealings in this Software without prior written
authorization from Illinois Institute of Technology.
"""

import matplotlib.pyplot as plt
import fabio
from .pyqt_utils import *
import numpy as np
import cv2

try:
    import PyMca.MaskImageWidget as PyMcaMaskImageWidget
except ImportError:
    import PyMca5.PyMca.MaskImageWidget as PyMcaMaskImageWidget


class DoubleZoomWindow(QDialog):
    """
    Dialog for double zoom
    """
    def __init__(self, doubleZoomCheckBox):
        super(DoubleZoomWindow, self).__init__(None)
        self.doubleZoomCheckBox = doubleZoomCheckBox
        self.initUI()

    def initUI(self):
        self.mainLayout = QGridLayout(self)
        self.imageFigure = plt.figure()
        self.imageAxes = self.imageFigure.add_subplot(111)
        self.imageCanvas = FigureCanvas(self.imageFigure)
        self.mainLayout.addWidget(self.imageCanvas, 0, 0, 1, 4)

    def scaleAndPlotImage(self, img):
        scaledImage = img#cv2.resize(img, (0,0), fx=5, fy=5)
        self.imageAxes.imshow(scaledImage)
        self.imageCanvas.draw_idle()


    def closeEvent(self, event):
        print("Double Zoom dialog is closed")
        self.doubleZoomCheckBox.setCheckState(Qt.Unchecked)

