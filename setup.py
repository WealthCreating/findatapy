from setuptools import setup, find_packages

setup(name='findatapy',
      version='0.05',
      description='Market data library',
      author='Saeed Amen',
      author_email='saeed@cuemacro.com',
      license='Apache 2.0',
      keywords = ['pandas', 'data', 'Bloomberg', 'tick', 'stocks', 'equities'],
      url = 'https://github.com/cuemacro/findatapy',
      packages = find_packages(),
      include_package_data = True,
      install_requires = ['pandas',
                          'twython',
                          'pytz',
                          'requests',
                          'numpy',
                          'pandas_datareader',
                          'fxcmpy',
                          'alpha_vantage',
                          'quandl',
                          'statsmodels',
                          'multiprocess',
                          'multiprocessing_on_dill',
                          'pathos',
                          'redis',
                          'numba',
                          'blosc',
                          'openpyxl'],
	  zip_safe=False)