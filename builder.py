import os
import compiler
def build(fileName, args):
  if not os.path.exists(fileName): # Check if file exists
    fileName = f'{fileName}.tpan' # If not try to add taipan extension to it
    if not os.path.exists(fileName): # Check if file with added extension exists  
      print('Error: File not found') # Error and exit
      exit()

  if args.folder:
    outputFolderName = args.folder
  else:
    outputFolderName = 'dist'

  # os.mkdir(outputFolderName)

  print('Building for production...')

  compiler.compile(fileName, os.path.join(outputFolderName, f'{fileName.removesuffix(".tpan")}.py'))

  print('Process finished')