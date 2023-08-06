# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'python'}

packages = \
['vault_client']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.20.0']

setup_kwargs = {
    'name': 'simple-vault-client',
    'version': '0.0.1',
    'description': 'Dead simple HashiCorp Vault consumer client',
    'long_description': '# Vault Client\n\n![Java](https://github.com/mbrancato/vault-client/workflows/Java%20CI%20with%20Gradle/badge.svg)\n![Python](https://github.com/mbrancato/vault-client/workflows/Python%20package/badge.svg)\n\nVault Client is designed to be a dead simple client library for Vault consumer \napplications. The purpose is to implement a robust Vault client that makes it \neasy for developers to instrument HashiCorp Vault into applications.\n\nAll implementations of Vault Client will use a common API. After configuring \nVault authentication, the developer simply needs to replace the location of a \nneeded secret in their code with the appropriate `read` method. The Vault \nClient object will handle authentication renewal and secret / lease renewal.\n\n## Quick Start Example\n\n**Java**\n\n```java\nString dbUser;\nString dbPass;\nVaultClient vault = new VaultClient();\nvault.setAuthMethod("gcp");\nvault.setAuthRole("app_name");\nvault.setVaultAddr("https://myvault.company.org");\n\ndbUser = vault.read("database/creds/my-role", "username");\ndbPass = vault.read("database/creds/my-role", "password");\n```\n\n**Python**\n\n```python\nvault = VaultClient(\n    vault_addr="https://myvault.company.org",\n    auth_method="gcp",\n    auth_role="app_name",\n)\n\ndb_user = vault.read("database/creds/my-role", "username")\ndb_pass = vault.read("database/creds/my-role", "password")\n```\n\n## Feature Matrix\n\n|                       | Java | Python | C#/.NET |\n|----------------------:|:----:|:------:|:-------:|\n| Language Support      | ⚠️   | ⚠️     | ❌       |\n| Auth Renewal (Async)  | 🚧   | 🚧     | ❌       |\n| Generic Read          | ✅   | ✅     | ❌       |\n| KV Read               | ✅   | ✅     | ❌       |\n| Lease Renewal (Async) | ✅   | ✅     | ❌       |\n| JWT Auth              | ✅   | ✅     | ❌       |\n| GCP Auth (GCE)        | ✅   | ✅     | ❌       |\n| Azure Auth            | 🚧   | ❌     | ❌       |\n| AppRole Auth          | ❌   | ❌     | ❌       |\n| TLS Auth              | ❌   | ❌     | ❌       |\n\n✅ - Implemented  \n❌ - Not implemented  \n⚠️ - Partially implemented  \n🚧 - Under construction  \n\n',
    'author': 'Mike Brancato',
    'author_email': 'mike@mikebrancato.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mbrancato/vault-client',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5.0,<4',
}


setup(**setup_kwargs)
