from setuptools import setup, find_packages

setup(
  name = 'tkit-memory-performer-xl',
  packages = find_packages(exclude=['examples']),
  version = '0.0.1.0',
  license='Apache License 2.0 ',
  description = 'Memory performer-XL, a variant of performer-XL that uses linear attention update long term memory',
  author = 'Terry Chan',
  author_email = 'napoler2008@gmail.com',
  url = 'https://github.com/napoler/memory-transformer-xl',
  keywords = ['attention mechanism', 'artificial intelligence', 'transformer', 'deep learning'],
  install_requires=[
      'torch',
      'performer-pytorch>=1.0.10',
      'mogrifier'
  ],
  classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3.6',
  ],
)