from setuptools import setup


setup(name='lexsetAPI',
      version='0.0.4',
      author='F. Bitonti',
      author_email='Francis@lexset.ai',
      license='Apache 2.0',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 2'
      ],
      packages=['lexsetAPI'],
      install_requires=[
          'pyjson',
          'yaml',
          'base64',
          'requests'
      ]
)
