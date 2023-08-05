# mnemic
A memory tracer application

To upload to cheese:

```
sudo python3 setup.py sdist bdist_wheel
twine upload  --skip-existing dist/* --verbose
```
