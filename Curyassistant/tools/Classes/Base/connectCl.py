import datetime

from peewee import *
from psycopg2.extensions import ISOLATION_LEVEL_SERIALIZABLE
from choice.bot.basic.dp_step.dp_poatgre import cfg
from choice.bot.basic.dp_step.peewee_Orm_postgre.models.models import PeeweeBase

# for catch make sure
class Connection:
    connector = PostgresqlDatabase(
        port=5432,
        database=cfg.dp_name,
        user=cfg.user,
        password=cfg.password,
        host=cfg.host,
        isolation_level=ISOLATION_LEVEL_SERIALIZABLE)



class integration(Model):
    pass

    class Meta:
        database = Connection.connector
        db_table = 'integration'


class User(Model):
    userId = TextField()
    UserName = TextField()
    password = TextField()
    joinedDate = DateTimeField(default=datetime.datetime.now, null=True)
    integration = BooleanField(null=True)
    integrationId = ForeignKeyField(model=integration, null=True)

    class Meta:
        database = Connection.connector
        db_table = 'User'


class YouTubeManagement(Model):
    User = ForeignKeyField(model=User)
    m_LastVideo = TextField()  # for keeping link
    m_FavVideo = TextField()   # for keeping link
    m_Array = IntegerField()  # for checking further about count method
    """..."""

    class Meta:
        database = Connection.connector
        db_table = 'YouTubeMng'

