from PyQt4 import QtGui, QtCore
from table_reduction_runs_editor_interface_refl import Ui_MainWindow
from run_sequence_breaker import RunSequenceBreaker
from decorators import waiting_effects
from mantid.simpleapi import *
from selection_bigTable_changed import SelectionBigTableChanged
import nexus_utilities
import utilities


class TableReductionRunEditor(QtGui.QMainWindow):
	
	_open_instances = []
	main_gui = None
	col = 0
	row = 0
	is_working_with_data = True
	lambda_requested = 'N/A'
	at_least_one_same_lambda = False
	valid_runs = []
	
	list_filename = []
	list_nxs = []
	list_runs = []
	str_list_runs = []
	
	def __init__(cls, parent=None, col=0, row=0):
		cls.main_gui = parent
		cls.col = col
		cls.row = row
		
		if col != 0:
			cls.is_working_with_data = False
		
		QtGui.QMainWindow.__init__(cls, parent=parent)
		cls.setWindowModality(False)
		cls._open_instances.append(cls)
		cls.ui = Ui_MainWindow()
		cls.ui.setupUi(cls)
		cls.initGui()
		
	def initGui(cls):
		cls.initLayout()
		cls.initContent()
		
	def initContent(cls):
		cls.ui.lambdaUnits.setText(u'\u00c5')
		
		palette_green = QtGui.QPalette()
		palette_green.setColor(QtGui.QPalette.Foreground, QtCore.Qt.darkGreen)
		cls.ui.validRunLabel.setPalette(palette_green)
		
		palette_red = QtGui.QPalette()
		palette_red.setColor(QtGui.QPalette.Foreground, QtCore.Qt.red)
		cls.ui.invalidRunLabel.setPalette(palette_red)

		verticalHeader = ["Data Run #", u'Lambda Requested (\u00c5)', 
		                  'Norm Run', u'Lambda Requested (\u00c5)']
		cls.ui.tableWidget.setHorizontalHeaderLabels(verticalHeader)
		cls.ui.tableWidget.resizeColumnsToContents()
		
		data_run = cls.main_gui.ui.reductionTable.item(cls.row, 0).text()
		norm_run = cls.main_gui.ui.reductionTable.item(cls.row, 6).text()
		if cls.col == 0:
			cls.ui.oldDataRun.setText(data_run)
			cls.ui.normRun.setText(norm_run)
		else:
			cls.ui.dataRun.setText(data_run)
			cls.ui.oldNormRun.setText(norm_run)
			
		config = cls.main_gui.bigTableData[cls.row, 2]

		lambda_value = cls.retrieveLambdaRequestedForThisRow()
		cls.lambda_requested = lambda_value
		cls.ui.lambdaValue.setText(lambda_value)

	def  retrieveLambdaRequestedForThisRow(cls):
		lambda_requested = ''
		bigTable = cls.main_gui.bigTableData
		
		# try to retrieve from bigTable[i,0]
		data_obj = bigTable[cls.row, 0]
		if data_obj is not None:
			_active_data = data_obj.active_data
			return str(_active_data.lambda_requested)
		
		# try to retrieve from bigTable[i,2] -> data_lambda_requested
		config_obj = bigTable[cls.row, 2]
		if (config_obj.data_lambda_requested != -1) and (config_obj.data_lambda_requested != '') :
			return str(config_obj.data_lambda_requested)
		
		# try to retrieve from bigTable[i,1]
		norm_obj = bigTable[cls.row, 1]
		if norm_obj is not None:
			_active_norm = norm_obj.active_data
			return str(_active_norm.lambda_requested)
		
		# try to retrieve from bigTable[i,2] -> norm_lambda_requested
		if (config_obj.norm_lambda_requested != -1) and (config_obj.data_lambda_requested != ''):
			return str(config_obj.norm_lambda_requested)
		
		# try from data_run, if not None -> load and retrieve
		data_run = cls.main_gui.ui.reductionTable.item(cls.row, 0).text()
		if data_run != '':
			try:
				_filename = nexus_utilities.findNeXusFullPath(data_run)
				cls.list_filename.append(_filename)
				randomString = utilities.generate_random_workspace_name()
				_nxs = LoadEventNexus(Filename=_filename, OutputWorkspace=randomString, MetaDataOnly=True)
				return str(_nxs.getRun().getProperty('LambdaRequest').value[0])
			except:
				pass
		
		# try from norm_run, if not None -> load and retrieve
		norm_run = cls.main_gui.ui.reductionTable.item(cls.row, 6).text()
		if norm_run != '':
			try:
				_filename = nexus_utilities.findNeXusFullPath(norm_run)
				cls.list_filename.append(_filename)
				randomString = utilities.generate_random_workspace_name()
				_nxs = LoadEventNexus(Filename=_filename, OutputWorkspace=randomString, MetanormOnly=True)
				return str(_nxs.getRun().getProperty('LambdaRequest').value[0])
			except:
				pass
		
		# give up and return 'N/A'
		return 'N/A'

	def initLayout(cls):
		if cls.col == 0: #data then hide norm frame
			cls.ui.norm_groupBox.setHidden(True)
		else:
			cls.ui.data_groupBox.setHidden(True)
			
	@waiting_effects		
	def dataLineEditValidate(cls):
		run_sequence = cls.ui.dataLineEdit.text()
		oListRuns = RunSequenceBreaker(run_sequence)
		_list_runs = oListRuns.getFinalList()
		cls.list_runs = _list_runs
		cls.ui.dataLineEdit.setText("")

		cls.list_filename = []
		cls.list_nxs = []
		if _list_runs[0] == -1:
			return
		for _runs in _list_runs:
			try:
				_filename = nexus_utilities.findNeXusFullPath(_runs)
			except:
				pass
			else:
				cls.list_filename.append(_filename)
				randomString = utilities.generate_random_workspace_name()
				_nxs = LoadEventNexus(Filename=_filename, OutputWorkspace=randomString, MetaDataOnly=True)
				cls.list_nxs.append(_nxs)
				cls.str_list_runs.append(str(_runs))
			
		cls.updateDataTable()
		cls.updateInsertValidRunsButton()
		
	@waiting_effects
	def normLineEditValidate(cls):
		_run = cls.ui.normLineEdit.text()
		cls.ui.normLineEdit.setText("")
		if _run == '':
			return
		cls.list_runs = [_run]
		try:
			_filename = nexus_utilities.findNeXusFullPath(_run)
		except:
			pass
		else:
			cls.list_filename.append(_filename)
			randomString = utilities.generate_random_workspace_name()
			_nxs = LoadEventNexus(Filename=_filename, OutputWorkspace=randomString, MetaDataOnly=True)
			cls.list_nxs = [_nxs]
			cls.str_list_runs.append(str(_run))
			
		cls.updateNormTable()
		cls.updateInsertValidRunsButton()
		
	def updateInsertValidRunsButton(cls):
		cls.ui.insertValidRunsButton.setEnabled(cls.at_least_one_same_lambda)
		
	@waiting_effects
	def insertValidRunsButton(cls):
		''' Reach by the valid button '''
		_valid_runs = cls.valid_runs
		cls.replaceRunsIntoMainGui(_valid_runs)
		cls.close()
		cls.replotMainGuiSelectedField()
		
	def replotMainGuiSelectedField(cls):
		if cls.col != 0:
			_col = 6
		else:
			_col = 0
		cls.main_gui._cur_column_selected = _col
		cls.main_gui._cur_row_selected = cls.row
		SelectionBigTableChanged(cls.main_gui)
		
	def replaceRunsIntoMainGui(cls, _valid_runs):
		cls.updateReductionTable(_valid_runs)
		cls.updateConfigObject()
		cls.updateBigTableData()
		
	def updateBigTableData(cls):
		_row = cls.row
		_col = cls.col
		bigTableData = cls.main_gui.bigTableData
		bigTableData[_row,_col] = None
		cls.main_gui.bigTableData = bigTableData
		
	def updateConfigObject(cls):
		_row = cls.row
		bigTableData = cls.main_gui.bigTableData
		config_object = bigTableData[_row, 2]
		if cls.is_working_with_data:
			config_object.data_sets = ",".join(cls.str_list_runs)
			config_object.data_full_file_name = ",".join(cls.list_filename)
		else:
			config_object.norm_sets = ",".join(cls.str_list_runs)
			config_object.norm_full_file_name = ",".join(cls.list_filename)
		bigTableData[_row,2] = config_object
		cls.main_gui.bigTableData = bigTableData
		
	def updateReductionTable(cls, _valid_runs):
		_col = cls.col
		if _col != 0:
			_col = 6
		_row = cls.row
		new_runs = ",".join(_valid_runs)
		_item = QtGui.QTableWidgetItem(str(new_runs))
		cls.main_gui.ui.reductionTable.setItem(_row, _col, _item)

	def updateDataTable(cls):
		lambda_requested = str(cls.ui.lambdaValue.text())
		cls.at_least_one_same_lambda = False
		cls.valid_runs = []

		cls.clearTable()
		cls.ui.tableWidget.clearContents()
		nbr_row = len(cls.list_nxs)
		_runs = cls.list_runs
		for _row in range(nbr_row):
			cls.ui.tableWidget.insertRow(_row)
			same_lambda_flag = False

			_nxs = cls.list_nxs[_row]
			_run = _runs[_row]

			_lambda =  str(cls.retrieveMetadataFromNxs(_nxs, 'LambdaRequest'))
			if lambda_requested == 'N/A/':
				same_lambda_flag = False
			elif lambda_requested == _lambda:
				same_lambda_flag = True
				cls.at_least_one_same_lambda = True
				cls.valid_runs.append(str(_run))
				
			cls.addItemToTable(value=_run, row=_row, column=0, isSameLambda=same_lambda_flag)
			cls.addItemToTable(value=_lambda, row=_row, column=1, isSameLambda=same_lambda_flag)
		
	def updateNormTable(cls):
		lambda_requested = str(cls.ui.lambdaValue.text())
		cls.at_least_one_same_lambda = False
		cls.clearTable()
		cls.ui.tableWidget.clearContents()

		cls.ui.tableWidget.insertRow(0)
		same_lambda_flag = False
		
		_nxs = cls.list_nxs[0]
		_run = cls.list_runs[0]
		_lambda =  str(cls.retrieveMetadataFromNxs(_nxs, 'LambdaRequest'))
		if lambda_requested == 'N/A/':
			same_lambda_flag = False
		elif lambda_requested == _lambda:
			same_lambda_flag = True
			cls.at_least_one_same_lambda = True
			cls.valid_runs.append(_run)
			
		cls.addItemToTable(value=_run, row=0, column=0, isSameLambda=same_lambda_flag)
		cls.addItemToTable(value=_lambda, row=0, column=1, isSameLambda=same_lambda_flag)
			
	def 	clearTable(cls):
		nbr_row = cls.ui.tableWidget.rowCount()
		if nbr_row > 0:
			for i in range(nbr_row):
				cls.ui.tableWidget.removeRow(i)
		
	def retrieveMetadataFromNxs(cls, nexus=None, tag=''):
		if nexus is None:
			return ''
		mt_run = nexus.getRun()
		return mt_run.getProperty(tag).value[0]
			
	def addItemToTable(cls, value='', row=0, column=0, isSameLambda=False):
		if isSameLambda:
			color = QtGui.QColor(0,255,0)
		else:
			color = QtGui.QColor(255,0,0)
		_item = QtGui.QTableWidgetItem(str(value))
		_item.setForeground(color)
		
		cls.ui.tableWidget.setItem(row, column, _item)
				
	def closeEvent(cls, event=None):
		cls.close()
	
	