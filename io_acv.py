import struct
from pathlib import Path

binary_file_empty = "empty-curve.acv"
binary_file_full = "dotgain corrected test.acv"
binary_file_5ch = "5channelcurve.acv"

def read_ints(data, offset, count):
    result = []
    for i in range(count):
        result.append(int.from_bytes(data[offset:offset+2], byteorder="big", signed=False))
        offset = offset + 2

    return result

def checkNullCurve(ints):
    if ints == [2, 0]:
        return True
    else: 
        return False

def readACVFile(filepath):
    with open(filepath, 'rb') as file:
        data = Path(filepath).read_bytes()

    data_length = len(data)
    offset = 4 # skip version and curve count
    data_array = []

    while offset < data_length:
        # we got curve data!
        curve_point_count = read_ints(data, offset, 1)[0]
        if curve_point_count != 0:
            curve_data = read_ints(data, offset+2, curve_point_count*2)
            data_array.append(curve_data)
            offset = offset + ((curve_point_count * 2) + ((curve_point_count*2)+2) )
            continue
        else:
            offset = offset + 4
    return data_array

def readACVFileRaw(filepath):
    with open(filepath, 'rb') as file:
        data = Path(filepath).read_bytes()

    data_length = len(data)
    offset = 0
    data_array = []

    while offset < data_length:
        data_array.append(read_ints(data, offset, data_length))
        offset += 2
    return data_array

def saveACVFile(filepath, curve_array):
    curve_count = len(curve_array)
    binary_data = []
    header = []

    # construct header
    header.append(b'\x00\x04') #version number  
    header.append(struct.pack(">H", curve_count)) #curve count 
    header = b"".join(header)
    binary_data.append(header)

    # construct data
    for curve in curve_array:
        pair_count = int(len(curve)/2)
        binary_data.append(struct.pack(">H", pair_count))
        for integer in curve:
            binary_data.append(struct.pack(">H", integer))

    binary_data = b"".join(binary_data)

    with open(filepath, 'wb') as file:
        file.write(binary_data)

