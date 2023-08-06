from setuptools import setup,find_packages
setup(
    name='cylinderize',
    version='1.0.0',
    description='Turn any file into a cylinder',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['Pillow==8.2.0', 'matplotlib==3.4.2', 'numpy==1.20.3'],
    url='https://github.com/donno2048/cylinderize',
    packages=find_packages(),
    license='MIT',
    author='Elisha Hollander',
    classifiers=['Programming Language :: Python :: 3'],
    entry_points={ 'console_scripts': [ 'cylinderize=cylinderize.__main__:main' ] }
)