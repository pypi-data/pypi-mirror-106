from distutils.core import setup

setup(
    name = 'el_logging',
    packages = ['el_logging'],
    version = '0.1.7',
    license='MIT',
    description = 'Loguru based custom logging package for most python projects.',
    author = 'Batkhuu Byambajav',
    author_email = 'batkhuu@ellexi.com',
    url = 'https://bitbucket.org/ellexiinc/el_logging/',
    download_url = 'https://bitbucket.org/ellexiinc/el_logging/get/0.1.7.tar.gz',
    keywords = ['logging', 'loguru', 'custom'],
    install_requires = [
            'python-dotenv>=0.17.1',
            'loguru>=0.5.3'
        ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
