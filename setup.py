from setuptools import setup


setup(
    name='flaskMemo',
    packages=['flaskMemo'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask_migrate',
    ],
)