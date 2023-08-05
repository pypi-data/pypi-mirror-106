import setuptools

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

REQUIRED_PACKAGES = [
    'torch>=1.1.0', 'tqdm', 'sklearn', 'tensorflow'
]

setuptools.setup(
    name="easyrec",
    version="0.1.0_beta",
    author="yinpu",
    author_email="741456392@163.com",
    description="deep learning frame for recommendation algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yinpu/easyrec",
    download_url='https://github.com/yinpu/easyrec/tags',
    packages=setuptools.find_packages(),
    python_requires=">=3.5.*",  # '>=3.4',  # 3.4.6
    install_requires=REQUIRED_PACKAGES,
    extras_require={

    },
    entry_points={
    },
    classifiers=(
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
    license="MIT",
    keywords=['deep learning', 'torch', 'tensor', 'pytorch'],
)
