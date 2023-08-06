import logging

from django.conf import settings
from django.db.models import DateTimeField, BigIntegerField

from isc_common import delAttr, setAttr
from isc_common.auth.models.user import User
from isc_common.auth.models.usergroup import UserGroup
from isc_common.fields.code_field import CodeField
from isc_common.fields.name_field import NameField
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.models.audit import AuditQuerySet, AuditManager, AuditModel
from lfl_admin.user_ext.models.administrators import Administrators, AdministratorsManager

logger = logging.getLogger(__name__)


class Administrators_viewQuerySet(AuditQuerySet):

    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)

class Administrators_viewManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'active': record.active,
            'birthday': record.birthday,
            'color': record.color,
            'deliting': record.deliting,
            'editing': record.editing,
            'editor_id': record.editor.id if record.editor else None,
            'first_name': record.first_name,
            'id': record.id,
            'last_login': record.last_login,
            'last_name': record.last_name,
            'middle_name': record.middle_name,
            'old_id': record.old_id,
            'password': record.password,
            'photo_src': f'http://{settings.IMAGE_CONTENT_HOST}:{settings.IMAGE_CONTENT_PORT}/{record.image_src}',
            'post_id': record.post_id,
            'post_name': record.post_name,
            'real_name': record.real_name,
            'register_date': record.register_date,
            'user_id': record.user_id,
            'username': record.username,
        }
        return res

    def get_queryset(self):
        return Administrators_viewQuerySet(self.model, using=self._db)

    def get_user(self, old_id):
        editor = super().getOptional(old_id=old_id)
        if editor is None:
            return None
        return editor.user


class Administrators_view(AuditModel):
    active = NameField()
    birthday = DateTimeField(null=True, blank=True)
    color = CodeField()
    editor = ForeignKeyProtect(User, related_name='Administrators_view_editor', null=True, blank=True)
    first_name = NameField()
    last_login = DateTimeField(null=True, blank=True)
    last_name = NameField()
    middle_name = NameField()
    old_id = BigIntegerField(db_index=True)
    password = CodeField()
    post_id = BigIntegerField(db_index=True)
    post_name = NameField()
    register_date = DateTimeField(null=True, blank=True)
    user_id = BigIntegerField(db_index=True)
    usergroup = ForeignKeyProtect(UserGroup)
    username = NameField()
    image_src = NameField()
    real_name = NameField()

    props = AdministratorsManager.props()

    objects = Administrators_viewManager()

    @classmethod
    def unknown(cls):
        return Administrators.unknown()

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Кросс-таблица'
        db_table = 'isc_common_administrator_view'
        managed = False
