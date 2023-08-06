import sys
from easysettings import EasySettings
from pathlib import Path
from .serve import serve_local_model

settings = EasySettings(str(Path.home()) + "/.inferrd.conf")

def main():
  command = sys.argv[1]

  if(command != 'auth' and command != 'serve'):
    print('The only command available are "auth" and "serve"')
    exit()

  if(len(sys.argv) == 2 and command == 'auth'):
    print('Missing api key. Usage: inferrd auth <api-key>')
    exit()

  if(command == 'serve'):
    serve_local_model()

  if(command == 'auth'):
    api_key = sys.argv[2]
    settings.set('api_key', api_key)
    settings.save()
    print('API Key has been set.')

if __name__ == '__main__':
  main()