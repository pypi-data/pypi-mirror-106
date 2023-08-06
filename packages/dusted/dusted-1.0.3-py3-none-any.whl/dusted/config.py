import configparser
import logging
from pathlib import Path

import appdirs

logger = logging.getLogger(__name__)


class Config:
    def __init__(self):
        self.path = Path(appdirs.user_config_dir("dusted")) / "config.ini"
        self.config = configparser.ConfigParser()
        self.read()

    @property
    def dustforce_path(self):
        return self.config["DEFAULT"].get("dustforce_path", r"C:\Program Files (x86)\Steam\steamapps\common\Dustforce")

    @dustforce_path.setter
    def dustforce_path(self, new_path):
        self.config["DEFAULT"]["dustforce_path"] = new_path

    def read(self):
        logger.info(f"Reading config file: {self.path}")
        self.config.read(self.path)

    def write(self):
        logger.info(f"Writing config file: {self.path}")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w+") as file:
            self.config.write(file)

config = Config()
