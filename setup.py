from setuptools import setup, find_packages


setup(name= 'stepByStepApiTTT',
      version='1.0',
      description='Example python project for TTT meetup',
      packages=find_packages(),
      install_requires=[
          "pytest==7.1.2",
          "pytest-html==3.1.1",
          "requests==2.28.1",
      ]

)