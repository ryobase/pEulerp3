import setuptools

setuptools.setup(
    name="ppp",
    version="0.1.0",
    url="https://github.com/borntyping/cookiecutter-pypackage-minimal",

    author="Moss Pakhapoca",
    author_email="thorsleepless@gmail.com",

    description="Project Euler solutions in Python 3",

    license="MIT",

    packages=setuptools.find_packages(),

    install_requires=[
        "Click"
    ],

    # entry_points={
    #     "console_scripts": [
    #         "euler = euler.cli:main"
    #     ]
    # },

    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
