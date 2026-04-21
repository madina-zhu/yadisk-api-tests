```markdown
# Яндекс.Диск API автотесты

Автотесты для API Яндекс.Диска, проверяющие основные методы работы с файлами и папками.

## 🛠 Стек технологий

- Python 3.12
- Pytest 7.4.3
- Requests 2.31.0
- Allure Pytest 2.13.2
- python-dotenv 1.0.0

## 📋 Требования

- Python 3.9+
- pip
- Git

## 🚀 Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/ВАШ_ЛОГИН/yadisk-api-tests.git
cd yadisk-api-tests
```

### 2. Создать и активировать виртуальное окружение

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Получить OAuth-токен Яндекс.Диска

#### 4.1. Создать приложение

1. Перейдите на страницу: https://oauth.yandex.ru/
2. Войдите под своим Яндекс-аккаунтом
3. Нажмите кнопку **"Создать приложение"**
4. Название: `API Тесты Диска` (или любое другое)
5. Выберите **"Для доступа к API или отладки"**
6. В разделе "Доступ к данным" отметьте:
   - `Доступ к папке приложения на Диске`
   - `Чтение всего Диска`
   - `Запись в любом месте на Диске`
   - `Доступ к информации о Диске`
7. Нажмите **"Создать приложение"**
8. Скопируйте **ClientID** (строка из букв и цифр)

#### 4.2. Получить токен

1. Сформируйте ссылку, заменив `ВАШ_CLIENT_ID`:
https://oauth.yandex.ru/authorize?response_type=token&client_id=ВАШ_CLIENT_ID
2. Перейдите по ссылке
3. Нажмите **"Разрешить"**
4. Скопируйте токен из адресной строки (часть после `access_token=`)

Пример: `https://yandex.ru/#access_token=AQAAA...&token_type=bearer`

### 5. Создать файл с токеном

```bash
echo "YANDEX_DISK_TOKEN=ваш_токен_скопированный_выше" > .env
```

### 6. Запустить тесты

**Обычный запуск:**
```bash
pytest tests/ -v
```

**С Allure-отчётом:**
```bash
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

**Запуск конкретного теста:**
```bash
pytest tests/test_get.py -v
```

##  Покрытие тестов

| HTTP метод | Эндпоинт | Что проверяется |
|------------|----------|-----------------|
| **GET** | `/resources` | Получение содержимого папки |
| **GET** | `/resources` | Проверка обязательных полей (name, created, modified) |
| **GET** | `/resources` | Параметризация: корневая папка (200) и несуществующая (404) |
| **POST** | `/resources/copy` | Копирование папки |
| **POST** | `/resources/upload` | Загрузка файла по URL |
| **PUT** | `/resources` | Создание новой папки |
| **PUT** | `/resources` | Ошибка при создании существующей папки (409/423) |
| **DELETE** | `/resources` | Удаление папки |
| **DELETE** | `/resources` | Ошибка 404 при удалении несуществующей папки |

**Всего тестов: 10**

## 📈 Результат запуска

```bash
collected 10 items

tests/test_delete.py::test_delete_folder PASSED                    [10%]
tests/test_delete.py::test_delete_nonexistent_folder PASSED        [20%]
tests/test_get.py::test_get_folder_contents PASSED                 [30%]
tests/test_get.py::test_get_metadata_has_required_fields PASSED    [40%]
tests/test_get.py::test_get_different_paths[/-200] PASSED          [50%]
tests/test_get.py::test_get_different_paths[/nonexistent-404] PASSED [60%]
tests/test_post.py::test_copy_folder PASSED                        [70%]
tests/test_post.py::test_upload_from_url PASSED                    [80%]
tests/test_put.py::test_create_folder_put PASSED                   [90%]
tests/test_put.py::test_create_existing_folder PASSED              [100%]

============================== 10 passed in 44.99s ==============================

## 📁 Структура проекта

```
yadisk-api-tests/
├── .venv/                 # Виртуальное окружение
├── tests/                 # Тесты
│   ├── __init__.py
│   ├── conftest.py        # Фикстуры
│   ├── test_delete.py     # DELETE тесты
│   ├── test_get.py        # GET тесты
│   ├── test_post.py       # POST тесты
│   └── test_put.py        # PUT тесты
├── .env                   # Токен (не загружается в Git)
├── .gitignore             # Исключения Git
├── api_client.py          # Клиент для API
├── config.py              # Конфигурация
├── requirements.txt       # Зависимости
├── pytest.ini             # Настройки pytest
└── README.md              # Документация
```

##  Особенности реализации

- ✅ **Безопасное хранение токена** — через `.env` файл
- ✅ **Логирование запросов** — все HTTP запросы логируются
- ✅ **Параметризация тестов** — один тест с разными входными данными
- ✅ **Проверка тела ответа** — валидация обязательных полей
- ✅ **Allure-отчёты** — красивые отчёты о тестировании
- ✅ **Автоматическая очистка** — фикстуры удаляют тестовые данные

##  Возможные проблемы

### Ошибка 401 (Unauthorized)
- Проверьте правильность токена в файле `.env`
- Получите новый токен по инструкции выше

### Ошибка 404 (Not Found)
- Проверьте интернет-соединение
- Убедитесь, что API Яндекс.Диска доступен

### Ошибка импорта модулей
```bash
export PYTHONPATH=$(pwd)
pytest tests/ -v
```

##  Полезные команды

```bash
# Запуск с подробным выводом
pytest tests/ -vv

# Запуск с остановкой при первой ошибке
pytest tests/ -x

# Запуск конкретного теста по имени
pytest tests/test_get.py::test_get_folder_contents -v

# Показать все print() в консоли
pytest tests/ -v -s

# Запуск с маркерами (если добавлены)
pytest tests/ -v -m smoke
```
