import os
import pathlib

from tg_bot.etc.conf import settings
from tg_bot.etc.management.commands import migrate


settings.BASE_DIR = pathlib.Path(__file__).parent
migrate.Command().handle()
