import os
import socket
import sys
import shlex #для понимания команд с кавычками

class ShellEmulator:
    def __init__(self):
        print("Initializing ShellEmulator")
        self.current_dir = os.getcwd() #запоминаем текущую (исходную) директорию
        self.username = os.getenv('USERNAME','user') #узнаем имя пользователя
        self.hostname = socket.gethostname() #узнаем имя компьютера
        self.running = True #Флаг работаем или нет
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


#запускаем эмулятор
if __name__ == "__main__":
    shell = ShellEmulator()
    shell.run()