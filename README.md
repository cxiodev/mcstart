# mcstart
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

**mcstart** - это open-source скрипт, предназначенный для автоматического запуска/перезапуска группы Minecraft серверов. Теперь, вам не придётся прописывать все команды для запуска вручную!

## Запуск скрипта
```sh
python mcstart.py
```
### Требования
* Python 3.x
* screen (yum install screen)
* psmisc (yum install psmisc)

### Установка
```sh
wget -qO- https://raw.githubusercontent.com/nesclassdev/mcstart/v1.0/mcstart.py
```

### Настройка
config.json:
```json
{
 "servers": [
    {
      "name": "surv",
      "core": "~/surv/spigot.jar",
      "port": 25565,
      "memory": 8
    }
  ]
}
```
**name** - название сервера (внутреннее)  
**core** - путь к ядру сервера  
**port** - выделенный порт  
**memory** - кол-во выделяемой памяти (в гигабайтах)  
