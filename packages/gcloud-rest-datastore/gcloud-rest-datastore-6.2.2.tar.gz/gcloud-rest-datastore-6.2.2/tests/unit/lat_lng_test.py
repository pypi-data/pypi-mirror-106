from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from builtins import str
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from future import standard_library
standard_library.install_aliases()
from builtins import object
import pytest
from gcloud.rest.datastore import LatLng


class TestLatLng(object):
    @staticmethod
    def test_from_repr(lat_lng):
        original_latlng = lat_lng
        data = {
            'latitude': original_latlng.lat,
            'longitude': original_latlng.lon,
        }

        output_order = LatLng.from_repr(data)

        assert output_order == original_latlng

    @staticmethod
    def test_to_repr():
        lat = 49.2827
        lon = 123.1207
        latlng = LatLng(lat, lon)

        r = latlng.to_repr()

        assert r['latitude'] == lat
        assert r['longitude'] == lon

    @staticmethod
    def test_repr_returns_to_repr_as_string(lat_lng):
        assert repr(lat_lng) == str(lat_lng.to_repr())

    @staticmethod
    @pytest.fixture(scope='session')
    def lat_lng()          :
        return LatLng(49.2827, 123.1207)
