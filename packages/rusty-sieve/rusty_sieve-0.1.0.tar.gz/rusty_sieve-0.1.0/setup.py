import sys

from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="rusty_sieve",
    version="0.1.0",
    rust_extensions=[RustExtension("rusty_sieve.rusty_sieve", binding=Binding.RustCPython)],
    packages=["rusty_sieve"],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
    long_description="Prime Sieve of Eratosthenes implemented in Rust",
    long_description_content_type="text/x-rst"
)