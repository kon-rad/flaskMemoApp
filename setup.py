from setuptools import setup


setup(
    name='flaskMemo',
    packages=['flaskMemo'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask_migrate',
        'flask_cors',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)