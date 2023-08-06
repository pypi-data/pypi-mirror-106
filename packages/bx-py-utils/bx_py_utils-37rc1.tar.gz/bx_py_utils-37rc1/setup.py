# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bx_py_utils',
 'bx_py_utils.aws',
 'bx_py_utils.humanize',
 'bx_py_utils.test_utils']

package_data = \
{'': ['*']}

install_requires = \
['python-stdnum']

entry_points = \
{'console_scripts': ['publish = bx_py_utils_tests.publish:publish']}

setup_kwargs = {
    'name': 'bx-py-utils',
    'version': '37rc1',
    'description': 'Various Python utility functions',
    'long_description': '# Boxine - bx_py_utils\n\nVarious Python utility functions\n\n\n## Quickstart\n\n```bash\npip install bx_py_utils\n```\n\n\n## Existing stuff\n\nHere only a simple list about existing utilities.\nPlease take a look into the sources and tests for deeper informations.\n\n\n### test utilities\n\n* `datetime.parse_dt()` - Handy `datetime.strptime()` convert\n* `assert_json_requests_mock()` - Check the requests history of `requests_mock.mock()`\n* `assert_equal()` - Compare objects with a nice diff using pformat\n* `assert_text_equal()` - Compare text strings with a nice diff\n* `assert_snapshot` - Helper for quick snapshot test functionality (comparing value with one stored in a file using json)\n* `assert_text_snapshot` - Same as `assert_snapshot` comparing text strings\n* `assert_py_snapshot` - Snapshot test using `PrettyPrinter()`\n\n### humanize\n\n* `humanize.time.human_timedelta()` - Converts a time duration into a friendly text representation. (`X ms`, `sec`, `minutes` etc.)\n* `pformat()` - Better `pretty-print-format` using JSON with fallback to `pprint.pformat()`\n\n\n### AWS stuff\n\n* `bx_py_utils.aws.secret_manager.SecretsManager` - Get values from AWS Secrets Manager\n* `bx_py_utils.test_utils.mock_aws_secret_manager.SecretsManagerMock` - Mock our `SecretsManager()` helper in tests\n* `bx_py_utils.test_utils.mock_boto3session.MockedBoto3Session` - Mock `boto3.session.Session()` (Currently only `get_secret_value()`)\n* `bx_py_utils.aws.client_side_cert_manager.ClientSideCertManager` - Helper to manage client-side TLS certificate via AWS Secrets Manager\n\n### GraphQL\n\n* `graphql_introspection.introspection_query` Generate an introspection query to get an introspection doc.\n* `graphql_introspection.complete_query` Generate a full query for all fields from an introspection doc.\n\n### misc\n\n* `dict_utils.dict_get()` - nested dict `get()`\n* `dict_utils.pluck()` - Extract values from a dict, if they are present\n* `environ.cgroup_memory_usage()` - Get the memory usage of the current cgroup\n* `error_handling.print_exc_plus()` - Print traceback information with a listing of all the local variables in each frame\n* `iteration.chunk_iterable()` - Create chunks off of any iterable\n* `processify.processify()` - Will execute the decorated function in a separate process\n* `anonymize.anonymize()` - Anonymize a string (With special handling of email addresses)\n* `hash_utils.url_safe_hash()` - Generate URL safe hashes\n* `compat.removeprefix()` - Backport of `str.removeprefix` from PEP-616\n* `compat.removesuffix()` - Backport of `str.removesuffix` from PEP-616\n\n\n## Backwards-incompatible changes\n\n### v36 -> v37 - Outsourcing Django stuff\n\nWe split `bx_py_utils` and moved all Django related utilities into the separated project:\n\n* https://github.com/boxine/bx_django_utils\n\nSo, `bx_py_utils` is better usable in non-Django projects, because Django will not installed as decency of "bx_py_utils"\n\n\n## developing\n\nTo start developing e.g.:\n\n```bash\n~$ git clone https://github.com/boxine/bx_py_utils.git\n~$ cd bx_py_utils\n~/bx_py_utils$ make\nhelp                 List all commands\ninstall-poetry       install or update poetry\ninstall              install via poetry\nupdate               Update the dependencies as according to the pyproject.toml file\nlint                 Run code formatters and linter\nfix-code-style       Fix code formatting\ntox-listenvs         List all tox test environments\ntox                  Run pytest via tox with all environments\ntox-py36             Run pytest via tox with *python v3.6*\ntox-py37             Run pytest via tox with *python v3.7*\ntox-py38             Run pytest via tox with *python v3.8*\ntox-py39             Run pytest via tox with *python v3.9*\npytest               Run pytest\npytest-ci            Run pytest with CI settings\npublish              Release new version to PyPi\nclean                Remove created files from the test project\n```\n\n\n## License\n\n[MIT](LICENSE). Patches welcome!\n\n## Links\n\n* https://pypi.org/project/bx-py-utils/\n',
    'author': 'Jens Diemer',
    'author_email': 'jens.diemer@boxine.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0.0',
}


setup(**setup_kwargs)
