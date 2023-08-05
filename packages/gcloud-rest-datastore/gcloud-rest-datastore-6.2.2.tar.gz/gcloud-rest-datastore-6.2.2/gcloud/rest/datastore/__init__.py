from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from future import standard_library
standard_library.install_aliases()
from pkg_resources import get_distribution
__version__ = get_distribution('gcloud-rest-datastore').version

from gcloud.rest.datastore.constants import CompositeFilterOperator
from gcloud.rest.datastore.constants import Consistency
from gcloud.rest.datastore.constants import Direction
from gcloud.rest.datastore.constants import Mode
from gcloud.rest.datastore.constants import MoreResultsType
from gcloud.rest.datastore.constants import Operation
from gcloud.rest.datastore.constants import PropertyFilterOperator
from gcloud.rest.datastore.constants import ResultType
from gcloud.rest.datastore.datastore import Datastore
from gcloud.rest.datastore.datastore import SCOPES
from gcloud.rest.datastore.datastore_operation import DatastoreOperation
from gcloud.rest.datastore.entity import Entity
from gcloud.rest.datastore.entity import EntityResult
from gcloud.rest.datastore.filter import CompositeFilter
from gcloud.rest.datastore.filter import Filter
from gcloud.rest.datastore.filter import PropertyFilter
from gcloud.rest.datastore.key import Key
from gcloud.rest.datastore.key import PathElement
from gcloud.rest.datastore.lat_lng import LatLng
from gcloud.rest.datastore.mutation import MutationResult
from gcloud.rest.datastore.projection import Projection
from gcloud.rest.datastore.property_order import PropertyOrder
from gcloud.rest.datastore.query import GQLQuery
from gcloud.rest.datastore.query import Query
from gcloud.rest.datastore.query import QueryResultBatch
from gcloud.rest.datastore.value import Value


__all__ = ['__version__', 'CompositeFilter', 'CompositeFilterOperator',
           'Consistency', 'Datastore', 'DatastoreOperation', 'Direction',
           'Entity', 'EntityResult', 'Filter', 'GQLQuery', 'Key', 'LatLng',
           'Mode', 'MoreResultsType', 'MutationResult', 'Operation',
           'PathElement', 'Projection', 'PropertyFilter',
           'PropertyFilterOperator', 'PropertyOrder', 'Query',
           'QueryResultBatch', 'ResultType', 'SCOPES', 'Value']
