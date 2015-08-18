from RefRed.compare_two_nxsdata_for_sfcalculator import CompareTwoNXSDataForSFcalculator
from RefRed.qreduce import NXSData

class Position(object):
	before = -1
	same = 0
	after = 1

class SortNXSData(object):

	sortedArrayOfNXSData = None
	sf_gui = None
	
        def __init__(cls, arrayOfNXSDataToSort, parent=None): 
		nbr_runs = len(arrayOfNXSDataToSort)
		if nbr_runs<2:
 			cls.sortedArrayOfNXSData = arrayOfNXSDataToSort
						
		cls.sf_gui = parent
		_sortedArrayOfNXSData = [arrayOfNXSDataToSort[0]]
		_positionIndexNXSDataToPosition=0
    		
		for source_index in range(1,nbr_runs):
			_is_same_nxs = False
			_nxsdataToPosition = arrayOfNXSDataToSort[source_index]
			for indexInPlace in range(len(_sortedArrayOfNXSData)):
				_nxsdataToCompareWith = _sortedArrayOfNXSData[indexInPlace]
				compareTwoNXSData = CompareTwoNXSDataForSFcalculator(_nxsdataToCompareWith, _nxsdataToPosition)
				_isBeforeSameOrAfter = compareTwoNXSData.result()
				if _isBeforeSameOrAfter == Position.before:
					_positionIndexNXSDataToPosition = indexInPlace
					break
				elif _isBeforeSameOrAfter == Position.after:
					_positionIndexNXSDataToPosition += 1
				else:
					_new_nxsdata = cls.mergedNXSData(_nxsdataToPosition, _nxsdataToCompareWith)
					_sortedArrayOfNXSData[indexInPlace] = _new_nxsdata
					_is_same_nxs = True
					break
			if not _is_same_nxs:
				_sortedArrayOfNXSData.insert(_positionIndexNXSDataToPosition, _nxsdataToPosition)
		cls.sortedArrayOfNXSData = _sortedArrayOfNXSData	
					
	def mergedNXSData(cls, nxsdata1, nxsdata2):
		_full_file_name1 = nxsdata1.active_data.filename
		_full_file_name2 = nxsdata2.active_data.filename
		_new_nxsdata =  NXSData([_full_file_name1, _full_file_name2], bins=cls.sf_gui.bin_size, is_auto_peak_finder=True)
		return _new_nxsdata
	
	def getSortedList(cls):
		return cls.sortedArrayOfNXSData