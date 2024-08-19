![Header Image](https://i.imgur.com/rAosM9d.jpeg)
# TreeSpect 🌳

TreeSpect is a powerful Python script for visualizing directory structures. It provides a clear and informative representation of your project's file system, which is especially useful for documentation and quick project overviews.

## Features 🚀

- 🌳 Creates a visual tree representation of directory structures
- 🚫 Automatically ignores `__pycache__` directories
- 🎭 Marks Python virtual environments as `[virtual environment]`
- 📦 Optionally displays the number of installed packages in virtual environments
- 🔍 Ignores the script file itself in the output
- 📁 Marks directories with a `[dir]` prefix
- 📄 Displays files before directories for easier viewing
- 💾 Option to save the result to a text file
- 🔢 Multiple options for displaying information about virtual environment packages
- 📊 Option to show only information about virtual environments
- 🛡️ Resilient to deep directory structures
- ⏱️ Execution time limit to prevent hanging

## Installation 📥

1. Clone the repository:
   ```
   git clone https://github.com/ursaloper/TreeSpect.git
   ```
2. Navigate to the TreeSpect directory:
   ```
   cd TreeSpect
   ```

## Usage 🖥️

Run the script in the directory you want to visualize:

```
python run_treespect.py [options]
```

### Options 🔧

- `-rs`, `--result-save`: Save the result to a file
- `-vp`, `--venv-packages`: Show installed packages in virtual environments (options: 'none', 'count', 'names', 'full')
- `-vo`, `--venv-only`: Show only information about virtual environments without the full tree
- `-vps`, `--venv-packages-save`: Save information about virtual environment packages to a file (options: 'names', 'full')
- `-md`, `--max-depth`: Maximum depth of directory traversal (default: 10)
- `-to`, `--timeout`: Timeout in seconds (default: 300)

### Examples 📚

1. Basic usage (console output):
   ```
   python run_treespect.py
   ```

2. Save the result to a file:
   ```
   python run_treespect.py -rs
   ```

3. Display the number of packages in the virtual environment:
   ```
   python run_treespect.py -vp count
   ```

4. Display the names of packages in the virtual environment:
   ```
   python run_treespect.py -vp names
   ```

5. Show only information about virtual environments:
   ```
   python run_treespect.py -vo
   ```

6. Save information about virtual environment packages to a file:
   ```
   python run_treespect.py -vps
   ```

7. Limit scan depth and set timeout:
   ```
   python run_treespect.py -md 5 -to 60
   ```

8. View help:
   ```
   python run_treespect.py -h
   ```

## Example Output 📋

```
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── [dir] app
    ├── __init__.py
    ├── [dir] models
    │   ├── __init__.py
    │   └── user.py
    ├── [dir] views
    │   ├── __init__.py
    │   └── main.py
    └── [virtual environment] venv (10 packages installed)
```

## Error Handling and Notifications 🚨

- If no virtual environment is found when using the `-vo` option, a notification is displayed:
  ```
  [INFO] No virtual environments found.
  ```

- When using the `-vps` option, if no virtual environment is found, the file is not saved, and a notification is displayed:
  ```
  [INFO] No virtual environments found. File will not be saved.
  ```

## Configuration ⚙️

You can configure ignored directories by modifying the `IGNORE_DIRS` variable at the beginning of the script:

```python
IGNORE_DIRS = ["__pycache__", "node_modules"]  # Example: also ignore node_modules
```

## Contributing 🤝

We welcome contributions to improve TreeSpect! If you have ideas for enhancements, please create an issue or submit a pull request.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

# TreeSpect 🌳

TreeSpect - это мощный Python-скрипт для визуализации структуры директорий. Он предоставляет четкое и информативное представление файловой системы вашего проекта, что особенно полезно для документации и быстрого обзора структуры проекта.

## Особенности 🚀

- 🌳 Создает визуальное древовидное представление структуры директорий
- 🚫 Автоматически игнорирует `__pycache__` директории
- 🎭 Отмечает Python виртуальные окружения как `[virtual environment]`
- 📦 Опционально показывает количество установленных пакетов в виртуальных окружениях
- 🔍 Игнорирует файл самого скрипта в выводе
- 📁 Отмечает директории префиксом `[dir]`
- 📄 Отображает файлы перед директориями для более удобного просмотра
- 💾 Возможность сохранения результата в текстовый файл
- 🔢 Несколько опций для отображения информации о пакетах виртуального окружения
- 📊 Возможность показать только информацию о виртуальных окружениях
- 🛡️ Устойчивость к глубоким структурам директорий
- ⏱️ Ограничение времени выполнения для предотвращения зависаний

## Установка 📥

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/ursaloper/TreeSpect.git
   ```
2. Перейдите в директорию TreeSpect:
   ```
   cd TreeSpect
   ```

## Использование 🖥️

Запустите скрипт в директории, структуру которой вы хотите визуализировать:

```
python run_treespect.py [опции]
```

### Опции 🔧

- `-rs`, `--result-save`: Сохранить результат в файл
- `-vp`, `--venv-packages`: Показать установленные пакеты в виртуальных окружениях (варианты: 'none', 'count', 'names', 'full')
- `-vo`, `--venv-only`: Показать только информацию о виртуальных окружениях без полного дерева
- `-vps`, `--venv-packages-save`: Сохранить информацию о пакетах виртуальных окружений в файл (варианты: 'names', 'full')
- `-md`, `--max-depth`: Максимальная глубина обхода директорий (по умолчанию: 10)
- `-to`, `--timeout`: Тайм-аут в секундах (по умолчанию: 300)

### Примеры использования 📚

1. Базовое использование (вывод в консоль):
   ```
   python run_treespect.py
   ```

2. Сохранение результата в файл:
   ```
   python run_treespect.py -rs
   ```

3. Отображение количества пакетов виртуального окружения:
   ```
   python run_treespect.py -vp count
   ```

4. Отображение имен пакетов виртуального окружения:
   ```
   python run_treespect.py -vp names
   ```

5. Показать только информацию о виртуальных окружениях:
   ```
   python run_treespect.py -vo
   ```

6. Сохранение информации о пакетах виртуального окружения в файл:
   ```
   python run_treespect.py -vps
   ```

7. Ограничение глубины сканирования и установка тайм-аута:
   ```
   python run_treespect.py -md 5 -to 60
   ```

8. Просмотр справки:
   ```
   python run_treespect.py -h
   ```

## Пример вывода 📋

```
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── [dir] app
    ├── __init__.py
    ├── [dir] models
    │   ├── __init__.py
    │   └── user.py
    ├── [dir] views
    │   ├── __init__.py
    │   └── main.py
    └── [virtual environment] venv (10 packages installed)
```

## Обработка ошибок и уведомления 🚨

- Если при использовании опции `-vo` не обнаружено виртуальное окружение, в консоль выводится уведомление:
  ```
  [INFO] No virtual environments found.
  ```

- При использовании опции `-vps`, если не обнаружено виртуальное окружение, файл не сохраняется и выводится уведомление:
  ```
  [INFO] No virtual environments found. File will not be saved.
  ```

## Настройка ⚙️

Вы можете настроить игнорируемые директории, изменив переменную `IGNORE_DIRS` в начале скрипта:

```python
IGNORE_DIRS = ["__pycache__", "node_modules"]  # Пример: игнорировать также node_modules
```

## Вклад в проект 🤝

Мы приветствуем вклад в улучшение TreeSpect! Если у вас есть идеи по улучшению, пожалуйста, создайте issue или отправьте pull request.

## Лицензия 📄

Этот проект лицензирован под MIT License - см. файл [LICENSE](LICENSE) для деталей.
