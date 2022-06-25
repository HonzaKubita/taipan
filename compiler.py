def compile(inputFile, outputFile):
  
  f_inputFile = open(inputFile, "r")
  inputFileContent = f_inputFile.read()

  f_outputFile = open(outputFile, "w")
  f_outputFile.write(inputFileContent)

  f_inputFile.close()
  f_outputFile.close()