from setuptools import setup

setup(
	name='npdtools',
	version='0.1a1',
	packages=['npdtools', 'npdtools.types', 'npdtools.errors'],
	url='https://gitlab.com/whiteapfel/npdtools',
	license='MPL 2.0',
	author='WhiteApfel',
	author_email='white@pfel.ru',
	description='tool for work with FNS API',
	install_requires=['typing', 'httpx'],
)
