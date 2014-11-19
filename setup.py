#coding=utf-8
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

requires = [
    'six',
    'requests',
    'tornado',
    ]

setup(name='pysnowflake',
      version='0.1.2',
      description='Python Snowflake Kit',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries",
        ],
      author='Học .T Đỗ',
      author_email='hoc3010@gmail.com',
      url='https://github.com/tarzanjw/pysnowflake',
      keywords='snowflake server client',
      packages=['snowflake', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="snowflake",
      entry_points="""\
      [console_scripts]
      snowflake_start_server = snowflake.server:main
      """,
      )
