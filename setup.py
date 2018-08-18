from setuptools import setup

setup(
    name='WeatherLine',
    description = 'A weather app',
    install_requires=['requests'],

    entry_points={
        'console_scripts': [
            'weather=weatherline:__main__',
        ],
    },
)