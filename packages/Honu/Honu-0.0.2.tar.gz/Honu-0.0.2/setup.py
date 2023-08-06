from setuptools import setup, find_packages

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
# Also used to specify package_data
setup(
    name="Honu",
    install_requires=[
    ],
    extras_require={
    },
    package_data={
        # Used to include the default levels
        "": ["*.json", "*.png"],
    },
    # entry_points={
    #     'console_scripts': ['honutest=honu.cli.honu_test:main'],
    # }
)
