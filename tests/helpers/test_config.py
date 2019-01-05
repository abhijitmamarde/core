import pydoc

from masonite.helpers import config, Dot


class TestConfig:

    def setup_method(self):
        self.config = config

    def test_config_can_get_value_from_file(self):
        assert self.config('config.application.DEBUG') == True

    def test_config_can_get_dict_value_lowercase(self):
        assert self.config('config.application.debug') == True

    def test_config_can_get_dict_default(self):
        assert self.config('config.sdff.na', 'default') == 'default'

    def test_dict_dot_returns_value(self):
        assert Dot().dict_dot('s3.test', {'s3': {'test': 'value'}}) == 'value'

    def test_config_can_get_dict_value_inside_dict(self):
        assert self.config('config.database.DATABASES.default') == 'sqlite'

    def test_config_can_get_dict_value_inside_dict_with_lowercase(self):
        assert self.config('config.database.databases.default') == 'sqlite'

    def test_config_can_get_dict_inside_dict_inside_dict(self):
        assert isinstance(self.config('config.database.databases.sqlite'), dict)

    def test_config_can_get_dict_inside_dict_inside_another_dict(self):
        assert self.config('config.storage.DRIVERS.s3.test_locations.test') == 'value'
