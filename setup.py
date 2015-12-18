from distutils.core import setup

setup(
    author = 'Moroz Ilya',
    author_email = 'flamewowilia@gmail.com',
    description = 'Modification of PyAPNs python library for interacting with the Apple Push Notification Service',
    download_url = 'https://github.com/flamewow/PyAPNs.git',
    license = 'unlicense.org',
    name = 'apns_py2py3',
    py_modules = ['apns_py2py3'],
    scripts = ['apns-send'],
    url = 'http://29.io/',
    version = '2.0.1',
)
