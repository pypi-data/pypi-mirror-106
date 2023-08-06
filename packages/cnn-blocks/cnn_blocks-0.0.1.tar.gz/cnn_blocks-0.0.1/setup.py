from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='cnn_blocks',
  version='0.0.1',
  description='Construct new CNN architectures using famous CNN blocks',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url="https://github.com/mitul01/CNN_Architectures",
  author='Mitul Tandon',
  author_email='mtandon_be18@thapar.edu',
  license='MIT',
  classifiers=classifiers,
  keywords=['python','Machine Learning','Deep Learning','CNN','RESNET','VGG','Inception'],
  packages=find_packages(),
  install_requires=['']
)
