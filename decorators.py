import time
import os

def log_path(log_dir):
    def logger_decor(func):
        def log(*args, **kwargs):
            if not os.path.isdir(log_dir):
                os.mkdir(log_dir)
            os.chdir(log_dir)
            with open(f'func_log.txt', 'w') as f:
                f.write(f"{time.strftime('%d.%m.%Y - %H:%M:%S', time.localtime())};\nф-ия: {func.__name__};\n")
                res = func(*args, **kwargs)
                f.write(f"аргументы ф-ии: {args};\nвозвращаемое значение: {res}")
            return res
        return log
    return logger_decor

@log_path('log')
def mult(x, y):
    return x * y


if __name__ == '__main__':
    mult(5, 10)
    print('Задачи №№ 1 и 2: лог-файл func_log.txt записан в указанную директорию!')

