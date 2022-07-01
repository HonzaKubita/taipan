from pharser import *
from verifyer import verify
from loading import Loading
import os
import pkg_resources

def _buildProjectTree(mainFile):
  f_mainFile = open(mainFile, "r")
  mainFileContent = f_mainFile.read()
  f_mainFile.close()
  return [mainFile] # ! Temporary

def _compileFile(inputFile, outputFile):
  f_inputFile = open(inputFile, "r")
  inputFileContent = f_inputFile.read()
  f_inputFile.close()
  
  # statements
  # if
  # if_statements = find_occurrences(r"\bif\b", inputFileContent)
  if_statements = find_occurrences(r"\bif\b", inputFileContent)
  print(if_statements)
  for bracket in find_brackets(inputFileContent):
    print(str(bracket.type))

  # re.findall(r"\bif\b", inputFileContent)

  f_outputFile = open(outputFile, "w")
  f_outputFile.write(inputFileContent)
  f_outputFile.close()


def compile(inputFile, folder):

  projectTree = _buildProjectTree(inputFile)

  print("Verifying...")

  loading = Loading(len(projectTree))
  loading.start()
  for i in projectTree: # Verify syntax of all project files
    verify(i)
    loading.add(1)

  print("Done")

  print("Compiling...")
  loading = Loading(len(projectTree))
  loading.start()
  for i in projectTree: # Build all project files
    _compileFile(i, os.path.join(folder, i))
    loading.add(1)
  print("Done")
  