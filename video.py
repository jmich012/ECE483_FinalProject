import sys

video_dev = "/dev/IntelFPGAUP/video"
video_file = None

# define some graphics colors
WHITE, YELLOW, RED, GREEN, BLUE, CYAN, MAGENTA, GREY, PINK, ORANGE = \
   0xFFFF, 0xFFE0, 0xF800, 0x07E0, 0x041F, 0x07FF, 0xF81F, 0xC618, 0xFC18, 0xFC00

def open_dev( ):
   ''' Opens the VGA video device
   
   :return: 1 on success, else 0
   '''
   global video_file
   try:
       video_file = open(video_dev, 'rb+')
   except IOError:
       sys.stderr.write("ERROR: {} driver does not exist.\n".format(video_dev))
       video_file = None
       return 0
   return 1

def read( ):
   ''' Reads the video device
   
   :return: four integers: screen_x (x resolution), screen_x (y resolution), 
      char_x (# of text columns), char_y (# of text lines)
   '''
   global video_file
   if video_file is not None:
      video_buffer = video_file.read()
      groups = video_buffer.split()   # columns rows tcols trows
      return int(groups[0]), int(groups[1]), int(groups[2]), int(groups[3])

def clear( ):
   ''' Erases all graphics in the current video frame buffer
   
   :return: none
   '''
   global video_file
   if video_file is not None:
      video_file.write('clear')
      video_file.flush()

def pixel(x, y, color):
   ''' Sets the pixel at coordinates (x, y) to color
   
   :param x: the column
   :param y: the row
   :param color: 16-bit VGA color
   :return: none
   '''
   global video_file
   if video_file is not None:
      video_file.write("pixel %03d,%03d %04X" % (x, y, color))
      video_file.flush()

def line(x1, y1, x2, y2, color):
   ''' Draws a color line from graphics point (x1, y1) to (x2, y2)
   
   :param x1: the column for one end of the line
   :param y1: the row for one end of the line
   :param x2: the column for the other end of the line
   :param y2: the row for the other end of the line
   :param color: 16-bit VGA color
   :return: none
   '''
   global video_file
   if video_file is not None:
      video_file.write("line %03d,%03d %03d,%03d %04X" % (x1, y1, x2, y2, color))
      video_file.flush()

def box(x1, y1, x2, y2, color):
   ''' Draws a filled color box from corner (x1, y1) to corner (x2, y2)
 
   :param x1: the column for one corner
   :param y1: the row for one corner
   :param x2: the column for the other corner
   :param y2: the row for the other corner
   :param color: 16-bit VGA color
   :return: none
   '''
   global video_file
   if video_file is not None:
      video_file.write("box %03d,%03d %03d,%03d %04X" % (x1, y1, x2, y2, color))
      video_file.flush()

def text(x, y, msg):
   ''' Draws the text msg at character coordinates (x, y)

   :param x: the character column
   :param y: the character row
   :param msg: the text string
   :return: none
   '''
   global video_file
   if video_file is not None:
      video_file.write("text %03d,%03d %s" % (x, y, msg))
      video_file.flush()

def erase( ):
   ''' Erases all text in the video character buffer
   
   :return: none
   '''
   global video_file
   if video_file is not None:
      video_file.write('erase')
      video_file.flush()

def show( ):
   ''' Swaps the front/back video frame buffers
   
   :return: none
   '''
   global video_file
   if video_file is not None:
      video_file.write('sync')
      video_file.flush()

def close( ):
   ''' Closes the video device
   
   :return: none
   '''
   global video_file
   video_file.close()
   video_file = None
