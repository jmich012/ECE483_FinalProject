import sys

LEDR_dev = "/dev/IntelFPGAUP/LEDR"
LEDR_file = None

def open_dev( ):
   ''' Opens the red light LEDR device
   
   :return: 1 on success, else 0
   '''
   global LEDR_file
   try:
       LEDR_file = open(LEDR_dev, 'rb+')
   except IOError:
       sys.stderr.write("ERROR: {} driver does not exist.\n".format(LEDR_dev))
       LEDR_file = None
       return 0
   return 1

def set(data):
   ''' Sets the red light LEDR device
   
	:param data: the integer data to write to LEDR
   :return: none
   '''
   global LEDR_file
   if LEDR_file is not None:
      LEDR_file.write(hex(data)[2:]) # convert to hex string; skip the leading 0x
      LEDR_file.flush()

def close( ):
   ''' Closes the red light LEDR device
   
   :return: none
   '''
   global LEDR_file
   LEDR_file.close()
   LEDR_file = None
