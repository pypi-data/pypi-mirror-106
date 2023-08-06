from setuptools import setup, find_packages

setup(
    name='bilnn',
    version='0.0.2',
    description='A SDK For Bilnn Pan',
    py_modules=["bilnn"],

    long_description="A SDK for Bilnn Pan, made by Yixiangzhilv.",
    url='https://github.com/Danny-Yxzl/bilnn-python-sdk',
    author='Yixiangzhilv',
    author_email='mail@yixiangzhilv.com',
    classifiers=[

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    keywords='netdisk sdk',
    install_requires=['requests', 'urllib3', 'xmltodict'],
    project_urls={
        'Bug Reports': 'https://github.com/Danny-Yxzl/bilnn-python-sdk/issues',
        'Say Thanks!': 'https://www.yixiangzhilv.com/',
        'Source': 'https://github.com/Danny-Yxzl/bilnn-python-sdk',
    }
)
