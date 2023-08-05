import os
from setuptools import setup, find_packages
 
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requirements = parse_requirements("requirements.txt", session=False)
requirements = [str(ir.requirement) for ir in install_requirements]

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 2.7'
]
 
setup(
  name='User Properties SDK',
  version='0.0.1',
  description='internal tool',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Saifur Rehman',
  author_email='saifurrahmankhankhan@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='sdk', 
  packages=find_packages(),
  install_requires=requirements 
)
