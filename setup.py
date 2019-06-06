from setuptools import setup, find_packages

setup(
	name='event',
	description='Restful Api.',
	version='0.0.1-dev',
	install_requires=(
		'Flask',
		'Flask-SQLAlchemy',
		'Flask-Migrate',
		'Flask-Script',
		'Flask-WTF',
		'Flask-Mail',
		'flask-cors',
		'pyjwt',
		'passlib',
		'blinker',
		'celery[redis]',
		'redis',
		'pymysql',
	),
	packages=find_packages(),
	license='MIT',
	zip_safe=False,
	test_suite='nose.collector',
    tests_require=['nose'],
)
