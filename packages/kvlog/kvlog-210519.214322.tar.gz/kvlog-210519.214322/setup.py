import time
from distutils.core import setup


setup(version=time.strftime('%y%m%d.%H%M%S'),
      name='kvlog',
      module=['kvlog'],
      description='Strongly consistent replicated log, '
                  'using Paxos for consensus and SQLite for storage, '
                  'to be used as a Queue or a Key Value Store with '
                  'Compare-and-Swap capability on a key',
      author='Bhupendra Singh',
      author_email='bhsingh@gmail.com',
      url='https://github.com/magicray/kvlog')

# python3 setup.py sdist upload
