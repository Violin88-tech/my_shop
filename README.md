<h1 align="center">Проект по тестированию онлайн-магазина 
<p align="center">
<a href="https://my-shop.ru/" target="_blank">
<img src="https://s.rbk.ru/v1_companies_s3/resized/960xH/media/trademarks/91cbd2c0-7f6c-48e5-ba52-f72f348a2f65.jpg" 
alt="МАЙШОП" width="128" height="64"> </a> 
</p></h1>
 
<!-- Тест кейсы -->
----
## Автоматизировано тестирование функционала:

## UI-тесты

* Проверка главного меню сайта
* Поле поиска в хедере (позитивный и негативный сценарий)
* Авторизация пользователя на сайте(успешная и неуспешная)
* Добавление и удаление товара в избранное
* Добавление и удаление товара из корзины

## API-тесты

* Поиск книги (успешный и неуспешный)
* Добавление книги в корзину
* Добавление книги в избранное

----
# <a name="Technology">Технологии и инструменты</a>

<p  align="center">
  <code><img width="5%" title="Python" src="media/logo/python.png"></code>
  <code><img width="5%" title="Pycharm" src="media/logo/pycharm.png"></code>
  <code><img width="5%" title="Pytest" src="media/logo/pytest.png"></code>
  <code><img width="5%" title="Selenium" src="media/logo/selenium.png"></code>
  <code><img width="5%" title="Selene" src="media/logo/selene.png"></code>
  <code><img width="5%" title="GitHub" src="media/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="media/logo/jenkins.png"></code>
  <code><img width="5%" title="Allure Report" src="media/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="media/logo/allure_testops.png"></code>
  <code><img width="5%" title="Telegram" src="media/logo/tg.png"></code>
</p>

----
В данном проекте автотесты написаны на **Python** с использованием фреймворка **Pytest** и популярных библиотек *
*Selene, WebDriver-Manager, Selenium**.
Из **Jenkins** выполняется запуск тестов.
**Selenoid** используется для запуска браузеров в контейнерах **Docker**.
**Allure Report, Telegram Bot** используются для визуализации результатов тестирования.

----
# <a name="Jenkins">Запуск тестов в [Jenkins](https://jenkins.autotests.cloud/job/10_da-vasilev_qa-guru-hw25/)</a>

> <a target="_blank" href="https://jenkins.autotests.cloud/job/my_shop/">Ссылка на проект в
> Jenkins</a>

### Для запуска автотестов в Jenkins
1. Открыть проект
2. Выбрать пункт "Собрать с параметрами"
<img src="/media/screenshots/img2.png">



### Локальный запуск автотестов

1. Клонируйте репозиторий

```ruby
gh repo clone MaryMokretsova/my_shop_project_tests
```

2. Создайте и активируйте виртуальное окружение

  ```ruby
  python -m venv .venv
  source .venv/bin/activate
  ```

3. Установите зависимости с помощью pip

  ```ruby
  pip install -r requirements.txt
  ```

4. Запустите автотесты

  ```ruby
  pytest -sv
  ```

5. Получите отчёт allure

```ruby
allure serve allure-results
``` 

----

# <a name="AllureReport">Отчет о результатах тестирования в [Allure Report](https://jenkins.autotests.cloud/job/10_da-vasilev_qa-guru-hw25/23/allure/)</a>

#### Общая информация

Главная страница Allure-отчета содержит следующие информационные блоки:

> - <code><strong>*ALLURE REPORT*</strong></code> - отображает дату и время прохождения теста, общее количество
    прогнанных кейсов, а также диаграмму с указанием процента и количества успешных, упавших и сломавшихся в процессе
    выполнения тестов
>- <code><strong>*TREND*</strong></code> - отображает тренд прохождения тестов от сборки к сборке
>- <code><strong>*SUITES*</strong></code> - отображает распределение результатов тестов по тестовым наборам
>- <code><strong>*CATEGORIES*</strong></code> - отображает распределение неуспешно прошедших тестов по видам дефектов


Результат запуска сборки можно посмотреть в отчёте Allure

[//]: # (При первом запуске не все селекторы отработали корректно)


#### Общие результаты
<p align="center">
<img src="/media/screenshots/img4.png" alt="Allure Report" width="750">)
</p>

#### Список тест кейсов
<p align="center">
<img src="/media/screenshots/img5.png" alt="Allure Report" width="750">)
</p>

----
#### Тест-планы проекта
<p align="center">
<img src="/media/screenshots/img8.png" alt="Allure Report" width="750">)
</p>

#### Общий список всех кейсов, имеющихся в системе (без разделения по тест-планам и виду выполнения тестирования)
<p align="center">
<img src="/media/screenshots/img9.png" alt="Allure Report" width="750">)
</p>

#### Пример отчёта выполнения одного из автотестов
<p align="center">
<img src="/media/screenshots/img10.png" alt="Allure Report" width="750">)
</p>

#### Тестовые артефакты
<p align="center">
<img src="/media/screenshots/img11.png" alt="Allure Report" width="750">)
</p>

#### Пример dashboard с общими результатами тестирования
<p align="center">
<img src="/media/screenshots/img12.png" alt="Allure Report" width="750">)
</p>

#### История запуска тестовых наборов
<p align="center">
<img src="/media/screenshots/img13.png" alt="Allure Report" width="750">)
</p>

----
### Уведомления в Telegram

<p align="center">

<img src="/media/screenshots/img15.png" alt="Telegram" width="300"></a>
</p>

----




