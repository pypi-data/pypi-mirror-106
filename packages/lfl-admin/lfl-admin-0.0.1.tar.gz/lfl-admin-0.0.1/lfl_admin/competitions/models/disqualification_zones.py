import logging

from bitfield import BitField
from django.db.models import SmallIntegerField

from isc_common.auth.models.user import User
from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import Model_withOldIds
from isc_common.models.base_ref import BaseRef, BaseRefManager, BaseRefQuerySet
from lfl_admin.region.models.regions import Regions

logger = logging.getLogger(__name__)


class Disqualification_zonesQuerySet(BaseRefQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Disqualification_zonesManager(BaseRefManager):

    @classmethod
    def props(cls):
        return BitField(flags=(
            ('active', 'active'),  # 1
        ), default=1, db_index=True)

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'code': record.code,
            'name': record.name,
            'description': record.description,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Disqualification_zonesQuerySet(self.model, using=self._db)


class Disqualification_zones(BaseRef, Model_withOldIds):
    editor = ForeignKeyProtect(User, null=True, blank=True)
    number_of_yellowsold = SmallIntegerField()
    props = Disqualification_zonesManager.props()
    region = ForeignKeyProtect(Regions)

    objects = Disqualification_zonesManager()

    @classmethod
    def unknown(cls):
        res, _ = cls.objects.get_or_create(
            region=Regions.unknown()
        )
        return res

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Зоны контроля дисквалификаций'
