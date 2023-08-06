import logging
import queue
import threading
from subprocess import PIPE, Popen

logger = logging.getLogger(__name__)

procs = []
stdout = queue.Queue()


def read_stdout(proc):
    while (line := proc.stdout.readline()) != b"":
        stdout.put(line.decode().strip())
    logger.info("Stdout reading thread reached end of file")
    procs.remove(proc)


def create_proc(uri):
    logger.info(f"Opening uri: {uri}")
    proc = Popen(["unbuffer", "xdg-open", uri], stdout=PIPE, stderr=PIPE)
    procs.append(proc)
    logger.info("Starting stdout reading thread")
    threading.Thread(target=lambda: read_stdout(proc)).start()
