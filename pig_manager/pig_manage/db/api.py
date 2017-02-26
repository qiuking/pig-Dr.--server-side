import abc

from oslo_db import api as db_api
from oslo_log import log as logging
import six

from pig_manage import config as conf

CONF = conf.CONF

_BACKEND_MAPPING = {'sqlalchemy': 'pig_manage.db.sqlalchemy.api'}
IMPL = db_api.DBAPI.from_config(CONF, backend_mapping=_BACKEND_MAPPING,
                                lazy=True)

LOG = logging.getLogger(__name__)


def get_instance():
    """Return a DB API instance."""
    return IMPL

@six.add_metaclass(abc.ABCMeta)
class Connection(object):
    """Base class for storage system connections."""

    @abc.abstractmethod
    def __init__(self):
        """Constructor."""

    @abc.abstractmethod
    def get_sow_list(cls, context, filters=None, limit=None,
            marker=None, sort_key=None, sort_dir=None):
        """return all sow record in database."""

    @abc.abstractmethod
    def get_boar_list(cls, context, filters=None, limit=None,
            marker=None, sort_key=None, sort_dir=None):
        """return all sow record in database."""