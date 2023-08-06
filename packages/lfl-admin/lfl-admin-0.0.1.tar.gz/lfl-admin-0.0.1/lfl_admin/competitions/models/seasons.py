import logging
from datetime import timedelta

from bitfield import BitField
from django.db.models import DateField
from django.utils import timezone

from isc_common.common import undefined
from isc_common.models.audit import Model_withOldId
from isc_common.models.base_ref import BaseRefHierarcy, BaseRefHierarcyManager, BaseRefHierarcyQuerySet

logger = logging.getLogger(__name__)


class SeasonsQuerySet(BaseRefHierarcyQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class SeasonsManager(BaseRefHierarcyManager):
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
            'parent': record.parent.id if record.parent else None,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return SeasonsQuerySet(self.model, using=self._db)


class Seasons(BaseRefHierarcy, Model_withOldId):
    props = SeasonsManager.props()
    start_date = DateField()
    end_date = DateField()
    objects = SeasonsManager()

    @classmethod
    def unknown(cls):
        res, _ = cls.objects.get_or_create(
            code=undefined,
            defaults=dict(
                name='Нерпределенный',
                start_date=timezone.now(),
                end_date=timezone.now() + timedelta(days=1000))
        )
        return res

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'сезоны'
