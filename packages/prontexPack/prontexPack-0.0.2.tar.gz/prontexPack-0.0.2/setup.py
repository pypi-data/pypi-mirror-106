  
from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='prontexPack',
  version='0.0.2',
  description='a pack of functions and thing that can be cool in python',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read() + "\n\n\n" + open('GUIDE.txt').read(),
  url='',  
  author='Warren Stevens',
  author_email='no@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='pack', 
  packages=find_packages(),
  install_requires=[''] 
)