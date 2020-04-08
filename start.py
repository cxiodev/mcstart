import json, subprocess

print('\nmcStart v1.0 by nesclassdev\ngithub.com/nesclassdev/mcstart\n')

print('Удаляю предыдущие следы запуска...')
print('killall java; killall screen')

with open('config.json', 'r') as file:
    data = json.load(file)
    
    ct, i = len(data['servers']), 0
    print('Найден%s %s сервер%s. Запускаю...\n'%('о' if ct > 1 else '', ct, ('ов' if ct > 4 else 'а') if ct > 1 else ''))

    for server in data['servers']:
        i = i + 1
        subprocess.run('fuser -k %s/tcp 1>/dev/null 2>&1'%(server['port']))
        subprocess.run('screen -dmS %s; screen -S %s -p 0 -X stuff \'cd %s\njava -Xincgc -Xmx%sM -jar %s\''%(
            server['name'], server['name'], '/'.join(server['core'].split('/')[:-1]), int(server['memory']) * 1024, server['core'].split('/')[-1]))
        
        print('Сервер "%s" запущен. (%s/%s)'%(server['name'], i, ct))

print('\nГотово!')