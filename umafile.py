from plyer import notification
import os
import configparser
import shutil

config = configparser.ConfigParser()
config.read(os.getcwd() + '\\config.ini','UTF-8')


flag = os.path.exists(config['Dir']['copydir'] + '/' + config['Dir']['target'])

if not flag:
    copyfiles = os.listdir(os.getcwd() + '\\files')
    for file in copyfiles:
        print(os.getcwd() + '\\files\\' + file + "から" + config['Dir']['copydir'] + "にコピー")
        shutil.copy(os.getcwd() + '\\files\\' + file, config['Dir']['copydir'])
    
    notification.notify(
        title = config['setting']['title'],
        message = config['setting']['msg'],
        app_name = "自動ファイル追加"
    )
else:
    notification.notify(
        title = config['setting']['title'],
        message = config['setting']['nomsg'],
        app_name = "自動ファイル追加"
    )

os.system('powershell -Command start dmmgameplayer://umamusume/cl/general/umamusume')