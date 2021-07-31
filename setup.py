import os
from pathlib import Path

from semantic_version import Version
from setuptools import setup, find_packages, Command

from tax_calculator import version


class AbstractHandleVersion(Command):

    def _get_file_version(self) -> str:
        for dirpath, dnames, fnames in os.walk("./"):
            if len(Path(dirpath).parts) == 0:
                # Skip CWD
                continue
            main_directory = str(Path(dirpath).parts[0])
            if main_directory.startswith("."):
                continue
            if any(map(lambda x: main_directory == x, ["venv", "dist", "build", "egg-info"])):
                # ignore big folders
                continue
            for f in fnames:
                if f.endswith("version.py"):
                    return os.path.join(dirpath, f)
        else:
            raise ValueError(f"Cannot detect version file!")

    def _read_version(self, filename: str) -> Version:
        with open(filename, mode="r", encoding="utf8") as f:
            v = f.read()
        v = v.split("=")[1].strip("\"\' \t\n")
        return Version(v)

    def _write_version(self, filename: str, version: Version):
        with open(filename, mode="w", encoding="utf8") as f:
            f.write(f"VERSION = \"{version}\"")


class IncreasePatchVersion(AbstractHandleVersion):
    """
    Allows you to automatically increase version patch number.

    :see https://dankeder.com/posts/adding-custom-commands-to-setup-py/:
    """
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        version_file = self._get_file_version()
        current_version = self._read_version(version_file)
        next_version = current_version.next_patch()
        print(f"version file={version_file} current={current_version} next={next_version}")
        self._write_version(version_file, next_version)
        print(f"done updating version file {version_file}")


class IncreaseMinorVersion(AbstractHandleVersion):
    """
    Allows you to automatically increase version minor number.

    :see https://dankeder.com/posts/adding-custom-commands-to-setup-py/:
    """
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        version_file = self._get_file_version()
        current_version = self._read_version(version_file)
        next_version = current_version.next_minor()
        print(f"version file={version_file} current={current_version} next={next_version}")
        self._write_version(version_file, next_version)
        print(f"done updating version file {version_file}")


class IncreaseMajorVersion(AbstractHandleVersion):
    """
    Allows you to automatically increase version major number.

    :see https://dankeder.com/posts/adding-custom-commands-to-setup-py/:
    """
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        version_file = self._get_file_version()
        current_version = self._read_version(version_file)
        next_version = current_version.next_major()
        print(f"version file={version_file} current={current_version} next={next_version}")
        self._write_version(version_file, next_version)
        print(f"done updating version file {version_file}")


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="tax-calculator",
    version=version.VERSION,
    author="Massimo Bono",
    author_email="massimobono1@gmail.com",
    description="Allows you to compute taxes",
    license="MIT",
    keywords="tax",
    url="https://github.com/Koldar/tax-calculator",
    packages=find_packages(),
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    license_files="LICEN[SC]E*.md",
    # REQUIREMENTS
    python_requires=">=3.6",
    install_requires=[
        "arrow>=1.1.1",
        "beautifulsoup4>=4.9.3",
        "python-dateutil>=2.8.2",
        "requests>=2.26.0",
        "soupsieve>=2.2.1",
        "stringcase>=1.2.0",
        "urllib3>=1.26.6",
        "semantic_version>=2.8.5"
    ],
    # NON PYTHON DATA
    include_package_data=True,
    package_data={
        "": ["package_data/*.*"],
    },
    # CONSOLE SCRIPT
    entry_points={"console_scripts": [f"tax-calculator=tax_calculator.main:main"]},
    # TEST
    test_suite='tax_calculator.tests',
    # CUSTOM COMMANDS
    cmdclass={
        'update_version_patch': IncreasePatchVersion,
        'update_version_minor': IncreaseMinorVersion,
        'update_version_major': IncreaseMajorVersion,
    },
)
