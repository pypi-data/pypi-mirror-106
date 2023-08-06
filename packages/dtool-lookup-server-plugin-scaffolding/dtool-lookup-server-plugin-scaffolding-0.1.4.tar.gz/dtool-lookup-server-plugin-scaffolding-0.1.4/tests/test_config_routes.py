"""Test the /scaffolding/config blueprint route."""

import json
import dtool_lookup_server_plugin_scaffolding

from . import tmp_app_with_users  # NOQA
from . import snowwhite_token

def test_config_info_route(tmp_app_with_users):  # NOQA

    headers = dict(Authorization="Bearer " + snowwhite_token)
    r = tmp_app_with_users.get(
        "/scaffolding/config",
        headers=headers,
    )
    assert r.status_code == 200

    expected_content = {
        'some_public_plugin_specific_setting': 'public',
        'version': dtool_lookup_server_plugin_scaffolding.__version__}

    response = json.loads(r.data.decode("utf-8"))
    assert response == expected_content
