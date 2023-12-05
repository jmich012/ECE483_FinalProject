import sys

accel_dev = "/dev/IntelFPGAUP/accel"
accel_file = None

def open_dev( ):
   ''' Opens the 3D-accelerometer accel device
   
   :return: 1 on success, else 0
   '''
   global accel_file
   try:
      accel_file = open(accel_dev, 'rb+')
   except IOError:
      sys.stderr.write("ERROR: {} driver does not exist.\n".format(accel_dev))
      accel_file = None
       return 0
   return 1

def read( ):
   ''' Reads the accel device
   
   :return: seven integers: ready (1 if new acceleration data is available, else 0),
      tap (1 if tap event, else 0), dtap (1 if double-tap event, else 0), 
      x (acceleration in the x axis), y (... y axis), z (... z axis), 
      scale (mG per lsb scale factor for acceleration data)
   '''
   global accel_file
   if accel_file is not None:
      accel_buffer = accel_file.read()
      groups = accel_buffer.split()   # int_source x y z scale
      int_source, x, y, z, scale = int(groups[0], base=16), int(groups[1]), int(groups[2]), \
         int(groups[3]), int(groups[4])
      ready = tap = dtap = 0
      if ((int_source & 0x80) != 0):
         ready = 1
      if (((int_source & 0x40) or (int_source & 0x20)) != 0):
         tap = 1
      if ((int_source & 0x20) != 0):
         dtap = 1
      return ready, tap, dtap, x, y, z, scale

def init( ):
   ''' Initializes the 3D-acceleration device
   
   :return: none
   '''
   global accel_file
   if accel_file is not None:
      accel_file.write('init')
      accel_file.flush()

def calibrate( ):
   ''' Calibrates the 3D-acceleration device
   
   :return: none
   '''
   global accel_file
   if accel_file is not None:
      accel_file.write('calibrate')
      accel_file.flush()

def device( ):
   ''' Request printing of the device ID from the 3D-acceleration device
   
   :return: none
   '''
   global accel_file
   if accel_file is not None:
      accel_file.write('device')
      accel_file.flush()

def format(full, range):
   ''' Sets the format of acceleration data
   
   :param full: integer value of 1 sets full resolution
   :param range: integer to set the G range to {2, 4, 8, 16}
   :return: none
   '''
   global accel_file
   if accel_file is not None:
      accel_file.write("format %d %d" % (full, range))
      accel_file.flush()

def rate(rate):
   ''' Sets the data rate of acceleration data
   
   :param rate: float value to set rate to {25,12.5,6.25,1.56,0.78} Hz
   :return: none
   '''
   global accel_file
   if accel_file is not None:
      accel_file.write("rate %s" % (rate))
      accel_file.flush()

def close( ):
   ''' Closes the accel device
   
   :return: none
   '''
   global accel_file
   accel_file.close()
   accel_file = None
