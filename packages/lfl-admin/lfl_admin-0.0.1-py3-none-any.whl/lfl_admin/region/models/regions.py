import logging

from bitfield import BitField

from isc_common.common import undefined
from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import Model_withOldId
from isc_common.models.base_ref import BaseRefHierarcy, BaseRefQuerySet, BaseRefManager
from isc_common.models.standard_colors import Standard_colors
from lfl_admin.competitions.models.seasons import Seasons
from lfl_admin.region.models.region_zones import Region_zones

logger = logging.getLogger(__name__)


class RegionsQuerySet(BaseRefQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class RegionsManager(BaseRefManager):

    @classmethod
    def props(cls):
        return BitField(flags=(
            ('active', 'Актуальность'),  # 1
            ('select_division', 'select_division'),  # 2
            ('parimatch', 'parimatch'),  # 4
            ('submenu', 'submenu'),  # 8
            ('leagues_menu', 'leagues_menu'),  # 16
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
        return RegionsQuerySet(self.model, using=self._db)


class Regions(BaseRefHierarcy, Model_withOldId):
    color = ForeignKeyProtect(Standard_colors, null=True, blank=True)
    season = ForeignKeyProtect(Seasons)
    zone = ForeignKeyProtect(Region_zones)
    props = RegionsManager.props()

    objects = RegionsManager()

    @classmethod
    def unknown(cls):
        res, _ = cls.objects.get_or_create(
            code=undefined,
            defaults=dict(
                name='Нерпределенный',
                season=Seasons.unknown(),
                zone=Region_zones.unknown()
            ))
        return res

    def __str__(self):
        return f'ID:{self.id}, code: {self.code}, name: {self.name}, description: {self.description}, color: [{self.color}], season: [{self.season}], zone: [{self.zone}], props: [{self.props}]'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Регионы'
