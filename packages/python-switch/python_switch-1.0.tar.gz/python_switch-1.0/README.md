# Python Switch Like JavaScript Switch Statement

## Installing

Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/):

```sh
pip install python-switch
```

### A Simple Examples

```Python
from python_switch import Switch

s = Switch({"d":lambda x:f"returns {x} (d)","default":lambda x: f"returns {x} (default)"})

print(s.get("d")(1))
```

Adding a case later.

```Python
from python_switch import Switch

s = Switch({"default":lambda x: f"returns {x} (default)"})

s.addCase("d",lambda x:f"returns {x} (d)")

print(s.get("d")(1))
```

Adding cases with the decorator.

```Python
from python_switch import Switch

s = Switch({"default":lambda x: f"returns {x} (default)"})

@s.case()
def d(x):
 return f"returns {x} (d)"

print(s.get("d")(1))
```
