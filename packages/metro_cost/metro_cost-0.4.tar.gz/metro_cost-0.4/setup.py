from setuptools import setup

setup(name='metro_cost',
      version='0.4',
      description='A model that can predict the cost of metro construction',
      url='http://github.com/storborg/metro_cost',
      author='Manolo',
      author_email='manolo.szc@example.com',
      license='MIT',
      packages=['metro_cost'],
      install_requires=[
            'pandas',
            'numpy',
            'matplotlib',
            'sklearn',
            'catboost',
            'lightgbm'
      ],
      zip_safe=False)