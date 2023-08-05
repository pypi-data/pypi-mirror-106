# python-package-example

Install using `pip`
```shell
pip install example-pkg-trdlo
```
---
## Alternative installation method
Install using `git+ssh` URI schema
```shell
pip install git+ssh://git@gitlab.com/avnovoselov/python-package-example.git
```

Install using `https` URI schema
```shell
pip install https://gitlab.com/avnovoselov/python-package-example.git
```
---
# Update build
After run will prompt username and password.
```shell
python3 -m twine upload --repository pypi dist/*
```
---
## Links

* [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
* [Awesome .gitignore](https://gist.github.com/GhostofGoes/94580e76cd251972b15b4821c8a06f59)

