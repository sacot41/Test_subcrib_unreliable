
from setuptools import setup, find_packages

setup(
      name='Test',
      version='0.0.1',
      sdk_version='1.4.6',
      author='N.D.B. Tech',
      author_email='',
      description='',
      license='PRIVATE',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      package_data={"": ["*.gz", "*.txt"]}
      zip_safe=False,
      install_requires=[],
      entry_points="""
      [console_scripts]
      Test = Application:main
      """)