from PyQt4 import QtGui
from RefRed.load_reduced_data_set.reduced_ascii_table_handler import ReducedAsciiTableHandler


class ReducedAsciiDataRightClick(object):
    
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        
    def run(self):
        menu = QtGui.QMenu(self.parent)
        remove_rows = menu.addAction("Remove Row(s)")
        clear_table = menu.addAction("Clear Table")
        action = menu.exec_(QtGui.QCursor.pos())
        
        if action == remove_rows:
            self.remove_rows()
        elif action == clear_table:
            self.clear_table
            
    def remove_rows(self):
        o_reduced_ascii_table_handler = ReducedAsciiTableHandler(parent = self.parent)
        o_reduced_ascii_table_handler.remove_rows()

    def clear_table(self):
        o_reduced_ascii_table_handler = ReducedAsciiTableHandler(parent = self.parent)
        o_reduced_ascii_table_handler.clear_table()
        