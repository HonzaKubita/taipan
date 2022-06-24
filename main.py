from argparser import argParser# Library for parsing shell parameters

# Modules import
import compiler
import builder
import runner

parserTemplate = ['mode', 'fileName'] # Create template of shell arguments
parser = argParser(parserTemplate)

args = parser.parse()

# Put main args to their own variables
mode = args.mode
fileName = args.fileName

print(f'Mode: {mode}, fileName: {fileName}')