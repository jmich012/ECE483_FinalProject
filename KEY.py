import sys

KEY_dev = "/dev/IntelFPGAUP/KEY"
KEY_file = None

def open_dev( ):
   ''' Opens the pushbutton KEY device
   
   :return: 1 on success, else 0
   '''
   global KEY_file
   try:
       KEY_file = open(KEY_dev, 'rb+')
   except IOError:
       sys.stderr.write("ERROR: {} driver does not exist.\n".format(KEY_dev))
       KEY_file = None
       return 0
   return 1

def read( ):
   ''' Reads the pushbutton KEY device
   
   :return: integer reflecting the KEY settings
   '''
   global KEY_file
   if KEY_file is not None:
      return int(KEY_file.read().strip(), 16)

def close( ):
   ''' Closes the pushbutton KEY device
   
   :return: none
   '''
   global KEY_file
   KEY_file.close()
   KEY_file = None
   
