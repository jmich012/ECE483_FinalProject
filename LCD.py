import sys

LCD_dev = "/dev/IntelFPGAUP/LCD"
LCD_file = None

def open_dev( ):
   ''' Opens the LCD device
   
   :return: 1 on success, else 0
   '''
   global LCD_file
   try:
       LCD_file = open(LCD_dev, 'rb+')
   except IOError:
       sys.stderr.write("ERROR: {} driver does not exist.\n".format(LCD_dev))
       LCD_file = None
       return 0
   return 1

def read( ):
   ''' Reads the LCD device
   
   :return: four integers: screen_x (x resolution), screen_x (y resolution), 
      char_x (# of text columns), char_y (# of text lines)
   '''
   global LCD_file
   if LCD_file is not None:
      LCD_buffer = LCD_file.read()
      groups = LCD_buffer.split()   # columns rows tcols trows
      return int(groups[0]), int(groups[1]), int(groups[2]), int(groups[3])

def clear( ):
   ''' Erases all graphics in the LCD frame buffer
   
   :return: none
   '''
   global LCD_file
   if LCD_file is not None:
      LCD_file.write('clear')
      LCD_file.flush()

def pixel(x, y, color):
   ''' Sets the pixel at coordinates (x, y) to color
   
   :param x: the column
   :param y: the row
	:param color: LCD 16-bit color (all colors display as black except 0)
   :return: none
   '''
   global LCD_file
   if LCD_file is not None:
      LCD_file.write("pixel %03d,%03d %04X" % (x, y, color))
      LCD_file.flush()

def line(x1, y1, x2, y2, color):
   ''' Draws a color line from graphics point (x1, y1) to (x2, y2)
   
   :param x1: the column for one end of the line
   :param y1: the row for one end of the line
   :param x2: the column for the other end of the line
   :param y2: the row for the other end of the line
   :param color: 16-bit color
   :return: none
   '''
   global LCD_file
   if LCD_file is not None:
      LCD_file.write("line %03d,%03d %03d,%03d %04X" % (x1, y1, x2, y2, color))
      LCD_file.flush()

def box(x1, y1, x2, y2, color):
   ''' Draws a filled box from corner (x1, y1) to corner (x2, y2)
 
   :param x1: the column for one corner
   :param y1: the row for one corner
   :param x2: the column for the opposite corner
   :param y2: the row for the opposite corner
   :param color: 16-bit color
   :return: none
   '''
   global LCD_file
   if LCD_file is not None:
      LCD_file.write("box %03d,%03d %03d,%03d %04X" % (x1, y1, x2, y2, color))
      LCD_file.flush()

def text(x, y, msg):
   ''' Draws the text msg at character coordinates (x, y)

   :param x: the character column
   :param y: the character row
   :param msg: the text string
   :return: none
   '''
   global LCD_file
   if LCD_file is not None:
      LCD_file.write("text %03d,%03d %s" % (x, y, msg))
      LCD_file.flush()

def erase( ):
   ''' Erases all text in the LCD character buffer
   
   :return: none
   '''
   global LCD_file
   if LCD_file is not None:
      LCD_file.write('erase')
      LCD_file.flush()

def show( ):
   ''' Refreshes the LCD device to display both graphics and text
   
   :return: none
   '''
   global LCD_file
   if LCD_file is not None:
      LCD_file.write('sync')
      LCD_file.flush()

def close( ):
   ''' Closes the video device
   
   :return: none
   '''
   global LCD_file
   LCD_file.close()
   LCD_file = None
