import os
import shutil
import compiler
def build(fileName, args):
  if not fileName.endswith('.tpan'): # Add extension if not specified
    fileName = f'{fileName}.tpan'
  if not os.path.exists(fileName): # Check if file exists
    print(f'Taipan Error: File {fileName} not found') # Error and exit
    exit()

  outputFolderName = 'dist'
  if args.folder:
    outputFolderName = args.folder


  if os.path.exists(outputFolderName):
    shutil.rmtree(outputFolderName)
  os.mkdir(outputFolderName)

  print('Building for production...')

  compiler.compile(fileName, outputFolderName, args)

  print('Process finished')