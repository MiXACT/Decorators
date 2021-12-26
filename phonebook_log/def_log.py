import time
import os

def log_path(log_dir):
    def logger_decor(func):
        def log(*args, **kwargs):
            if not os.path.isdir(log_dir):
                os.mkdir(log_dir)
            os.chdir(log_dir)
            with open(f'func_log.txt', 'a', encoding='utf-8') as f:
                f.write(f"{time.strftime('%d.%m.%Y - %H:%M:%S', time.localtime())};\nф-ия: {func.__name__};\n")
                res = func(*args, **kwargs)
                f.write(f"аргументы ф-ии: {args};\nвозвращаемое значение: {res}\n\n")
            os.chdir('..')
            return res
        return log
    return logger_decor