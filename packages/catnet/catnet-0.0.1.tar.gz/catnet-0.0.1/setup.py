import os

from setuptools import find_packages, setup


def get_version():
    version_file = os.path.join('catnet', '__init__.py')
    with open(version_file, encoding='utf-8') as f:
        exec(f.read().strip())
    return locals()['__version__']


def get_readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content


setup(
    name='catnet',
    version=get_version(),
    author='Ye Liu',
    author_email='yeliudev@outlook.com',
    license='GPLv3',
    url='https://github.com/yeliudev/CATNet',
    description='Context Aggregation Network',
    long_description=get_readme(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering',
    ],
    python_requires='>=3.8',
    packages=find_packages())
