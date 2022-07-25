from setuptools import setup, find_packages


setup(
    name='example_publish_pypi_medium',
    version='1.0',
    license='MIT',
    author="Julien Flandre",
    author_email='julien.flandre@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          're',
          'nltk'
      ],

)
