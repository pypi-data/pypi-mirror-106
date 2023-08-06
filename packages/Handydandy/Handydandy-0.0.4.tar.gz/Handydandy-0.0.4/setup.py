from distutils.core import setup
setup(
  name = 'Handydandy',
  packages = ['handydandy'],
  version = '0.0.4',
  license='MIT',
  description = 'easy to use handy python tools', 
  author = 'LucasAmmer',
  author_email = 'lucas@ammer.nl',
  url = 'https://github.com/lucasammer/handydandy', 
  download_url = 'https://github.com/lucasammer/handydandy/archive/refs/tags/0.0.4.tar.gz',
  keywords = ['HANDY', 'EASY', 'SIMPLE'],
  install_requires=[
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)