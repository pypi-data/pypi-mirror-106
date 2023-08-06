#!/usr/bin/env python3

import argparse
import os.path
import subprocess

import prometheus_client as prometheus

registry = prometheus.CollectorRegistry()

installed_packages = prometheus.Gauge(
    "pacman_installed_packages",
    "The current number of installed packages",
    registry=registry,
)
updateable_packages = prometheus.Gauge(
    "pacman_updateable_packages",
    "The current number of updateable packages",
    registry=registry,
)
explicit_packages = prometheus.Gauge(
    "pacman_explicit_packages",
    "The current number of explicitly installed packages",
    registry=registry,
)
depends_packages = prometheus.Gauge(
    "pacman_depends_packages",
    "The current number of packages installed as dependencies",
    registry=registry,
)
unrequired_packages = prometheus.Gauge(
    "pacman_unrequired_packages",
    "The current number of unrequired packages",
    registry=registry,
)
foreign_packages = prometheus.Gauge(
    "pacman_foreign_packages",
    "The current number of foreign packages",
    registry=registry,
)
native_packages = prometheus.Gauge(
    "pacman_native_packages",
    "The current number of native packages",
    registry=registry,
)
orphan_packages = prometheus.Gauge(
    "pacman_orphan_packages",
    "The current number of orphan packages",
    registry=registry,
)


def pacman_query(options: list[str]) -> int:
    query = ["pacman", "--query"]
    query.extend(options)
    pacman = subprocess.run(query, capture_output=True, encoding="utf-8")
    return len(pacman.stdout.splitlines())


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--textfile-collector-dir",
        action="store",
        default="/var/lib/prometheus/node-exporter",
    )
    args = parser.parse_args()

    installed_packages.set(pacman_query([]))
    updateable_packages.set(pacman_query(["--upgrades"]))
    explicit_packages.set(pacman_query(["--explicit"]))
    depends_packages.set(pacman_query(["--deps"]))
    unrequired_packages.set(pacman_query(["--unrequired"]))
    foreign_packages.set(pacman_query(["--foreign"]))
    native_packages.set(pacman_query(["--native"]))
    orphan_packages.set(pacman_query(["--deps", "--unrequired"]))

    prometheus.write_to_textfile(
        os.path.join(args.textfile_collector_dir, "pacman.prom"), registry
    )


if __name__ == "__main__":
    main()
