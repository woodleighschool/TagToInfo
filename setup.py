from setuptools import setup

APP = ['main.py']
DATA_FILES = [('assets', ['assets/template.png',
               'assets/Arial.ttf', 'assets/Arial Bold.ttf'])]
OPTIONS = {
    'iconfile': 'assets/icon.icns',
    'plist': {
        'CFBundleName': 'TagToInfo',
        'CFBundleDisplayName': 'TagToInfo',
        'CFBundleIdentifier': 'com.woodleigh.tagtoinfo',
        'CFBundleVersion': '0.1.0',
        'CFBundleShortVersionString': '0.1',
    },
    'packages': ['requests', 'PIL', 'qrcode', 'PyQt5', 'chardet'],
    'includes': ['sys', 'os', 'json'],
}

setup(
    app=APP,
    name='TagToInfo',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)