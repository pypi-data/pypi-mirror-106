import logging

from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet
from isc_common.models.e_mails import E_mails
from lfl_admin.region.models.region_zones import Region_zones

logger = logging.getLogger(__name__)


class Region_zone_e_mailsQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Region_zone_e_mailsManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Region_zone_e_mailsQuerySet(self.model, using=self._db)


class Region_zone_e_mails(AuditModel):
    zone = ForeignKeyProtect(Region_zones)
    e_mail = ForeignKeyProtect(E_mails)

    objects = Region_zone_e_mailsManager()

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс таблица'
        unique_together = (('zone', 'e_mail'),)
