import colorama

# Печатаем все атрибуты и методы модуля colorama
# Это позволяет нам увидеть, какие функции и переменные есть в библиотеке
print(dir(colorama))

# Также можно пройти по всем атрибутам и распечатать их по отдельности
# Это даст более подробный список всех доступных элементов
for item in dir(colorama):
    print(item)


# Импортируем важные компоненты из библиотеки colorama
from colorama import init, deinit, Fore, Back, Style

# Инициализируем colorama
# Это необходимо, чтобы поддерживать работу с цветами, особенно в Windows, где без этого не будет отображаться цветной вывод в терминале
init()

# Пример использования Fore (цвет текста)
# Начнём с красного текста
print(Fore.RED + "Это красный текст" + Fore.RESET)  # После текста сбрасываем цвет, чтобы дальше он не применялся

# Теперь попробуем зелёный цвет для текста
print(Fore.GREEN + "Это зелёный текст" + Fore.RESET)

# Пример с фоном (Back)
# Здесь используем синий фон
print(Back.BLUE + "Текст с синим фоном" + Back.RESET)  # Сбрасываем фон после вывода, чтобы не повлиять на следующий текст

# Пример с изменением стиля текста (Style)
# Делаем текст ярким
print(Style.BRIGHT + "Яркий текст" + Style.RESET_ALL)  # После яркого текста сбрасываем стиль на стандартный

# Теперь попробуем тусклый стиль
print(Style.DIM + "Тусклый текст" + Style.RESET_ALL)

# Комбинируем цвета и стиль
# Сделаем желтый текст на красном фоне и применим яркий стиль
print(Fore.YELLOW + Back.RED + Style.BRIGHT + "Желтый текст на красном фоне с ярким стилем" + Style.RESET_ALL)

# Пример с деинициализацией (deinit)
# Если больше не нужно работать с цветами, можно отключить colorama
deinit()

# После вызова deinit() вывод будет обычным, без применения цветов и стилей
print("После деинициализации: обычный текст")
