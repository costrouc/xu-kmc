from setuptools import setup, find_packages


setup(
    name='kmc',
    version='0.0.1',
    packages=find_packages(),
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov'],
    install_requires=['numpy'],  # requires hoomd as well
    license='Unlicense',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
