import os
import compiler
import random
def run(fileName, arguments=None):
  if not os.path.exists(fileName): # Check if file exists
    fileName = f'{fileName}.tpan' # If not try to add taipan extension to it
    if not os.path.exists(fileName): # Check if file with added extension exists  
      print('Error: File not found') # Error and exit
      exit()
  
  # File exists
  tempFolder = f'temp-{random.randrange(1000, 1000000000)}'
  tempFileName = os.path.join(tempFolder, f'{fileName.removesuffix(".tpan")}.py.temp')

  os.mkdir(tempFolder)

  print('Compiling...')

  compiler.compile(fileName, tempFileName)

  print('Running...')

  exec(open(tempFileName).read())
  
  os.remove(tempFolder) # Not working

  print('Process finished')