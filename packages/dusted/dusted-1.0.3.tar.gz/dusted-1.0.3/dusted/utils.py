import logging
from pathlib import Path
from subprocess import PIPE, Popen

import requests
from dustmaker import read_map

from .config import config
from .replay import read_replay, write_replay

logger = logging.getLogger(__name__)


def load_replay_from_dustkid(replay_id):
    logger.info(f"Loading replay {replay_id} from dustkid")
    data = {"replay": replay_id}
    response = requests.post("http://54.69.194.244/backend8/get_replay.php", data=data)
    replay = read_replay(response.content)
    return replay

def load_level(level_id):
    level = load_level_from_file(level_id)
    if level is None:
        level = load_level_from_dustkid(level_id)
    return level

def load_level_from_file(level_id):
    logger.info(f"Loading level {level_id} from file")
    for path in ("content/levels2", "content/levels3", "user/levels", "user/level_src"):
        level_path = Path(config.dustforce_path) / path / level_id
        try:
            with level_path.open("rb") as f:
                return read_map(f.read())
        except FileNotFoundError:
            pass

def load_level_from_dustkid(level_id):
    logger.info(f"Loading level {level_id} from dustkid")
    data = {"id": level_id}
    response = requests.post("http://54.69.194.244/backend8/level.php", data=data)
    level = read_map(response.content)
    return level

def load_replay_from_file(filepath):
    logger.info(f"Loading replay from file: {filepath}")
    with open(filepath, "rb") as f:
        return read_replay(f.read())

def write_replay_to_file(filepath, replay):
    logger.info(f"Writing replay to file: {filepath}")
    with open(filepath, "wb") as f:
        f.write(write_replay(replay))
