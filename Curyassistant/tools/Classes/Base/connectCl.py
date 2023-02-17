import datetime

from peewee import *
from psycopg2.extensions import ISOLATION_LEVEL_SERIALIZABLE
from choice.bot.basic.dp_step.dp_poatgre import cfg
from choice.bot.basic.dp_step.peewee_Orm_postgre.models.models import PeeweeBase

# for catch make sure
class Connection:
    connector = PostgresqlDatabase(
        port=5432,
        database='Curie',
        user='postgres',
        password='123',
        host='localhost',
        isolation_level=ISOLATION_LEVEL_SERIALIZABLE)



class Integration(Model):
    setup = TextField()
    date = DateTimeField(default=datetime.datetime.now())
    login = TextField()
    password = TextField

    class Meta:
        database = Connection.connector
        db_table = 'integration'

class UserVibe(Model):
    user_id = IntegerField()
    vibe_id = IntegerField()

    class Meta:
        database = Connection.connector
        db_table = "UserVibes"

class MusicVibes(Model):
    name = TextField()
    status = IntegerField(default=1)  # it's been between 1 and 5
    tags = TextField()  # it must be as dict you know
    subscribers = BigIntegerField()
    # and so on

    class Meta:
        database = Connection.connector
        db_table = "MusicVibes"

class User(Model):
    userId = TextField()
    UserName = TextField()
    password = TextField()
    joinedDate = DateTimeField(default=datetime.datetime.now, null=True)
    integration = BooleanField(null=True)
    integrationId = ForeignKeyField(model=Integration, null=True)

    class Meta:
        database = Connection.connector
        db_table = 'User'


class MusicJanres(Model):
    User = ForeignKeyField(model=User)
    name = TextField()
    createdDate = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = Connection.connector
        db_table = 'MusicJanres'

class YouTubeManagement(Model):
    User = ForeignKeyField(model=User)
    m_LastVideo = TextField()  # for keeping link
    m_FavVideo = TextField()   # for keeping link
    m_Array = IntegerField()  # for checking further about count method
    """..."""

    class Meta:
        database = Connection.connector
        db_table = 'YouTubeMng'

def Create_Table():
    Connection.connector.connect()
    Connection.connector.create_tables([MusicJanres])




