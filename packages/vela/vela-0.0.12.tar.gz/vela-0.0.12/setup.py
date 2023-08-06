from setuptools import setup

setup(
    name='vela',
    version='0.0.12',
    py_modules=['vela'],
    install_requires=[],
    entry_points='''
        [console_scripts]
        vela=vela:vela
    ''',
)

