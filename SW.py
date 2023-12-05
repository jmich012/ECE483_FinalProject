import sys

SW_dev = "/dev/IntelFPGAUP/SW"
SW_file = None

def open_dev( ):
   ''' Opens the slide switch SW device
   
   :return: 1 on success, else 0
   '''
   global SW_file
   try:
       SW_file = open(SW_dev, 'rb+')
   except IOError:
       sys.stderr.write("ERROR: {} driver does not exist.\n".format(SW_dev))
       SW_file = None
       return 0
   return 1

def read( ):
   ''' Reads the slide switch SW device
   
   :return: integer reflecting the SW switch settings
   '''
   global SW_file
   if SW_file is not None:
      return int(SW_file.read().strip(), 16)

def close( ):
   ''' Closes the slide switch SW device
   
   :return: none
   '''
   global SW_file
   SW_file.close()
   SW_file = None
   
