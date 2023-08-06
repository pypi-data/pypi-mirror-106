from setuptools import setup

setup(
    name='monkey-color',
    version='0.0.2',
    author='monkey',
    author_email='a102009102009@gmail.com',
    url='https://github.com/a3510377/color',
    description=u'有色文字',
    packages=['color'],
    install_requires=[],  # 工具包的依赖包
    entry_points={
        'console_scripts': []
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
