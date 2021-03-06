import pytest
import vcr
from constructor_io import ConstructorIO

class TestConstructorIO:

    def test_encodes_parameters(self):
        constructor = ConstructorIO(api_token="boinka", autocomplete_key="doinka")
        serialized_params = constructor\
            ._serialize_params({'foo': [1, 2], 'bar': {'baz': ['a', 'b']}})
        assert serialized_params == "foo=%5B1%2C+2%5D&bar=%7B%27baz%27%3A+%5B%27a%27%2C+%27b%27%5D%7D"

    def test_creates_urls_correctly(self):
        constructor = ConstructorIO(api_token="boinka", autocomplete_key="a-test-autocomplete-key")
        generated_url = constructor._make_url('v1/test')
        assert generated_url == 'https://ac.cnstrc.com/v1/test?autocomplete_key=a-test-autocomplete-key'

    def test_set_api_token(self):
        api_token = 'a-test-api-key',
        constructor = ConstructorIO(api_token=api_token, autocomplete_key="boinka")
        assert constructor._api_token == api_token

    def test_set_ac_key(self):
        autocomplete_key = 'a-test-autocomplete-key'
        constructor = ConstructorIO(autocomplete_key=autocomplete_key, api_token="boinka")
        assert constructor._autocomplete_key == autocomplete_key

    def test_ac_query(self):
        with vcr.use_cassette("fixtures/ac.cnstrc.com/query-success.yaml"):
            constructor = ConstructorIO(
                api_token = "apiToken",
                autocomplete_key = "autocompleteKey",
                protocol = "http",
                host = "ac.cnstrc.com"
            )
            autocompletes = constructor.query(
                query_str = "a"
            )
            assert autocompletes != None
            assert type(autocompletes) == dict

    def test_add(self):
        with vcr.use_cassette("fixtures/ac.cnstrc.com/add-success.yaml"):
            constructor = ConstructorIO(
                api_token = "apiToken",
                autocomplete_key = "autocompleteKey",
                protocol = "http",
                host = "ac.cnstrc.com"
            )
            resp = constructor.add(
                item_name = "boinkamoinka",
                autocomplete_section = "Search Suggestions"
            )
            assert resp == True

    def test_remove(self):
        with vcr.use_cassette("fixtures/ac.cnstrc.com/remove-success.yaml"):
            constructor = ConstructorIO(
                api_token = "apiToken",
                autocomplete_key = "autocompleteKey",
                protocol = "http",
                host = "ac.cnstrc.com"
            )
            resp = constructor.remove(
                item_name = "racer",
                autocomplete_section = "Search Suggestions"
            )
            assert resp == True

    def test_modify(self):
        with vcr.use_cassette("fixtures/ac.cnstrc.com/modify-success.yaml"):
            constructor = ConstructorIO(
                api_token = "apiToken",
                autocomplete_key = "autocompleteKey",
                protocol = "http",
                host = "ac.cnstrc.com"
            )
            resp = constructor.modify(
                item_name = "Stanley_Steamer",
                new_item_name = "Newer_Stanley_Steamer",
                suggested_score = 100,
                autocomplete_section = "Search Suggestions"
            )
            assert resp == True

    def test_conversion(self):
        with vcr.use_cassette("fixtures/ac.cnstrc.com/conversion-success.yaml"):
            constructor = ConstructorIO(
                api_token = "apiToken",
                autocomplete_key = "autocompleteKey",
                protocol = "http",
                host = "ac.cnstrc.com"
            )
            resp = constructor.track_conversion(
                term = "Stanley_Steamer",
                autocomplete_section = "Search Suggestions"
            )
            assert resp == True

    def test_search_no_num_res(self):
        with vcr.use_cassette("fixtures/ac.cnstrc.com/search-noname-success.yaml"):
            constructor = ConstructorIO(
                api_token = "apiToken",
                autocomplete_key = "autocompleteKey",
                protocol = "http",
                host = "ac.cnstrc.com"
            )
            resp = constructor.track_search(
                term = "Stanley_Steamer",
                num_results = 10,
                autocomplete_section = "Search Suggestions"
            )
            assert resp == True

    def test_search_num_res(self):
        with vcr.use_cassette("fixtures/ac.cnstrc.com/search-success.yaml"):
            constructor = ConstructorIO(
                api_token = "apiToken",
                autocomplete_key = "autocompleteKey",
                protocol = "http",
                host = "ac.cnstrc.com"
            )
            resp = constructor.track_search(
                term = "Stanley_Steamer",
                num_results = 10,
                autocomplete_section = "Search Suggestions"
            )
            assert resp == True

    def test_click_through(self):
        with vcr.use_cassette("fixtures/ac.cnstrc.com/click-through-success.yaml"):
            constructor = ConstructorIO(
                api_token = "apiToken",
                autocomplete_key = "autocompleteKey",
                protocol = "http",
                host = "ac.cnstrc.com"
            )
            resp = constructor.track_click_through(
                term = "Stanley_Steamer",
                autocomplete_section = "Search Suggestions"
            )
            assert resp == True
