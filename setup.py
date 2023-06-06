from setuptools import setup
import platform

install_requires = []

# Install dependencies for Windows
if platform.system() == 'Windows':
    install_requires.append('winsdk')

# Install dependencies for MacOS
if platform.system() == 'Darwin':
    install_requires.append('pyobjc')

setup(
    name='simplenotify',
    version='0.32',
    description='A simple Python library for sending interactive notifications across multiple operating systems.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/julianwhiteco/simplenotify',
    project_urls={'Bug Tracker': 'https://github.com/julianwhiteco/simplenotify/issues'},
    author='Julian White',
    author_email='',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        "Topic :: Utilities",
        'Operating System :: Microsoft',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 11',
        'Operating System :: MacOS',
        'Operating System :: MacOS :: MacOS X'
    ],
    install_requires=install_requires,
    py_modules=['simplenotify']
)
