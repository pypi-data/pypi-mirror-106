# python-package-example

Install using `pip`
```shell
pip install example-pkg-trdlo
```

Usage example
```python
from example_pkg.pretty_code import Code
from example_pkg.pretty_code import PrettyCode

pretty_code = PrettyCode(6)

code = pretty_code.mirror()   # Code('408804')
pretty_code.half_and_random() # Code('666252')
pretty_code.sequence()        # Code('345678')
pretty_code.two_sequence()    # Code('876321')
pretty_code.simplest()        # Code('444444')
pretty_code.random()          # Code('286183')

print(code.code) # '408804'
print(code.hash) # 'fe5763dbf4013b6b4b984d06e351aef3e54889afe7eebb77afb3267284c5bec9'
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
python3 -m build
python3 -m twine upload --repository pypi dist/*
```
---
## Links

* [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
* [Awesome .gitignore](https://gist.github.com/GhostofGoes/94580e76cd251972b15b4821c8a06f59)

