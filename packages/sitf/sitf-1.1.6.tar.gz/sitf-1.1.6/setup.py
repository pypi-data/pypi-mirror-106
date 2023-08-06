from setuptools import setup, find_packages

setup(
    name='sitf',
    version='1.1.6',
    description="Sort Images by day's wise into to the folders",
    author='Shatak Gurukar',
    author_email='shatakgurukar@gmail.com',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(include=['sitfproject', 'sitfproject.*']),
    license='BSD License',
    entry_points={
        'console_scripts': ['sitf=sitfproject.sitf:main']
    },
    install_requires=[
        'Pillow'        
    ],
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is for
        'Intended Audience :: End Users/Desktop',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='folders files sorter images',
    python_requires='>=3.6'
)