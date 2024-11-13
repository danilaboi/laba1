# Color Converter

## Описание

Color Converter — это интерактивное веб-приложение, предназначенное для конвертации цветов между различными цветовыми моделями: RGB, XYZ и CMYK. Приложение позволяет пользователю выбирать цвет и интерактивно изменять его, отображая при этом его составляющие во всех трех моделях одновременно. При изменении любой компоненты цвета все остальные представления этого цвета в других моделях пересчитываются автоматически.

## Установка и запуск

### Системные требования

* **Операционная система**: Любая (поддержка браузеров).

### Запуск приложения

1. Перейдите по ссылке: [GitHub](https://github.com/danilaboi/laba1)
2. Скачайте файл main.exe приложения Color Converter из папки dist
3. Запустите приложение

## Пользовательский интерфейс

### Основные элементы

* **Области отображения цвета**: три цветовых квадрата, отображающих текущий цвет в каждой из моделей (RGB, XYZ, CMYK).
* **Поля ввода**: текстовые поля для ввода значений компонентов цвета вручную.
* **Ползунки**: для каждой компоненты цвета в каждой модели имеются ползунки для плавного изменения значений.

### Навигация по интерфейсу

#### Изменение цвета с помощью ползунков

1. Используйте ползунки под каждой моделью для изменения значений компонентов.
2. При изменении любого значения остальные модели обновятся автоматически.

#### Ввод значений вручную

1. Введите значения компонентов в текстовое поле соответствующей модели.
2. Нажмите **Enter** для применения изменений.
3. Пример ввода для RGB: 255 0 0.

## Использование приложения


### Работа с ползунками

* Ползунки позволяют плавно изменять значения компонентов цвета.
* **Диапазоны значений**:
  * **RGB**: от 0 до 255 для каждого компонента.
  * **XYZ**: от 0 до 1 для каждого компонента.
  * **CMYK**: от 0 до 1 для каждого компонента.
* При перемещении ползунка значения в других моделях обновляются автоматически.

#### Ввод значений вручную

1. Введите значения компонентов в текстовое поле соответствующей модели.
2. Нажмите **Enter** для применения изменений.
3. Пример ввода для RGB: 255 0 0.

## Особенности приложения

### Автоматический пересчет

* При изменении любого значения компоненты цвета в одной модели приложение автоматически пересчитывает значения в других моделях.
* Это обеспечивает согласованность и актуальность отображаемой информации.

### Обработка некорректных значений

* При вводе значений, выходящих за пределы допустимого диапазона, приложение автоматически корректирует их до ближайшего допустимого значения.
* Например, если ввести значение -10 для компоненты, допускающей диапазон от 0 до 255, приложение установит значение 0.

### Цветовые квадраты

* Каждый цветовой квадрат отображает цвет в соответствующей модели.
* Это позволяет визуально сравнить, как цвет выглядит в разных моделях.

## Цветовые модели

### RGB

* **Описание**: Аддитивная модель цвета, основанная на комбинации красного, зеленого и синего.
* **Компоненты**:
  * **R** — красный.
  * **G** — зеленый.
  * **B** — синий.

### XYZ

* **Описание**: Цветовая модель, основанная на восприятии цвета.
* **Компоненты**:
  * **X** — красный.
  * **Y** — зеленый.
  * **Z** — синий.

### LAB

* **Описание**: Cубтрактивная схема формирования цвета.
* **Компоненты**:
  * **С** — голубой.
  * **M** — пурпурный.
  * **Y** — желтый.
  * **K** — черный.

## Известные ограничения

* **Точность преобразования**: Преобразования между цветовыми моделями могут иметь незначительные погрешности из-за математических округлений.
* **Ограничение диапазонов**: Некоторые цвета могут быть недоступны в определенных цветовых моделях из-за их ограничений.
* **Отображение цветов**: Цвета могут отображаться по-разному на разных мониторах из-за различий в настройках цветопередачи.

## Исходный код

Исходный код приложения доступен на [GitHub](https://github.com/danilaboi/laba1). Вы можете ознакомиться с кодом, внести свои предложения или доработки.

## Обратная связь

Если у вас возникли вопросы, предложения или вы обнаружили ошибку, пожалуйста, свяжитесь с разработчиком:

* **Email**: daniil090106@mail.ru
* **GitHub**: [danilaboi](https://github.com/danilaboi)

## Лицензия

Приложение распространяется под лицензией MIT License.
