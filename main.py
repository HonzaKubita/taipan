from object import newObject # Library for creating anonymus objects
from argparser import argParser# Library for parsing shell parameters

# Modules import
import compiler
import builder
import runner

parserTemplate = ['mode', 'fileName', '--options'] # Create template of shell arguments
parserOptions = newObject(
  dev='bool',
  folder='str'
)

parser = argParser(parserTemplate)
parser.options = parserOptions

args = parser.parse()

# Put main args to their own variables
mode = args.mode
fileName = args.fileName

print(f'Mode: {mode}, fileName: {fileName}, dev: {args.options.dev}, folder: {args.options.folder}')