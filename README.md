# TreeSpect 🌳

TreeSpect is a powerful Python script for visualizing directory structures. It provides a clear and informative representation of your project's file system, which is especially useful for documentation and quick project structure overviews.

## Features 🚀

- 🌳 Creates a visual tree representation of directory structures
- 🚫 Automatically ignores `__pycache__` directories
- 🎭 Marks Python virtual environments as `[virtual environment]`
- 📦 Optionally shows the number of installed packages in virtual environments
- 🔍 Ignores the script file itself in the output
- 📁 Marks directories with the `[dir]` prefix
- 📄 Displays files before directories for easier viewing
- 💾 Option to save the result to a text file
- 🔢 Multiple options for displaying virtual environment package information
- 📊 Ability to show only virtual environment information

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

Run the script in the directory whose structure you want to visualize:

```
python treespect.py [options]
```

### Options 🔧

- `-rs`, `--result-save`: Save the result to a file
- `-vp`, `--venv-packages`: Show installed packages in virtual environments (choices: 'count', 'names', 'full')
- `-vo`, `--venv-only`: Show only virtual environment information without the full tree
- `-vps`, `--venv-packages-save`: Save virtual environment packages to a file (choices: 'names', 'full')

### Usage Examples 📚

1. Basic usage (output to console):
   ```
   python treespect.py
   ```

2. Save result to a file:
   ```
   python treespect.py -rs
   ```

3. Display virtual environment package information (count):
   ```
   python treespect.py -vp
   ```

4. Display virtual environment package names:
   ```
   python treespect.py -vp names
   ```

5. Show only virtual environment information:
   ```
   python treespect.py -vo
   ```

6. Save virtual environment package information to a file:
   ```
   python treespect.py -vps
   ```

7. View help:
   ```
   python treespect.py -h
   ```

## Output Example 📋

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

## Customization ⚙️

You can customize ignored directories by modifying the `IGNORE_DIRS` variable at the beginning of the script:

```python
IGNORE_DIRS = ["__pycache__", "node_modules"]  # Example: also ignore node_modules
```

## Contributing 🤝

We welcome contributions to improve TreeSpect! If you have ideas for enhancements, please create an issue or submit a pull request.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

# TreeSpect 🌳

TreeSpect - это мощный Python-скрипт для визуализации структуры директорий. Он предоставляет наглядное и информативное представление файловой системы вашего проекта, что особенно полезно для документации и быстрого обзора структуры проекта.

## Особенности 🚀

- 🌳 Создает визуальное древовидное представление структуры директорий
- 🚫 Автоматически игнорирует директории `__pycache__`
- 🎭 Отмечает Python виртуальные окружения как `[virtual environment]`
- 📦 Опционально показывает количество установленных пакетов в виртуальных окружениях
- 🔍 Игнорирует сам файл скрипта в выводе
- 📁 Отмечает директории префиксом `[dir]`
- 📄 Отображает файлы перед директориями для более удобного просмотра
- 💾 Возможность сохранения результата в текстовый файл
- 🔢 Несколько опций для отображения информации о пакетах виртуального окружения
- 📊 Возможность показать только информацию о виртуальных окружениях

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
python treespect.py [опции]
```

### Опции 🔧

- `-rs`, `--result-save`: Сохранить результат в файл
- `-vp`, `--venv-packages`: Показать установленные пакеты в виртуальных окружениях (варианты: 'count', 'names', 'full')
- `-vo`, `--venv-only`: Показать только информацию о виртуальных окружениях без полного дерева
- `-vps`, `--venv-packages-save`: Сохранить информацию о пакетах виртуальных окружений в файл (варианты: 'names', 'full')

### Примеры использования 📚

1. Базовое использование (вывод в консоль):
   ```
   python treespect.py
   ```

2. Сохранение результата в файл:
   ```
   python treespect.py -rs
   ```

3. Отображение информации о пакетах виртуального окружения (количество):
   ```
   python treespect.py -vp
   ```

4. Отображение имен пакетов виртуального окружения:
   ```
   python treespect.py -vp names
   ```

5. Показать только информацию о виртуальных окружениях:
   ```
   python treespect.py -vo
   ```

6. Сохранение информации о пакетах виртуального окружения в файл:
   ```
   python treespect.py -vps
   ```

7. Просмотр справки:
   ```
   python treespect.py -h
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

## Настройка ⚙️

Вы можете настроить игнорируемые директории, изменив переменную `IGNORE_DIRS` в начале скрипта:

```python
IGNORE_DIRS = ["__pycache__", "node_modules"]  # Пример: игнорировать также node_modules
```

## Вклад в проект 🤝

Мы приветствуем вклад в развитие проекта! Если у вас есть идеи по улучшению TreeSpect, пожалуйста, создайте issue или отправьте pull request.

## Лицензия 📄

Этот проект лицензирован под MIT License - см. файл [LICENSE](LICENSE) для деталей.

---
