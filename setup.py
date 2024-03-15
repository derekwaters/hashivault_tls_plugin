#!/usr/bin/env python

from setuptools import setup

requirements = [""]  # add Python dependencies here

setup(
    name='hashivault_tls_plugin',
    version='0.1',
    author='Derek Waters',
    author_email='dwaters@redhat.com',
    description='',
    long_description='',
    license='Apache License 2.0',
    keywords='ansible',
    url='http://github.com/derekwaters/hashivault_tls_plugin',
    packages=['hashivault_tls_plugin'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    install_requires=requirements,
    entry_points = {
        'awx.credential_plugins': [
            'hashivault_tls_kv_plugin = hashivault_tls_plugin:hashivault_tls_kv_plugin',
            'hashivault_tls_ssh_plugin = hashivault_tls_plugin:hashivault_tls_ssh_plugin'
        ]
    }
)