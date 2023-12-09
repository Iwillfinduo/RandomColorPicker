# Работа для курса по Python. Сетевой Физтех.
**MVP**

__ __English text below__ __
## Реализованный функционал:
1. **Парсинг** информации(палеток) с сайта Colorhunt.co
2. **Заполнение** базы данных
![image](https://github.com/Iwillfinduo/RandomColorPicker/assets/111530104/aeac584c-182f-4cf6-ab30-65b99c6187fd)
3. **Представление** информации на localhost:5001 с двумя возможными сценариями использования(для выбора сценариев доступна главная страница localhost:5001/ с гиперссылками):
![image](https://github.com/Iwillfinduo/RandomColorPicker/assets/111530104/2b2e0db7-94cc-48a5-a4cc-c9e45617d9ff)
    * Получение **лучшей** цветовой палетки из базы данных(по лайкам) с возможностью скопировать код цвета по клику на localhost:5001/best
    ![image](https://github.com/Iwillfinduo/RandomColorPicker/assets/111530104/0f2b396c-241b-4505-8ecc-dc1896e5edc4)
    * Получение **последней** цветовой палетки из базы данных с возможностью скопировать код цвета по клику на localhost:5001/last
4. Развертывание сервисов с помощью Docker и Docker-compose
5. Запуск через build.sh
6. README.md финальной версии

## Запуск c build.sh (Наличие Docker и Docker-compose необходимо)
1. Склонируйте репозиторий:
```
git clone https://github.com/Iwillfinduo/RandomColorPicker.git
cd RandomColorPicker
```
2. Запустите build.sh
```
.\build.sh
```
3. Откройте решение на localhost:5001/


## Примечание
Данная работа - учебный проект, созданный только в целях обучения. Весь контент принадлежит сервису **Colorhunt** и не используется в коммерческих целях.

# Work for a Python course. Remote MIPT.
**MVP**

## Implemented functionality:

1. **Parsing** information (pallets) from the website Colorhunt.co
2. **Filling** the database
![image](https://github.com/Iwillfinduo/RandomColorPicker/assets/111530104/aeac584c-182f-4cf6-ab30-65b99c6187fd)
3. **Representation** of information on localhost:5001 with two possible usage scenarios (the main page localhost:5001/ with hyperlinks is available to select scenarios):
![image](https://github.com/Iwillfinduo/RandomColorPicker/assets/111530104/2b2e0db7-94cc-48a5-a4cc-c9e45617d9ff)
    * Getting the **best** color palette from the database (by likes) with the ability to copy the color code by clicking (on localhost:5001/best)
    ![image](https://github.com/Iwillfinduo/RandomColorPicker/assets/111530104/0f2b396c-241b-4505-8ecc-dc1896e5edc4)
    * Getting the **latest** color palette from the database with the ability to copy the color code by clicking (on localhost:5001/last)
4. Deploying services using Docker and Docker-compose
5. Launch via build.sh
6. README.md final version
## Quick Start with build.sh (Docker and Docker-compose required)
1. Clone the repository:
```
git clone https://github.com/Iwillfinduo/RandomColorPicker.git
cd RandomColorPicker
```
2. Run build.sh
```
.\build.sh
```
3. Reveal service on localhost:5001/

## Note
This work is an educational project created for educational purposes only. All content belongs to the **Colorhunt** service and is not used for commercial purposes.

