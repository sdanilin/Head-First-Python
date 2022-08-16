from setuptools import setup #импорт функции setup  из модуля setuptools

setup(
    name='vsearch', #Аргумент name определяет имя дистрибутива. дистрибутивы часто называбтся так же как модули
    version='1.0',
    description='The Head First Python Search Tools',
    author='HF Python 2e',
    author_email='hfpy2e@gmail.com',
    url='headfirstlabs.com',
    py_modules=['vsearch'], #Список файлов .py, которые нужно включить в в пакет. В примере такой фаул только один "vsearch"
)