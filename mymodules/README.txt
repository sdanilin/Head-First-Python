#1)Создание файла описания; 2)Создание файла дистрибутива; 3)Установка файла дистрибутива
#Команда для содания дистрибутива: cd...mymodules$ python3 setup.py sdist
#Установка пакетов при помощи pip: cd...dist$ sudo python3 -m pip install vsearch-1.0.tar.gz