from distutils.core import setup
import py2exe

setup(console=['main.py'],
      packages=['bugsplat', 'certifi', 'cffi', 'chardet', 'charset-normalizer', 'cryptography', 'Deprecated', 'gitdb', 'GitPython', 'idna', 'linecache', 'numpy', 'pandas', 'pathlib', 'Pillow', 'pip', 'pycipher', 'pycparser', 'pycryptodome', 'PyJWT', 'PyNaCl', 'PySimpleGUI', 'python-dateutil', 'pytz', 'random-address', 'requests', 'setuptools', 'six', 'smmap', 'tenacity', 'tk', 'traceback', 'urllib3', 'wget', 'wheel', 'wrapt', 'wxPython', 'log0~=', 'logzero~=', 'pyglet~=']
)
