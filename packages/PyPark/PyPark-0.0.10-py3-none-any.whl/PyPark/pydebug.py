import logging
import os
import threading
import time


def pydebug_run():
    th = threading.Thread(target=__run)
    th.setDaemon(True)
    th.start()


def __run():
    while True:
        try:
            import pydevd_pycharm
            debug_host = os.environ.get("PY_DEBUG_SERVER")
            if debug_host != "":
                if ":" in debug_host:
                    ip, port = debug_host.split(":")
                else:
                    ip = debug_host
                    port = 9898
                logging.warning(f"======DEBUG SERVER: {debug_host}======")
                pydevd_pycharm.settrace(ip, port=int(port), stdoutToServer=True,
                                        stderrToServer=True)
            break
        except Exception as e:
            if "Connection refused" in str(e):
                logging.warning("Debug Server Connection refused...try..")
            else:
                logging.warning("""
                        ----------------
                        
                        $> pip3 install pydevd-pycharm
                        $> export DEBUG_HOST="192.168.1.100:9898"
                            
                        ----------------
                        """)
                logging.error(f"Debug Error: {str(e)}")
        time.sleep(3)
