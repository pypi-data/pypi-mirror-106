import os
from eventloop import EventLoop, FileSystemWatch, SingleShotTimer, walk, Schedule
import eventloop.base
import argparse
from colorama import Fore, Back, Style, init as colorama_init
import xml.etree.ElementTree as ET
from subprocess import Popen, PIPE, check_output
import datetime
import sys
import shutil

def debug_print_on(*args):
    print(*args)

def debug_print_off(*args):
    pass

if 'DEBUG_WATCH_UI' in os.environ and os.environ['DEBUG_WATCH_UI'] == "1":
    debug_print = debug_print_on
else:
    debug_print = debug_print_off

try:
    import PySide2
    debug_print("using PySide2")
except ImportError:
    try:
        import PyQt5
        debug_print("using PyQt5")
    except:
        raise Exception("PySide2 not found and PyQt5 not found")

has_PySide2 = 'PySide2' in globals()
has_PyQt5 = 'PyQt5' in globals()

def now_str():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class UiData:
    def __init__(self, path):
        self._path = path
        tree = ET.parse(path)
        root = tree.getroot()
        item = root.find('class')
        class_ = item.text
        item = root.find('widget')
        widget = item.get('class')
        self._class = class_
        self._widget = widget
        #print(class_, widget)

    def class_(self):
        return self._class

    def widget(self):
        return self._widget

    def dst_path(self):
        return os.path.join(os.path.dirname(self._path), 'Ui_{}.py'.format(self._class))

    def src_path(self):
        return self._path

    def src_rel_path(self):
        return os.path.basename(self._path)

    def dst_rel_path(self):
        return os.path.basename(self.dst_path())

    def class_path(self):
        return os.path.join(os.path.dirname(self._path), '{}.py'.format(self._class))

    def src_dirname(self):
        return os.path.dirname(self._path)

    def class_text(self):
        # TODO template in appdata
        if has_PySide2:
            package = 'PySide2'
        elif has_PyQt5:
            package = 'PyQt5'
        class_ = self._class
        widget = self._widget
        return """
from {} import QtWidgets
from Ui_{} import Ui_{}

class {}(QtWidgets.{}):
    def __init__(self, parent = None):
        super().__init__(parent)
        ui = Ui_{}()
        ui.setupUi(self)
        self._ui = ui

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = {}()
    widget.show()
    app.exec_()

""".format(package, class_, class_, class_, widget, class_, class_)

class Logger(eventloop.base.Logger):
    def __init__(self, path):
        super().__init__()
        self._path = path
        
    def print_info(self, msg):
        print(Fore.WHITE + now_str() + " " + Fore.YELLOW + Style.BRIGHT + msg + Fore.RESET + Style.NORMAL)

    def print_error(self, msg):
        print(Fore.WHITE + now_str() + " " + Fore.RED + msg + Fore.RESET)

    def print_compiled(self, src, dst):
        print(Fore.WHITE + now_str() + " " + Fore.GREEN + Style.BRIGHT + os.path.relpath(src, self._path) + Fore.WHITE + " -> " + Fore.GREEN + os.path.relpath(dst, self._path) + Fore.RESET + Style.NORMAL)
    
    def print_writen(self, class_path):
        print(Fore.WHITE + now_str() + " " + Fore.GREEN + Style.BRIGHT + os.path.relpath(class_path, self._path) + Fore.RESET + Style.NORMAL)

def is_modified_within_n_seconds(path, n):
    if not os.path.exists(path):
        return False
    d1 = datetime.datetime.fromtimestamp(os.path.getmtime(path))
    d2 = datetime.datetime.now()
    debug_print(d1, d2, (d2 - d1).total_seconds())
    return d1 <= d2 and (d2 - d1).total_seconds() < n

def write_text(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

class Executor(eventloop.base.Executor):

    def __init__(self, logger, no_class_files):
        super().__init__()
        self._logger = logger
        self._no_class_files = no_class_files

        if has_PySide2:
            name = "pyside2-uic"
        elif has_PyQt5:
            name = "pyuic5"

        uic = shutil.which(name)
        if uic is None:
            raise Exception("{} not found in PATH".format(name))

        self._uic = uic
        
    def execute(self, task):
        src = task
        if not os.path.exists(src):
            return True
        data = UiData(src)
        dst = data.dst_path()
        uic = self._uic
        logger = self._logger
        
        command = [uic, "-x", "-o", data.dst_rel_path(), data.src_rel_path()]
        process = Popen(command, stdout=PIPE, stderr=PIPE, cwd=data.src_dirname())
        stdout, stderr = process.communicate()
        modified = is_modified_within_n_seconds(dst, 5)
        ok = process.returncode == 0 and modified

        debug_print("process.returncode", process.returncode)
        debug_print("modified", modified)

        if ok:
            logger.print_compiled(src, dst)
        else:
            logger.print_error("Failed to compile {}".format(src))
            codec = 'cp1251' if sys.platform == 'win32' else 'utf-8'
            print(stdout.decode(codec))
            print(stderr.decode(codec))

        if not self._no_class_files:
            class_path = data.class_path()
            if not os.path.exists(class_path):
                write_text(class_path, data.class_text())
                logger.print_writen(class_path)

        # no point in rescheduling - must be something wrong with uic
        return True

def main():
    parser = argparse.ArgumentParser(prog="watch-ui")
    parser.add_argument('path',nargs='?',help="Path to watch, defaults to current directory")
    parser.add_argument('--no-initial-scan', action='store_true', help="Skip initial scan")
    parser.add_argument('--no-class-files', action='store_true', help="")
    args = parser.parse_args()

    #print(args); exit(0)

    colorama_init()

    watch_path = args.path if args.path is not None else os.getcwd()
    
    logger = Logger(watch_path)

    executor = Executor(logger, args.no_class_files)
    
    loop = EventLoop()

    schedule = Schedule(executor)

    def on_event(path, _):
        schedule.append(path, 1)

    def initial_scan():
        _, files = walk(watch_path, ["*.ui"], [])
        tasks = []
        for path in files:
            src = path
            data = UiData(path)
            dst = data.dst_path()
            add = True
            if os.path.exists(dst):
                m1 = os.path.getmtime(src)
                m2 = os.path.getmtime(dst)
                add = m2 <= m1
            if add:
                tasks.append(src)
        if len(tasks) > 0:
            schedule.append(tasks, 0)

    if not args.no_initial_scan:
        logger.print_info("Initial scan")
        initial_scan()

    watch = FileSystemWatch()
    logger.print_info("Watching {}".format(watch_path))
    watch.start(watch_path, on_event, recursive=True, include=["*.ui"])
    loop.start()

if __name__ == "__main__":
    main()