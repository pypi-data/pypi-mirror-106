import zipfile
import os
from easysettings import EasySettings
from .utils import zipdir

api_host = 'https://api.inferrd.com'

settings = EasySettings(str(Path.home()) + "/.inferrd.conf")

def deploy_current_folder(name):
  if(settings.get('api_key') == ''):
    print('No api key. Use inferrd.auth() or "inferrd auth <key" first.')
    exit()

  model = get_model(name)

  version = new_version(model['id'])
  current_folder = os.cwd()

  print('> Zipping custom model for upload')

  if os.path.exists(current_folder + '/inferrd.zip'):
    shutil.rmtree(current_folder + '/inferrd.zip')

  zipf = zipfile.ZipFile('inferrd.zip', 'w', zipfile.ZIP_DEFLATED)
  zipdir(current_folder, zipf) 
  zipf.close()

  # upload to storage
  print('> Uploading custom model')
  f = open("./inferrd.zip", 'rb')
  r = requests.put(version['signedUpload'], data=f, headers={'Content-Type': 'application/zip'})

  print('> Deploying version v' + str(version['number']))
  deploy_version(version['id'])

  shutil.rmtree('./inferrd.zip')
  #os.remove('./model.zip')

  print('> Custom model deployed')
  return version['number']