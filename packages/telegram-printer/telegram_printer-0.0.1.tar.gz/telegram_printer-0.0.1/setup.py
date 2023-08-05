from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='telegram_printer',
    version='0.0.1',
    description='Send the telegram message & print at the same time',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.TXT').read(),
    url='',
    author='TheBlackHero55',
    author_email='theblackhero2@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='telegram, print, tg, printer, prints, bold, underline',
    packages=find_packages(),
    install_requires=['telegram_send']
)
