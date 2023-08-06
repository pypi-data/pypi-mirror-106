from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='datagovernance',
  version='0.1',
  description='A very basic cleaning data',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='vignesh',
  author_email='marilike007@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='cleaning', 
  py_modules=['py_data_governance'],
  packages=find_packages(),
  install_requires=[''] 
)
