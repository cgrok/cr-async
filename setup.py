from setuptools import setup

setup(
    name='crasync',
    packages=['crasync'],  # this must be the same as the name above
    version='v1.3.0',
    description='An async wrapper for cr-api.com',
    author='verixx',
    license='MIT',
    author_email='abdurraqeeb53@gmail.com',
    url='https://github.com/grokkers/cr-async',  # use the URL to the github repo
    download_url='https://github.com/grokkers/cr-async/archive/v1.3.0.tar.gz',  # I'll explain this in a second
    keywords=['clashroyale'],  # arbitrary keywords
    classifiers=[],
    install_requires=['aiohttp>=2.0.0,<2.3.0'],
    package_data={'crasync':['chests.json']},
    include_package_data=True
)
