from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='axyloop',
    version='1.0',
    description='Makes infinite for loops in python much easier, faster and cleaner',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='http://axy-youtube.tk',
    author='IAmAxY',
    author_email='iamaxydev@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='forloop',
    packages=find_packages(),
    install_requires=['']
)