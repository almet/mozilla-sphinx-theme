from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    zip_safe=False,
    install_requires=["sphinx>=1.1"],
    name="mozilla-sphinx-theme",
    version=0.2,
    author="Alexis Metaireau",
    author_email="alexis@notmyidea.org",
    description="A theme using the default mozilla design guidelines",
    long_description=long_description,
    license="BSD",
    packages=("mozilla_sphinx_theme",),
    include_package_data=True,
    keywords="sphinx extension theme",
    url="https://github.com/ametaireau/mozilla-sphinx-theme/",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ]
)
