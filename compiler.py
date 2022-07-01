from pharser import *


def compile(inputFile, outputFile):

    f_inputFile = open(inputFile, "r")
    inputFileContent = f_inputFile.read()

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

    f_inputFile.close()
    f_outputFile.close()
