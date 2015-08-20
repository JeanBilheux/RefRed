from PyQt4 import QtGui

from RefRed.calculations.run_sequence_breaker import RunSequenceBreaker
from RefRed.calculations.check_list_run_compatibility_and_display_thread import CheckListRunCompatibilityAndDisplayThread
from RefRed.plot.display_reduction_table import DisplayReductionTable
import RefRed.colors 
from RefRed.lconfigdataset import LConfigDataset
from RefRed.plot.clear_plots import ClearPlots
from RefRed.calculations.locate_list_run import LocateListRun

class UpdateReductionTable(object):
    
    raw_runs = None
    
    def __init__(self, parent=None, row=0, col=1, runs=None):
        self.parent= parent
        self.row = row
        self.col = col
        
        item = self.parent.ui.reductionTable.item(row, col)
        if item.text() == '':
            self.clear_cell()
            return
        
        data_type = 'data' if col == 1 else 'norm'
        is_data_displayed = True if (col == 1) else False

        self.raw_runs = str(runs)
        run_breaker = RunSequenceBreaker(run_sequence=self.raw_runs)
        list_run = run_breaker.final_list
        
        # check if nexus can be found
        list_run_object = LocateListRun(list_run = list_run)
        if list_run_object.list_run_not_found != []:
            str_list_run_not_found = [str(x) for x in list_run_object.list_run_not_found]
            runs_not_located = ', '.join(str_list_run_not_found)
            mess = "Can not locate %s run(s): %s" %(data_type, runs_not_located)
            self.parent.ui.reductionTable.item(row, 8).setText(mess)
            _color = QtGui.QColor(RefRed.colors.VALUE_BAD)
            self.parent.ui.reductionTable.item(row, 8).setBackground(_color)
        else:
            mess = "%s runs have been located!" %data_type
            self.parent.ui.reductionTable.item(row, 8).setText(mess)
            _color = QtGui.QColor(RefRed.colors.VALUE_OK)
            self.parent.ui.reductionTable.item(row, 8).setBackground(_color)
            
        list_run_found = list(list_run_object.list_run_found)

        if list_run_found == []:
            self.parent.ui.reductionTable.item(row, col).setText('')
            return
        str_list_run_found = [str(x) for x in list_run_found]
        final_list_run_found = ','.join(str_list_run_found)        
        self.parent.ui.reductionTable.item(row, col).setText(final_list_run_found)

        list_nexus_found = list_run_object.list_nexus_found
        self.parent.loading_nxs_thread = CheckListRunCompatibilityAndDisplayThread()
        self.parent.loading_nxs_thread.setup(parent=self.parent,
                       list_run = list_run_found,
                       list_nexus = list_nexus_found,
                       row = row,
                       col = col, 
                       is_working_with_data_column = is_data_displayed,
                       is_display_requested = self.display_of_this_row_checked())
        self.parent.loading_nxs_thread.start()

        return
        
        
        
        
        nxs_loader = CheckListRunCompatibility(list_run=_list_run)
        #if nxs_loader.no_nexus_found:
            #_color = QtGui.QColor(RefRed.colors.VALUE_BAD)
            #self.parent.ui.reductionTable.item(row, 8).setBackground(_color)
            #self.parent.ui.reductionTable.item(row, 8).setText(data_type + " not found !")
            #return
        
        is_nexus_found = False if nxs_loader.list_nexus_found == None else True
        if is_nexus_found is False:
            ClearPlots(self.parent, 
                       is_data = is_data_displayed,
                       is_norm = (not is_data_displayed),
                       plot_yt = True,
                       plot_yi = True,
                       plot_it = True,
                       plot_ix = True)     
            self.parent.ui.reductionTable.item(row,col).setText('')

            #create empty lconfig
            big_table_data = self.parent.big_table_data
            lconfig = big_table_data[row, 2]
            if lconfig is None:
                big_table_data[row, 2] = LConfigDataset()
            else:
                if is_data_displayed:
                    lconfig.data_runs_compatible = False
                else:
                    lconfig.norm_runs_compatible = False
            big_table_data[row, 2] = lconfig
            self.parent.big_table_data = big_table_data
            
            return

        self.update_lconfigdataset(nxs_loader)

        #if nxs_loader.runs_compatible:
            #_color = QtGui.QColor(RefRed.colors.VALUE_OK)
            #_message = data_type + " runs not compat. !"
        #else:
            #_color = QtGui.QColor(RefRed.colors.VALUE_BAD)
            #_message = ""
        #self.parent.ui.reductionTable.item(row, 8).setBackground(_color)
        ##self.parent.ui.reductionTable.item(row, message_col_index).setText(_message)
    
        if self.display_of_this_row_checked():
            DisplayReductionTable(parent=self.parent, 
                                  row=self.row,
                                  is_data_displayed=is_data_displayed)
        else:
            ClearPlots(self.parent, 
                       is_data = is_data_displayed,
                       is_norm = (not is_data_displayed),
                       plot_yt = True,
                       plot_yi = True,
                       plot_it = True,
                       plot_ix = True)
    
    def update_lconfigdataset(self, nxs_loader):
        list_nexus_found = nxs_loader.list_nexus_found
        list_run_found = nxs_loader.list_run_found
        list_wks = nxs_loader.list_wks
        runs_compatible = nxs_loader.runs_compatible
        
        _row = self.row
        big_table_data = self.parent.big_table_data
        
        if big_table_data[_row, 2] is None:
            _lconfig = LConfigDataset()
        else:
            _lconfig = big_table_data[_row, 2]
            
        if self.col == 1: #data
            _lconfig.data_full_file_name = list_nexus_found
            _lconfig.data_sets = list_run_found
            _lconfig.data_wks =  list_wks
            _lconfig.data_runs_compatible = runs_compatible
        else: #norm
            _lconfig.norm_full_file_name = list_nexus_found
            _lconfig.norm_sets = list_run_found
            _lconfig.norm_wks = list_wks
            _lconfig.norm_runs_compatible = runs_compatible
            
        big_table_data[_row, 2] = _lconfig
        self.parent.big_table_data = big_table_data

    def clear_cell(self):
        print('in clear cell')
        
    def display_of_this_row_checked(self):
        _button_status = self.parent.ui.reductionTable.cellWidget(self.row, 0).checkState()
        if _button_status == 2:
            return True
        return False
    