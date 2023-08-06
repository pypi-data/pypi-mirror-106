import logging

from isc_common.common import undefined
from isc_common.models.audit import Model_withOldId
from isc_common.models.base_ref import BaseRefHierarcyManager, BaseRefHierarcyQuerySet, BaseRefHierarcy

logger = logging.getLogger(__name__)


class Region_zonesQuerySet(BaseRefHierarcyQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Region_zonesManager(BaseRefHierarcyManager):

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
        return Region_zonesQuerySet(self.model, using=self._db)


class Region_zones(BaseRefHierarcy, Model_withOldId):
    objects = Region_zonesManager()

    @classmethod
    def unknown(cls):
        res, _ = cls.objects.get_or_create(
            code=undefined,
            defaults=dict(
                name='Нерпределенный',
            ))
        return res

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Зоны регионов'
