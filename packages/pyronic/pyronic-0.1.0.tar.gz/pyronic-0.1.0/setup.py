import os
from setuptools import setup

def read_project_file(path):
    proj_dir = os.path.dirname(__file__)
    path = os.path.join(proj_dir, path)
    with open(path, 'r') as f:
        return f.read()

setup(
    name = 'pyronic',
    version = '0.1.0',
    description = 'Suppress command output on success',
    long_description = read_project_file('README.md'),
    long_description_content_type = 'text/markdown',
    author = 'Jonathon Reinhart',
    author_email = 'Jonathon.Reinhart@gmail.com',
    url = 'https://github.com/JonathonReinhart/pyronic',
    python_requires = '>=3.4.0',
    license = 'MIT',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
    ],
    scripts=['pyronic'],
)
