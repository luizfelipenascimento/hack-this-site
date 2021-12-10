import requests

basepath = 'https://www.hackthissite.org/missions/basic/8/'

files = ['tshngmww.shtml', 'hipykpqu.shtml', 'ztxdhjxn.shtml', 'avpfeoie.shtml', 'fviqpmaw.shtml', 'kqbybdzc.shtml', 'dzrnmzgx.shtml', 'npcsygfl.shtml', 'whqxxojt.shtml', 'ylomcmvu.shtml', 'uhdppswp.shtml', 'gzntiicx.shtml', 'dzwbqiuu.shtml', 'qvzuieng.shtml', 'smcerykh.shtml', 'qjhnmhmq.shtml', 'znodwztr.shtml']


for file in files:
  response = requests.get('https://www.hackthissite.org/missions/basic/8/tmp/' + file, verify=False)
  print('-' * 20)
  print(file)
  print(response.text)
  val = input('if you want to stop type \'n\'')
  if (val == 'n'):
    break

