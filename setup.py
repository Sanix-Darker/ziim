from distutils.core import setup

setup(
    name='Ziim',  # How you named your package folder (MyLib)
    packages=['ziim'],  # Chose the same as "name"
    version='0.1',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Let your CLI find available solutions for errors / exceptions online on commands you hit, for you, '
                'no need open a Browser. and find something yourself',  # Give a short description about your library
    author='Sanix darker',  # Type in your name
    author_email='s4nixd@gmail.com',  # Type in your E-Mail
    url='https://github.com/sanix-darker/ziim',  # Provide either the link to your github or to your website
    download_url='https://github.com/sanix-darker/ziim/archive/v_01.tar.gz',  # I explain this later on
    keywords=[
        'cli',
        'stackoverflow',
        'stackoverflow-questions',
        'stackoverflow-api',
        'exceptions',
        'exception-handling',
        'exception-handler',
        'error-handling',
        'error-correcting-codes',
        'python',
        'scraper',
        'crawler',
    ],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        'requests',
        'lxml',
        'pytest',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
