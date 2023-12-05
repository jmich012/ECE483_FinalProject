import sys

HEX_dev = "/dev/IntelFPGAUP/HEX"
HEX_file = None

def open_dev( ):
   ''' Opens the 7-segment displays HEX device
   
   :return: 1 on success, else 0
   '''
   global HEX_file
   try:
       HEX_file = open(HEX_dev, 'rb+')
   except IOError:
       sys.stderr.write("ERROR: {} driver does not exist.\n".format(HEX_dev))
       HEX_file = None
       return 0
   return 1

def set(data):
   ''' Sets the HEX device in decimal number mode
   
   :param data: an integer to be displayed as a 6-digit decimal number. The upper
      two digits will be displayed on HEX5-4, and the lower four on HEX3-0
   :return: none
   '''
   global HEX_file
   if HEX_file is not None:
      HEX_file.write(format(data,'06d'))
      HEX_file.flush()

def raw(data1, data2):
   ''' Sets the HEX device in raw mode
   
   :param data1: an integer that is written to HEX5-4 as raw bits
   :param data2: an integer that is written to HEX3-0 as raw bits
   :return: none
   '''
   global HEX_file
   if HEX_file is not None:
      HEX_file.write('-r ' + format(data1,'04x') + ' ' + format(data2,'08x'))
      HEX_file.flush()

def close( ):
   ''' Closes the HEX device
   
   :return: none
   '''
   global HEX_file
   HEX_file.close()
   HEX_file = None
