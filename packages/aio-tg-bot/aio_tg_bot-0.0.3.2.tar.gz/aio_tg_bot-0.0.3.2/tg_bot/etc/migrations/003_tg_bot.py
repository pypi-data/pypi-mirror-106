import peewee

from tg_bot.etc.conf import settings
from tg_bot.etc.database import models, fields, validators


# noinspection PyUnusedLocal
def migrate(migrator, database, fake=False, **kwargs):
    migrator.rename_table("broadcast", "tg_bot_broadcast")


# noinspection PyUnusedLocal
def rollback(migrator, database, fake=False, **kwargs):
    migrator.rename_table("tg_bot_broadcast", "broadcast")

