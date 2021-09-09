"""
Base model class for all models.
Every new model has to be inherited from this class.
"""
import uuid
from datetime import datetime

from django.db.models import Model, UUIDField, DateTimeField


class BaseDbModel(Model):
    """
    Base model class which describes the attributes and methods
    which have to exist in all models of the app.
    """
    class Meta:
        abstract = True

    id = UUIDField(name='id', unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=None, null=True)

    @property
    def _update_allowed_fields(self) -> list:
        """
        Defines a list of fields of the model which can be updated.
        :return: list
        """
        raise NotImplementedError('Each model has to have its list of update allowed fields')

    def update_db_record(self, update_body: dict):
        """
        Updates attribute of any BaseModel subclass object
        :param update_body: Dict with keys to be updated
        :return: None
        """
        for attribute, value in update_body.items():
            if attribute in self._update_allowed_fields:
                setattr(self, attribute, value)
        self.updated_at = datetime.now()
        self.save()
