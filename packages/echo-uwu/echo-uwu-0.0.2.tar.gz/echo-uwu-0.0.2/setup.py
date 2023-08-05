from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='echo-uwu',
    version='0.0.2',
    description='Echo UwU',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Fabio Grimaldi',
    author_email='fabio@fabiogrimaldi.dev',
    license='MIT',
    classifiers=classifiers,
    keywords='echo',
    packages=find_packages(),
    install_requires=['']
)