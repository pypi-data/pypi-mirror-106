your_module_package/
├── your_module
    - sub_module
        - __init__.py
    - python_file1.py
    - python_file2.py
    - __init__.py
- setup.py
- README.md
- LICENSE


<!-- Run Build -->
- python3 setup.py sdist bdist_wheel

<!-- Upload to PyPi -->
- twine upload dist/*