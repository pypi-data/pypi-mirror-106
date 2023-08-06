from distutils.core import setup
setup(
  name = 'pysrt2txt',
  packages = ['pysrt2txt'],
  version = '0.1',
  license='MIT',
  description = 'Python library to read subtitles file and extract the text',
  author = 'Bharath and Yadunandan',
  author_email = 'bharath.ts91@gmail.com, yadunandanlh64@gmail.com',
  url = 'https://github.com/bharath-ts/pysrt2txt.git',
  download_url = 'https://github.com/bharath-ts/pysrt2txt/archive/refs/tags/v1.0.0.tar.gz',
  keywords = ['MOVIE', 'SRT', 'SUBTITLE', 'TEXT CONVERSION'],
  install_requires=[
          're2'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    ],
)