## Publishing to PyPI

Requires `twine`

```
rm -rf build dist hot_potato.egg-info/

python setup.py sdist bdist_wheel

twine check dist/*

twine upload dist/*
```