#!/usr/bin/env python

def main():
	try:
		from setuptools import setup
	except ImportError:
		from distutils.core import setup

	config = {
		'description': 'Helper functions for use with Magellan (py_entitymatching, etc.)',
		'author': 'Matt Christie',
		'download_url': 'https://github.com/christiemj09/magellan_aux.git',
		'author_email': 'christiemj09@gmail.com',
		'version': '0.1',
		# 'install_requires': [],  # Use requirements file instead
		'packages': ['magellan_aux'],
		'scripts': [
		    # 'bin/refresh-funcs',  # Example
		],
		'entry_points': {
		    'console_scripts': [
		        # Generic format; write a function called console_script() in the action module
		        # 'action=garten.action:console_script'
		    ]
		},
		'name': 'magellan_aux'
	}

	setup(**config)	

if __name__ == '__main__':
	main()
