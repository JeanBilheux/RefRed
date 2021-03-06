import math
import os
import numpy as np
from random import randint
import nexus_utilities


def convert_angle(angle=0, from_units='degree', to_units='rad'):
    '''
    To convert angles from degree/rad to rad/degree
    '''

    if from_units == to_units:
        return angle

    if from_units == 'degree' and to_units == 'rad':
        coeff = math.pi / float(180)
    elif from_units == 'rad' and to_units == 'degree':
        coeff = float(180) / math.pi
    else:
        coeff = 1
    return float(angle) * coeff


def arrayByValue(array, value):
    for [index, _ele] in enumerate(array):
        array[index] = float(array[index]) * value
    return array


def convertTOF(TOFarray=None, from_units='micros', to_units='ms'):
    try:
        if TOFarray is None:
            return None
        if from_units == to_units:
            return TOFarray
        if from_units == 'micros':
            if to_units == 'ms':
                return arrayByValue(TOFarray, 0.001)
            else:
                raise NameError(to_units)
        elif from_units == 'ms':
            if to_units == 'micros':
                return arrayByValue(TOFarray, 1000)
            else:
                raise NameError(to_units)
        else:
            raise NameError(from_units)
    except NameError:
        print 'units not supported'
        return None


def output_2d_ascii_file(filename, image):
    f = open(filename, 'w')
    sz = image.shape
    dim1 = sz[0]
    dim2 = sz[1]
    for px in range(dim1):
        _line = ''
        for t in range(dim2):
            _line += str(image[px, t])
            _line += ' '
        _line += '\n'
        f.write(_line)
    f.close


def output_big_ascii_file(file_name,
                          x_axis,
                          y_axis,
                          y_error_axis):

    f = open(file_name, 'w')

    sz = y_axis.shape  # (nbr_pixel, nbr_tof)
    nbr_tof = sz[1]
    nbr_pixel = sz[0]
    f.write('#2D Pixel vs TOF (integrated over low resolution pixel range)')

    for t in range(nbr_tof):
        _tmp_str = str(x_axis[t])
        for x in range(nbr_pixel):
            _tmp_str += ' ,' + str(y_axis[x, t]) + " ," + str(y_error_axis[x, t])

        _tmp_str += '\n'
        f.write(_tmp_str)

    f.close


def output_ascii_file(file_name,
                      x_axis,
                      y_axis,
                      y_error_axis):

    f = open(file_name, 'w')

    sz_x_axis = len(x_axis)
    for i in range(sz_x_axis - 1):
        f.write(str(x_axis[i]) + "," + str(y_axis[i]) + "," + str(y_error_axis[i]) + "\n")

    f.close


def import_ascii_file(filename):
    try:
        f = open(filename, 'r')
        data = f.read()
        f.close()
    except:
        data = []
    return data


def output_big_Q_ascii_file(file_name,
                            x_axis,
                            y_axis,
                            y_error_axis):

    if os.path.isfile(file_name):
        os.remove(file_name)
    f = open(file_name, 'w')

    sz = y_axis.shape  # (nbr_pixel, nbr_tof)
    nbr_tof = sz[1]
    nbr_pixel = sz[0]

    for t in range(nbr_tof):
        _tmp_str = ''
        for x in range(nbr_pixel):
            _tmp_str += str(x_axis[x, t]) + ',' + str(y_axis[x, t]) + " ," + str(y_error_axis[x, t]) + ',,'
        _tmp_str += '\n'
        f.write(_tmp_str)

    f.close


def createPickleFilename(filename):
    '''
    will create the new pickeFilename based on the filename given
    (new extension but same base file name)
    '''
    filename, _ = os.path.splitext(filename)
    new_fileExtension = '_quicknx.dat'
    new_filename = filename + new_fileExtension
    return new_filename


def weighted_mean(data_array, error_array):
    '''
    weighted mean of an array
    '''
    sz = len(data_array)

    # calculate the numerator of mean
    dataNum = 0
    for i in range(sz):
        if not (data_array[i] == 0):
            tmpFactor = float(data_array[i]) / float((pow(error_array[i], 2)))
            dataNum += tmpFactor

    # calculate denominator
    dataDen = 0
    for i in range(sz):
        if not (error_array[i] == 0):
            tmpFactor = 1. / float((pow(error_array[i], 2)))
            dataDen += tmpFactor

    if dataDen == 0:
        mean = 0
        mean_error = 0
    else:
        mean = float(dataNum) / float(dataDen)
        mean_error = math.sqrt(1 / dataDen)

    return [mean, mean_error]


def write_ascii_file(filename, text):
    '''
    produce the output ascii file
    '''
    if os.path.isfile(filename):
        os.remove(filename)
    f = open(filename, 'w')
    for _line in text:
        f.write(_line + '\n')
    f.close()


def createAsciiFile(filename, str_list):
    if os.path.isfile(filename):
        os.remove(filename)
    f = open(filename, 'w')
    for _line in str_list:
        f.write(_line)
    f.close()


def weighted_sum(dataArray, errorArray, axisToSum=0):

    inputDim = len(dataArray.shape)

    if inputDim == 2:
        [sumArray, errorArray] = weighted_sum_dim2(dataArray, errorArray, axisToSum)
        return [sumArray, errorArray]
    elif inputDim == 3:
        [sumArray, errorArray] = weighted_sum_dim3(dataArray, errorArray, axisToSum)
        return [sumArray, errorArray]
    else:  # dim = 1
        [sumValue, errorValue] = weighted_sum_dim1(dataArray, errorArray)
        return [sumValue, errorValue]


