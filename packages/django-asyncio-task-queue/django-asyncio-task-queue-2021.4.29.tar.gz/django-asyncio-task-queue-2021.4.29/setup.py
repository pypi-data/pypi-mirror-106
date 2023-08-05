import setuptools

setuptools.setup(
    name='django-asyncio-task-queue',
    version='2021.4.29',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
