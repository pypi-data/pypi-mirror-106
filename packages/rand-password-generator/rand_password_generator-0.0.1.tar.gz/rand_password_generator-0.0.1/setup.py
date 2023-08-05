from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='rand_password_generator',
  version='0.0.1',
  description='A very basic random password generator',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/DevER-M/rand_password_generator/',  
  author='Dever',
  author_email='',
  license='MIT', 
  classifiers=classifiers,
  keywords='random password ', 
  packages=find_packages(),
  install_requires=['']
) 