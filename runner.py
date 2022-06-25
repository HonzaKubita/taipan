import os
import compiler
def run(fileName, arguments=None):
  if not os.path.exists(fileName): # Check if file exists
    fileName = f'{fileName}.tpan' # If not try to add taipan extension to it
    if not os.path.exists(fileName): # Check if file with added extension exists  
      print('Error: File not found') # Error and exit
      exit()
  
  # File exists
  tempFileName = f'{fileName.removesuffix(".tpan")}.py.temp'

  print('Compiling...')

  compiler.compile(fileName, tempFileName)

  print('Running...')

  exec(open(tempFileName).read())
  
  os.remove(tempFileName)

  print('Process finished')