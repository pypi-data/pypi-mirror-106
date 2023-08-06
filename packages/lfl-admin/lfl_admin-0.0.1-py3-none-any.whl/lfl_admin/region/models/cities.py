import logging

from isc_common.models.audit import Model_withOldId
from isc_common.models.base_ref import BaseRef, BaseRefManager, BaseRefQuerySet

logger = logging.getLogger(__name__)


class CitiesQuerySet(BaseRefQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class CitiesManager(BaseRefManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'code': record.code,
            'name': record.name,
            'description': record.description,
            'parent': record.parent.id if record.parent else None,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return CitiesQuerySet(self.model, using=self._db)


class Cities(BaseRef, Model_withOldId):
    # region = ForeignKeyProtect(Regions, null=True, blank=True)

    objects = CitiesManager()

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Города'
