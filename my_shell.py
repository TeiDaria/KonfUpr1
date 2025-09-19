import os
import socket
import sys
import shlex #для понимания команд с кавычками
import argparse #парсер аргументов


def parse_args():
    parser = argparse.ArgumentParser(description='My shell emulator')
    # учимся понимать параметры:
    parser.add_argument('--vfs-path',
                        default='',
                        help='Path to the vfs directory')
    parser.add_argument('--script',
                        default=None,
                        help='Script to execute')
    parser.add_argument('--debug',
                        action='store_true',
                        help='Turn on debug mode')
    return parser.parse_args()  # узнаем команду

class ShellEmulator:
    def __init__(self, vfs_path=None, debug=False):
        ##print("Initializing ShellEmulator with parametres")

        self.current_dir = os.getcwd() #запоминаем текущую (исходную) директорию
        self.username = os.getenv('USERNAME','user') #узнаем имя пользователя
        self.hostname = socket.gethostname() #узнаем имя компьютера
        self.running = True #Флаг работаем или нет

        self.vfs_path = vfs_path or './vfs'
        self.debug = debug

        if debug:
            print(f" Настройки: VFS путь = {self.vfs_path}")
            print(f" Режим отладки: ВКЛЮЧЕН")

        print("Print 'exit' to stop")

    def get_promt(self): #приглашение к вводу
        #узнаем имя текущей папки
        base_dir = os.path.dirname(self.current_dir)
        if base_dir == '':
            base_dir = '/'

        #делаем красивую надпись
        return f"{self.username}@{self.hostname}:~$ "

    def parse_command(self, command_line):
        try:
            return shlex.split(command_line)
        except ValueError:
            print("Quotation marks are invalid")
            return None

    def execute_command(self, command_parts):
        if not command_parts: #команды нет
            return

        command = command_parts[0] #первая часть - команда
        args = command_parts[1:] #остальное - аргументы

        if command == "exit":
            self.running = False
            print("Goodbye")
        elif command == "ls":
            print(f"Pretending to execute command: {command}")
            print(f"Arguments: {args}")
        elif command == "cd":
            print(f"Pretending to execute command: {command}")
            print(f"Arguments: {args}")
        else:
            print("Unknown command")

    def run(self):
        print("~~~~~~~~~~~My emulator~~~~~~~~~~~")
        print("Print 'exit' to stop")
        print("Commands: ls, cd, exit")
        print("Try commands with quotation marks: ls 'my_text.txt'")
        print("~" * 34)

        while self.running:  # пока флажок true
            try:
                # показываем приглашение и ждем команду
                command_line = input(self.get_promt()).strip()
                if not command_line:
                    continue
                else:
                    parts = self.parse_command(command_line)
                    if parts is not None:
                        self.execute_command(parts)
            except KeyboardInterrupt:
                print("\nPrint 'exit' to stop")
            except EOFError:
                print("\nВыход...")
                break

    def run_script(self, script_path):
        if not os.path.exists(script_path):
            print("Script not found")
            return
        print(f"Running script: {script_path}")
        print("~" * 50)

        try:
            with open(script_path, 'r') as file:
                lines = file.readlines()

                for line_num, line in enumerate(lines, 1):
                    line = line.strip()

                    if not line or line.startswith('#'):
                        continue #пропускаем пустые строки

                    if self.debug:
                        print(f"Reading line {line_num}: {line}")

                    #Показываем команду как будто её ввел пользователь
                    print(self.get_promt()+line)

                    #Выполняем программу
                    parts = self.parse_command(line)
                    if parts is not None:
                        self.execute_command(parts)
                    print() #пустая строка между командами

        except Exception as e:
            print(f"Error while reading script: {e}")



#запускаем эмулятор
if __name__ == "__main__":
    #узнаем какие параметры нам дали
    args = parse_args()

    if args.debug:
        print("Debug mode:")
        print(f"VFS path: {args.vfs_path}")
        print(f"Script: {args.script}")
        print("~"*40)

    shell = ShellEmulator(vfs_path=args.vfs_path, debug=args.debug)
    if args.script:
        #Выполнение скрипта если он есть
        shell.run_script(args.script)
    else:
        #Иначе запуск обычного режима
        shell.run()