import os

from setuptools import find_packages, setup

# Declare your non-python data files:
# Files underneath configuration/ will be copied into the build preserving the
# subdirectory structure if they exist.
data_files = []
for root, dirs, files in os.walk("configuration"):
    data_files.append(
        (os.path.relpath(root, "configuration"), [os.path.join(root, f) for f in files])
    )

setup(
    name="aws-glue-sessions",
    version="0.4",
    url="",
    author="",
    author_email="",
    # declare your packages
    packages=find_packages(where="src", exclude=("test",)),
    package_dir={"": "src"},
    package_data={'': ['*.json','*.sh']},
    # include data files
    data_files=data_files,
    entry_points="""
        [console_scripts]
        install-glue-kernels = aws_glue_interactive_sessions_kernel.glue_kernel:install
    """,
    # Use the pytest brazilpython runner. Provided by BrazilPython-Pytest.
    test_command="brazilpython_pytest",
    # Use custom sphinx command which adds an index.html that's compatible with
    # code.amazon.com links.
    doc_command="amazon_doc_utils_build_sphinx",
    # Enable build-time format checking
    check_format=True,
    # Enable type checking
    test_mypy=False,
    # Enable linting at build time
    test_flake8=True,
    install_requires=[  'hdijupyterutils>=0.6',
                        'autovizwidget>=0.6',
                        'ipython>=4.0.2',
                        'nose',
                        'requests',
                        'ipykernel>=4.2.2',
                        'ipywidgets>5.0.0',
                        'notebook>=4.2',
                        'tornado>=4',
                        'requests_kerberos>=0.8.0',
                        'boto3',
                        'botocore',
                        'Click'],
)
