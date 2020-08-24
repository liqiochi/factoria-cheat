# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Factorio_Cheat_GUI_RTM.py'],
             pathex=['C:\\Users\\liqio\\OneDrive\\Codes\\factorio_cheat'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['aiohttp', 'altgraph', 'appdirs', 'asgiref', 'astroid', 'async-timeout', 'attrs', 'autopep8', 'backcall', 'beautifulsoup4', 'cchardet', 'certifi', 'cffi', 'chardet', 'click', 'colorama', 'comtypes', 'cycler', 'distutils', 'django', 'filelock', 'flask', 'gevent', 'greenlet', 'hook', 'hooks', 'html5lib', 'idna', 'importlib-metadata', 'ipython', 'ipython-genutils', 'isort', 'jedi', 'kivy', 'kiwisolver', 'lazy-object-proxy', 'lxml', 'macholib', 'matplotlib', 'mccabe', 'mechanize', 'MouseInfo', 'multidict', 'mysql-connector-python', 'numpy', 'odfpy', 'opencv', 'pandas', 'parso', 'pattern', 'pefile', 'Pillow', 'PyAutoGUI', 'pygame', 'pygi', 'pyglet', 'PIL', 'pylint', 'pilkit', 'pillow', 'pipenv', 'pydoc', 'pynput', 'PyQt4', 'PyQt5', 'PyQt5-sip', 'PyQt5-tools', 'pyramid', 'pythoncom', 'pytube', 'pytz', 'pywintypes', 'pyz', 'requests', 'scapy', 'scipy', 'scrapy', 'setuptools', 'site', 'six', 'sklearn', 'sqlite3', 'sympy', 'tensorflow', 'tornado', 'wrapt', 'wxPython', 'xlrd', 'xlwings', 'yarl', 'zipp', 'zope.event'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Factorio_Cheat_GUI_RTM',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
