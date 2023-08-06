from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='datagovernancenew',
  version='0.0.2',
  description='A very basic cleaning data',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='vignesh',
  author_email='vigneshlike007@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='cleaning', 
  py_modules=['datagovernancenew'],
  packages=find_packages(),
  install_requires=[''] 
)
