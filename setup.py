from distutils.core import setup

setup(name='fuse',
      description='a fusion admin client',
      version='0.1.0',
      author='Rackspace',
      author_email='jason@duncancreek.net',
      license='Apache License (2.0)',
      classifiers=["Programming Language :: Python"],
      url='https://github.com/heat-tools/fuse',
      scripts=['fuse'],
      install_requires=[
          'hot',
          'requests',
      ]
      )
