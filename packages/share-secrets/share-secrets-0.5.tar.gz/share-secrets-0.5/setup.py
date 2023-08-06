import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="share-secrets",
    version="0.5",
    author="Anish M",
    author_email="aneesh25861@gmail.com",
    description="share secrets with ease.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3",
    keywords = ['Secret sharing', 'cryptography','student project'],
    url="https://github.com/Anish-M-code/share_secrets",
    packages=["share_secrets"],
    classifiers=(
        'Development Status :: 5 - Production/Stable',      
        'Intended Audience :: Developers',      
        'Topic :: Software Development',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',   
        'Programming Language :: Python :: 3',      
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Topic :: Security :: Cryptography',
  
    ),
    entry_points={"console_scripts": ["share-secrets = share_secrets:main",],},
)
