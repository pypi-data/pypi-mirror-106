# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['airflow_dbt_python', 'airflow_dbt_python.operators']

package_data = \
{'': ['*']}

install_requires = \
['apache-airflow>=1.10.12', 'dbt-core>=0.19,<0.20']

extras_require = \
{'all': ['dbt-postgres>=0.19,<0.20',
         'dbt-redshift>=0.19,<0.20',
         'dbt-snowflake>=0.19,<0.20',
         'dbt-bigquery>=0.19,<0.20'],
 'bigquery': ['dbt-bigquery>=0.19,<0.20'],
 'postgres': ['dbt-postgres>=0.19,<0.20'],
 'redshift': ['dbt-redshift>=0.19,<0.20'],
 'snowflake': ['dbt-snowflake>=0.19,<0.20']}

setup_kwargs = {
    'name': 'airflow-dbt-python',
    'version': '0.2.0',
    'description': 'A dbt operator for Airflow that uses the dbt Python package',
    'long_description': None,
    'author': 'Tomás Farías Santana',
    'author_email': 'tomas@tomasfarias.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
