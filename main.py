from object import newObject # Library for creating anonymus objects
from argparser import argParser# Library for parsing shell parameters

# Modules import
import builder
import runner
from help import printHelp

# Shell arguments processing
parserTemplate = ['command', 'opt', '--options'] # Create template of shell arguments
parserOptions = newObject(
  dev='bool',
  folder='str'
)

parser = argParser(parserTemplate)
parser.options = parserOptions

args = parser.parse() # parse the shell arguments to object

mode = args.command
filePath = args.opt


if mode == 'run':
  runner.run(filePath, args.options)
elif mode == 'build':
  builder.build(filePath, args.options)
elif mode == 'help' or mode == '-help' or mode == '--help':
  printHelp(args.opt)
else:
  print(f'Unknown mode {mode}. Please choose from run | build')
  print('Use taipan help for more information.')