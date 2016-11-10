from PyQt4.QtGui import QFileDialog
from PIL import Image


class FileHandler(object):

    data = []
    
    def __init__(self, parent=None):
        self.parent = parent
        
    def browse_tiff_file(self):
        
        
        file_name = str(QFileDialog.getOpenFileName(caption = "Select the TIFF file",
                                                filter = "tiff (*.tif)"))
        
        if file_name:
            self.parent.ui.tiff_file_label.setText(file_name)
            self.load_image(file_name)
            self.display_image()
            
    def load_image(self, filename):
        data = Image.open(filename)
        self.data = data
        
    def display_image(self):
        self.parent.ui.widget.canvas.ax.imshow(self.data)
        self.parent.ui.widget.draw()
            