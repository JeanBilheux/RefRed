from RefRed.plot.display_plots import DisplayPlots
from RefRed.gui_handling.gui_utility import GuiUtility

class SpinBox(object):
    
    parent = None
    
    def __init__(self, parent=None, is_data=True, entry_type='peak', value_min=-1, value_max=-1):
        self.parent = parent
        big_table_data = parent.big_table_data
        gui_utility = GuiUtility(self.parent)
        row = gui_utility.get_current_table_reduction_check_box_checked()
        
        if row == -1:
            return
        
        if is_data:
            index = 0
        else:
            index = 1
        data = big_table_data[row, index]
        
        val1 = value_min
        val2 = value_max

        if (val1 > val2):
            val_min = val2
            val_max = val1
        else:
            val_min = val1
            val_max = val2
        
        is_plot_yt = True
        is_plot_yi = True
        is_plot_it = False
        is_plot_ix = False
        if entry_type == 'data':
            data.peak = [str(val_min), str(val_max)]
        elif entry_type == 'norm':
            data.back = [str(val_min), str(val_max)]
        else:
            is_plot_yt = False
            is_plot_yi = False
            is_plot_ix = True
            data.low_res = [str(val_min), str(val_max)]
            
        big_table_data[row, index] = data
        self.parent.big_table_data = big_table_data
                
        DisplayPlots(parent = self.parent,
                     row = row,
                     is_data = is_data,
                     plot_yt = is_plot_yt,
                     plot_yi = is_plot_yi,
                     plot_it = is_plot_it,
                     plot_ix = is_plot_ix,
                     refresh_reduction_table = False)

class DataSpinbox(object):

    def __init__(self, parent=None, entry_type='peak', value_min=-1, value_max=-1):
        SpinBox(parent = parent, 
                is_data = True,
                entry_type = entry_type,
                value_min = value_min,
                value_max = value_max)

class NormSpinbox(object):
    
    def __init__(self, parent=None, entry_type='peak', value_min=-1, value_max=-1):
        SpinBox(parent = parent, 
                is_data = False,
                entry_type = entry_type,
                value_min = value_min,
                value_max = value_max)

class DataPeakSpinbox(object):
    
    parent = None
    
    def __init__(self, parent=None):
        self.parent = parent
        peak1 = self.parent.ui.dataPeakFromValue.value()
        peak2 = self.parent.ui.dataPeakToValue.value()
        DataSpinbox(parent = parent,
                    entry_type = 'peak',
                    value_min = peak1,
                    value_max = peak2)
       
class DataBackSpinbox(object):
    
    parent = None
    
    def __init__(self, parent=None):
        self.parent = parent
        back1 = self.parent.ui.dataBackFromValue.value()
        back2 = self.parent.ui.dataBackToValue.value()
        DataSpinbox(parent = parent,
                    entry_type = 'back',
                    value_min = back1,
                    value_max = back2)

class NormPeakSpinbox(object):

    Parent = None
    
    def __init__(self, parent=None):
        self.parent = parent
        peak1 = self.parent.ui.normPeakFromValue.value()
        peak2 = self.parent.ui.normPeakToValue.value()
        NormSpinbox(parent = parent,
                    entry_type = 'peak',
                    value_min = peak1,
                    value_max = peak2)
       
class NormBackSpinbox(object):
    
    parent = None
    
    def __init__(self, parent=None):
        self.parent = parent
        back1 = self.parent.ui.normBackFromValue.value()
        back2 = self.parent.ui.normBackToValue.value()
        NormSpinbox(parent = parent,
                    entry_type = 'back',
                    value_min = back1,
                    value_max = back2)

class DataLowResSpinbox(object):
    
    parent = None
    
    def __init__(self, parent=None):
        self.parent = parent
        lowres1 = self.parent.ui.dataLowResFromValue.value()
        lowres2 = self.parent.ui.dataLowResToValue.value()
        DataSpinbox(parent = parent,
                    entry_type = 'low_res',
                    value_min = lowres1,
                    value_max = lowres2)

class NormLowResSpinbox(object):
    
    parent = None
    
    def __init__(self, parent=None):
        self.parent = parent
        lowres1 = self.parent.ui.normLowResFromValue.value()
        lowres2 = self.parent.ui.normLowResToValue.value()
        NormSpinbox(parent = parent,
                    entry_type = 'low_res',
                    value_min = lowres1,
                    value_max = lowres2)
        