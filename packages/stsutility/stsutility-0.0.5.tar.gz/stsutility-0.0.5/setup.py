import setuptools

setuptools.setup(
	name="stsutility",
	version="0.0.5",
	author="636",
	author_email="win.stitch.23@gmail.com",
	description="636 Utility Package",
	url="https://github.com/0187773933/stsutility",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
	setup_requires=['numpy','pandas','Pint'],
	install_requires=[
		'json',
		'pathlib',
		'time',
		'Pint',
		'math',
		'decimal',
		'operator',
		'pandas',
		'numpy',
		'pprint',
	],
)

