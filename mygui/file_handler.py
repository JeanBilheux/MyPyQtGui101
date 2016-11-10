from PyQt4.QtGui import QFileDialog


class FileHandler(object):
    
    def __init__(self, parent=None):
        self.parent = parent
        
    def browse_tiff_file(self):
        
        
        file_name = QFileDialog.getOpenFileName(caption = "Select the TIFF file",
                                                filter = "tiff (*.tif)")
        
        if file_name:
            self.parent.ui.tiff_file_label.setText(file_name)
        