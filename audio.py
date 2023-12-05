import sys

audio_dev = "/dev/IntelFPGAUP/audio"
audio_file = None

MAX_VOLUME = 0x7FFFFFFF
MAX_SAMPLING_RATE, MID_SAMPLING_RATE, MIN_SAMPLING_RATE = 48000, 32000, 8000

def open_dev( ):
   ''' Opens the digital audio device
   
   :return: 1 on success, else 0
   '''
   global audio_file
   try:
      audio_file = open(audio_dev, 'rb+')
   except IOError:
      sys.stderr.write("ERROR: {} driver does not exist.\n".format(audio_dev))
      audio_file = None
      return 0
   return 1

def read( ):
   ''' Reads the audio device
   
   :return: two integers: left-channel data, right-channel data
   '''
   global audio_file
   if audio_file is not None:
      audio_buffer = audio_file.read()
      groups = audio_buffer.split()   # left right
      left, right = int(groups[0]), int(groups[1])
      return left, right

def init( ):
   ''' Initializes the audio device
   
   :return: none
   '''
   global audio_file
   if audio_file is not None:
      audio_file.write('init')
      audio_file.flush()

def sampling_rate(data):
   ''' Sets the audio device sampling rate
   
   :param data: sampling rate in thousands/sec. Valid data = {8000, 32000, 48000)
   :return: none
   '''
   global audio_file
   if audio_file is not None:
      audio_file.write("rate %d" % (data))
      audio_file.flush()

def wait_write( ):
   ''' Waits for space to be available for writing to the audio device
   
   :return: none
   '''
   global audio_file
   if audio_file is not None:
      audio_file.write('waitw')
      audio_file.flush()

def wait_read( ):
   ''' Waits until data is available for reading from the audio device
   
   :return: none
   '''
   global audio_file
   if audio_file is not None:
      audio_file.write('waitr')
      audio_file.flush()

def write_left(data):
   ''' Writes data to the left audio channel
   
   :param data: integer value to be written
   :return: none
   '''
   global audio_file
   if audio_file is not None:
      audio_file.write("left %d" % (data))
      audio_file.flush()

def write_right(data):
   ''' Writes data to the right audio channel
   
   :param data: integer value to be written
   :return: none
   '''
   global audio_file
   if audio_file is not None:
      audio_file.write("right %d" % (data))
      audio_file.flush()

def close( ):
   ''' Closes the audio device
   
   :return: none
   '''
   global audio_file
   audio_file.close()
   audio_file = None