def weighted_sum_dim3(dataArray, errorArray, axisToSum=0):
    _shapeArray = dataArray.shape
    _nbrElementAxis0 = _shapeArray[0]
    _nbrElementAxis1 = _shapeArray[1]
    _nbrElementAxis2 = _shapeArray[2]

    if axisToSum == 0:
        sumValueArray = np.zeros((_nbrElementAxis1, _nbrElementAxis2))
        sumErrorArray = np.zeros((_nbrElementAxis1, _nbrElementAxis2))

        for j in range(_nbrElementAxis2):
            [_value, _error] = weighted_sum_dim2(dataArray[:, :, j], errorArray[:, :, j], axisToSum)
            sumValueArray[:, j] = _value
            sumErrorArray[:, j] = _error
    elif axisToSum == 1:
        sumValueArray = np.zeros((_nbrElementAxis0, _nbrElementAxis2))
        sumErrorArray = np.zeros((_nbrElementAxis0, _nbrElementAxis2))

        for j in range(_nbrElementAxis0):
            [_value, _error] = weighted_sum_dim2(dataArray[j, :, :], errorArray[j, :, :], axisToSum - 1)
            sumValueArray[j, :] = _value
            sumValueArray[j, :] = _value

    else:  # axisToSum == 2
        sumValueArray = np.zeros((_nbrElementAxis0, _nbrElementAxis1))
        sumErrorArray = np.zeros((_nbrElementAxis0, _nbrElementAxis1))

        for j in range(_nbrElementAxis0):
            [_value, _error] = weighted_sum_dim2(dataArray[j, :, :], errorArray[j, :, :], axisToSum - 1)
            sumValueArray[j, :] = _value
            sumValueArray[j, :] = _value

    return [sumValueArray, sumErrorArray]


def weighted_sum_dim2(dataArray, errorArray, axisToSum=0):

    _shapeArray = dataArray.shape
    _nbrElementAxis0 = _shapeArray[0]
    _nbrElementAxis1 = _shapeArray[1]

    if axisToSum == 0:
        sumValueArray = np.zeros(_nbrElementAxis1)
        sumErrorArray = np.zeros(_nbrElementAxis1)

        for i in range(_nbrElementAxis1):
            [_value, _error] = weighted_sum_dim1(dataArray[:, i], errorArray[:, i])
            sumValueArray[i] = _value
            sumErrorArray[i] = _error
    else:
        sumValueArray = np.zeros(_nbrElementAxis0)
        sumErrorArray = np.zeros(_nbrElementAxis0)

        for i in range(_nbrElementAxis0):
            [_value, _error] = weighted_sum_dim1(dataArray[i, :], errorArray[i, :])
            sumValueArray[i] = _value
            sumErrorArray[i] = _error

    return [sumValueArray, sumErrorArray]


def weighted_sum_dim1(dataArray, errorArray):

    _sumValue = sum(dataArray)

    sz = len(dataArray)
    _tmpSumError = 0
    for i in range(sz):
        _tmpError = pow(errorArray[i], 2)
        _tmpSumError += _tmpError

    _sumError = math.sqrt(_tmpSumError)

    return [_sumValue, _sumError]


def generate_random_workspace_name():
    '''
    This will generate a random workspace name to avoid conflict names
    '''
    string = 'abcdefghijklmnopqrstuvwxyz1234567890'
    stringList = list(string)
    nbrPara = len(stringList)

    listRand = []
    for i in range(5):
        _tmp = stringList[randint(0, nbrPara - 1)]
        listRand.append(_tmp)

    randomString = ''.join(listRand)
    return randomString


def touch(full_file_name):
    with open(full_file_name, 'a'):
        os.utime(full_file_name, None)


def makeSureFileHasExtension(filename, default_ext=".xml"):
    _, file_extension = os.path.splitext(filename)
    if file_extension == '':
        filename += default_ext
    return filename


def findFullFileName(run_number):
    try:
        full_file_name = nexus_utilities.findNeXusFullPath(run_number)
    except:
        full_file_name = ''
    return full_file_name


def str2bool(v):
    try:
        return v.lower() in ("yes", "true", "t", "1")
    except:
        if float(v) == 0:
            return False
        else:
            return True


def removeEmptyStrElementAndUpdateIndexSelected(str_list, index_selected):
    sz = len(str_list)
    final_list = []
    final_index = index_selected
    for i in range(sz):
        _element = str_list[i]
        if _element.strip() != '':
            final_list.append(_element)
        else:
            if final_index >= i:
                final_index -= 1
    return [final_list, final_index]


def format_to_list(values):
    if type(values) == type([]):
        return values
    else:
        return [values]


def get_index_free_thread(parent=None):
    nbr_max_thread = len(parent.loading_nxs_thread)
    index_free_thread = parent.index_free_thread
    new_index = index_free_thread + 1
    if new_index == nbr_max_thread:
        new_index = 0
    parent.index_free_thread = new_index
    return new_index


def weighted_mean_default(data_array, error_array, error_0):

    sz = len(data_array)

    # calculate the numerator of mean
    dataNum = 0
    for i in range(sz):
        if (error_array[i] == 0):
            error_array[i] = error_0

        tmpFactor = float(data_array[i]) / float((pow(error_array[i], 2)))
        dataNum += tmpFactor

    # calculate denominator
    dataDen = 0
    for i in range(sz):
        if (error_array[i] == 0):
            error_array[i] = error_0
        tmpFactor = 1. / float((pow(error_array[i], 2)))
        dataDen += tmpFactor

    if dataDen == 0:
        data_mean = np.nan
        mean_error = np.nan
    else:
        data_mean = float(dataNum) / float(dataDen)
        mean_error = math.sqrt(1 / dataDen)

    return [data_mean, mean_error]
