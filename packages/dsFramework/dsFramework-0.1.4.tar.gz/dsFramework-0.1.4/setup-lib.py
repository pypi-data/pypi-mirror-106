import os
from setuptools import find_packages, setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='dsFramework',
    py_modules=['api_cli', 'dsFramework'],
    packages=[
        'cli',
        'lib',
        'lib.base_classes',
        'lib.config',
        'lib.pipeline',
        'lib.shared',
        'lib.utils',
    ],
    entry_points='''
        [console_scripts]
        ds-framework-cli=api_cli:cli
    ''',
    version='0.1.4',
    description='My first Python library',
    # url='http://pypi.python.org/pypi/PackageName/',
    author='oribrau@gmail.com',
    license='MIT',
    install_requires=required,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)

# for test -  python setup.py pytest
# for build wheel -  python setup.py bdist_wheel
# for source dist -  python setup.py sdist
# for build -  python setup.py build
# for install -  python setup.py install
# for uninstall - python -m pip uninstall ds_framework
# for install - python -m pip install dist/ds_framework-0.1.0-py3-none-any.whl

'''
    use
    1. python setup-lib.py install
    2. ds-framework-cli g model new_model_name
    3. twine check dist/*
    4. twine upload --repository-url https://pypi.org/legacy/ dist/*
    4. twine upload dist/*
'''
