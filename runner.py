import os
import shutil
import random
import compiler
def run(fileName, args):
  if not fileName.endswith('.tpan'): # Add extension if not specified
    fileName = f'{fileName}.tpan'
  if not os.path.exists(fileName): # Check if file exists
    print(f'Taipan Error: File {fileName} not found') # Error and exit
    exit()
  
  # File exists
  tempFolder = f'temp-{random.randrange(1000, 1000000000)}'

  os.mkdir(tempFolder)

  compiler.compile(fileName, tempFolder, args)

  print('Running...')

  exec(open(os.path.join(tempFolder, fileName)).read())
  
  shutil.rmtree(tempFolder)

  print('Process finished')