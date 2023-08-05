import pathlib
from setuptools import find_packages, setup

Here = pathlib.Path(__file__).parent

README = (Here / "README.md").read_text()

setup(
    name='Script Scheduler',
    packages=find_packages(include=['scriptScheduler']),
    version='0.2.0',
    description='Schedule Scripts For Running With Time Interval',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Bramhesh Kumar Srivastava',
    license='MIT',
    install_requires=['shortuuid', 'pino', 'os', 'time', 're', 'subprocess', 'threading', 'datetime'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    classifiers = [
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]
)