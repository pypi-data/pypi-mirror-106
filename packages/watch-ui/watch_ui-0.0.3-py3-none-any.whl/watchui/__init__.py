import os
from eventloop import EventLoop, FileSystemWatch, SingleShotTimer, walk
import argparse
from colorama import Fore, Back, Style, init as colorama_init
import xml.etree.ElementTree as ET
from subprocess import Popen, PIPE, check_output
import datetime
import sys

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

class Logger:
    def __init__(self, path):
        self._path = path
        
    def print_info(self, msg):
        print(Fore.WHITE + now_str() + " " + Fore.YELLOW + Style.BRIGHT + msg + Fore.RESET + Style.NORMAL)

    def print_error(self, msg):
        print(Fore.WHITE + now_str() + " " + Fore.RED + msg + Fore.RESET)

    def print_compiled(self, src, dst):
        print(Fore.WHITE + now_str() + " " + Fore.GREEN + Style.BRIGHT + os.path.relpath(src, self._path) + Fore.WHITE + " -> " + Fore.GREEN + os.path.relpath(dst, self._path) + Fore.RESET + Style.NORMAL)

class Runner:
    def __init__(self, logger):
        self._logger = logger
        if sys.platform == 'win32':
            ext = ".bat"
        else:
            ext = ""
        if has_PySide2:
            uic = ["pyside2-uic" + ext]
        elif has_PyQt5:
            uic = ["pyuic5" + ext]
        self._uic = uic

    def run(self, src, dst):
        uic = self._uic
        logger = self._logger

        base = os.path.dirname(src)
        src_ = os.path.relpath(src, base)
        dst_ = os.path.relpath(dst, base)

        args = uic + ["-x", "-o", dst_, src_]
        #print(args)
        process = Popen(args, stdout=PIPE, stderr=PIPE, cwd=base)
        stdout, stderr = process.communicate()
        codec = 'cp1251' if sys.platform == 'win32' else 'utf-8'
        debug_print(stdout.decode(codec))
        debug_print(stderr.decode(codec))
        logger.print_compiled(src, dst)

def dst_path(path):
    #print("path", path)
    tree = ET.parse(path)
    root = tree.getroot()
    item = root.find('class')
    class_ = item.text
    return os.path.join(os.path.dirname(path), "Ui_{}.py".format(class_))
    
class Schedule:

    def __init__(self, logger, runner):
        self._timer = None
        self._items = []
        self._logger = logger
        self._runner = runner
        
    def onTimer(self):
        #print("onTimer")
        runner = self._runner
        for src in self._items:
            dst = dst_path(src)
            runner.run(src, dst)
        self._items = []

    def append(self, path, timeout):
        #print("append", path)
        items = self._items
        if isinstance(path, list):
            paths = path
        else:
            paths = [path]
        #print("append", paths)
        for path in paths:
            if path not in items:
                items.append(path)
        self._schedule(timeout)

    def _schedule(self, timeout):
        timer = self._timer
        if timer:
            timer.stop()
        timer = SingleShotTimer()
        timer.start(timeout, self.onTimer)
        self._timer = timer

def main():
    parser = argparse.ArgumentParser(prog="watch-ui")
    parser.add_argument('path',nargs='?',help="Path to watch, defaults to current directory")
    parser.add_argument('--no-initial-scan', action='store_true', help="Skip initial scan")
    args = parser.parse_args()

    #print(args); exit(0)

    colorama_init()

    watch_path = args.path if args.path is not None else os.getcwd()
    
    logger = Logger(watch_path)

    runner = Runner(logger)
    
    loop = EventLoop()

    schedule = Schedule(logger, runner)

    def on_event(path, _):
        schedule.append(path, 1)

    def initial_scan():
        _, files = walk(watch_path, ["*.ui"], [])
        srcs = []
        for path in files:
            src = path
            dst = dst_path(src)
            add = True
            if os.path.exists(dst):
                m1 = os.path.getmtime(src)
                m2 = os.path.getmtime(dst)
                add = m2 <= m1
            if add:
                srcs.append(src)
        if len(srcs) > 0:
            schedule.append(srcs, 0)

    if not args.no_initial_scan:
        logger.print_info("Initial scan")
        initial_scan()

    watch = FileSystemWatch()
    logger.print_info("Watching {}".format(watch_path))
    watch.start(watch_path, on_event, recursive=True, include=["*.ui"])
    loop.start()

if __name__ == "__main__":
    main()