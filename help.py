commands = {
  "help": {
    "description": "Displays help about commands",
    "parameters": "[command] - optional",
    "options": None
  },
  "run": {
    "description": "Compiles taipan into temporary python file and executes it",
    "parameters": "[filePath] - required",
    "options": None
  },
  "build": {
    "description": "Compiles taipan into python",
    "parameters": "[filePath] - required",
    "options": "--folder [folderName] - specifies folder where the output should be saved"
  },
}

def printHelp(command=None):
  if command == None:
    print('Taipan help')
    print('Available commands:')
    print('-----------------------------------------')
    print('help  - displays this message')
    print('run   - executes taipan file')
    print('build - builds taipan file into python')
    print('-----------------------------------------')
    print('Use taipan help [command] for more information')
  elif command in commands:
    print('Command description:')
    print(commands[command]['description'])
    print('Parameters:')
    print(commands[command]['parameters'])
    print('Options:')
    print(commands[command]['options'])
  else: 
    print(f'Unknown command: {command}')