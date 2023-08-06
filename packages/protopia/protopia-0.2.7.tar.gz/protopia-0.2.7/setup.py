from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name             = 'protopia',
    version          = '0.2.7',
    description      = 'Python agent for protopia',
    author           = 'Alan Synn',
    author_email     = 'alan@protopia.ai',
    url              = 'https://github.com/protopia-ai/py-agent',
    download_url     = 'https://github.com/protopia-ai/py-agent/archive/0.2.1.tar.gz',
    install_requires = [
        'grpcio>=1.34.1',
        'grpcio-tools>=1.34.1',
        'oauthlib>=3.1.0',
        'requests-oauthlib>=1.3.0',
        'torch>=1.0.0'
    ],
    packages         = find_packages(exclude = ['docs', 'tests*']),
    keywords         = ['protopia', 'protopia-agent'],
    python_requires  = '>=3',
    package_data     =  {
    },
    long_description=long_description,
    long_description_content_type='text/markdown',
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)