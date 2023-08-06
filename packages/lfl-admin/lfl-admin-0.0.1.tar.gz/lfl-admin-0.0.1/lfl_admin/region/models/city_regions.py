import logging

from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from lfl_admin.region.models.cities import Cities
from lfl_admin.region.models.regions import Regions

logger = logging.getLogger(__name__)


class City_regionsQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class City_regionsManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return City_regionsQuerySet(self.model, using=self._db)


class City_regions(AuditModel):
    region = ForeignKeyProtect(Regions)
    city = ForeignKeyProtect(Cities)

    objects = City_regionsManager()

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс таблица'
        unique_together = (('city', 'region'),)
