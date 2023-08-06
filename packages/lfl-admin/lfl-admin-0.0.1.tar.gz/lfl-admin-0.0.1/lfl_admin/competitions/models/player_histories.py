import logging

from bitfield import BitField

from isc_common.auth.models.user import User
from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import AuditManager, AuditQuerySet, AuditModel
from lfl_admin.competitions.models.calendar import Calendar
from lfl_admin.competitions.models.clubs import Clubs
from lfl_admin.competitions.models.formation import Formation
from lfl_admin.competitions.models.players import Players
from lfl_admin.competitions.models.tournaments import Tournaments

logger = logging.getLogger(__name__)


class Player_historiesQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Player_historiesManager(AuditManager):
    @classmethod
    def props(cls):
        return BitField(flags=(
            ('game_started', 'game_started'),  # 1
            ('substituted', 'substituted'),  # 1
            ('keeper', 'keeper'),  # 1
        ), default=0, db_index=True)

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Player_historiesQuerySet(self.model, using=self._db)


class Player_histories(AuditModel):
    club = ForeignKeyProtect(Clubs)
    editor = ForeignKeyProtect(User, null=True, blank=True)
    formation = ForeignKeyProtect(Formation)
    match = ForeignKeyProtect(Calendar)
    player = ForeignKeyProtect(Players)
    props = Player_historiesManager.props()
    tournament = ForeignKeyProtect(Tournaments)

    objects = Player_historiesManager()

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Данные об участии игрока в конкретном матче'
