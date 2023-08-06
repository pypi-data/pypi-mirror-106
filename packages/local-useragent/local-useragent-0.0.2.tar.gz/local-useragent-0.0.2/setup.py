from setuptools import setup

setup(
    name='local-useragent',
    version='0.0.2',
    packages=['local_useragent'],
    url='https://github.com/g1im2/fake_useragent_local',
    project_urls={
        'Bug Tracker': 'https://github.com/g1im2/fake_useragent_local/issues'
    },
    license='MIT',
    author='fxf',
    author_email='fxfpro@163.com',
    description='fake_useragent use local data',
    install_requires=[
        'fake_useragent'
    ],
)
