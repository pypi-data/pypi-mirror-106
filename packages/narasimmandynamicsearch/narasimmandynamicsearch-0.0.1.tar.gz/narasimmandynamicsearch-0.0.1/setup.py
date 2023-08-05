from setuptools import setup, find_packages
 




classifiers = [
  'Development Status :: 4 - Beta',
  'Intended Audience :: Science/Research',
  'Operating System :: Microsoft :: Windows',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3',
  'Programming Language :: Python :: 2'
]
 
setup(
  name='narasimmandynamicsearch',
  version='0.0.1',
  description='A sample python code value search in array in optimized way',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Narasimman Saravana',
  author_email='narasimman.saravana@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='dynamic search', 
  packages=find_packages(),
  install_requires=[''] 
)