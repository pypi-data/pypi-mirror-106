from setuptools import setup

setup(
    name="prometheus-pacman-exporter",
    description="Export pacman statistics to prometheus",
    version="0.0.3",
    license="GPLv3+",
    author="Dennis Fink",
    author_email="dennis.fink@c3l.lu",
    py_modules=["prometheus_pacman_exporter"],
    platforms="any",
    install_requires=["prometheus-client"],
    entry_points={
        "console_scripts": [
            "prometheus-pacman-exporter=prometheus_pacman_exporter:main"
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Topic :: System :: Monitoring",
    ],
)
