# sparkbar

Creates text version of horizontal bar chart.

## Usage

To generate bars for a list of numbers:

```
>>> import sparkbar
>>> a = [80, 65, 33, 12]
>>> v = sparkbar.sparkbarh(a)
>>> for x in v:
...     print(x)
...
████████
██████▌
███▎
█▎
```

Can also adjust width:

```
>>> v = sparkbar.sparkbarh(a, width=15)
>>> for x in v:
...     print(x)
...
███████████████
████████████▎
██████▎
██▎
```

And add a value label:

```
>>> v = sparkbar.sparkbarh(a, width=15, value_label=True)
>>> for x in v:
...     print(x)
...
███████████████ 80
████████████▎ 65
██████▎ 33
██▎ 12
```

You can also render cells individually (but will need to supply the max value):

```
>>> sparkbar.sparkbarh_cell(44, max_value=88, width=8)
'████'
```

Incase you need alignment horizontal alighmnent you can specify `uniform_width`:

```
>>> v = sparkbar.sparkbarh(a)
>>> print(v)
['████████', '██████▌', '███▎', '█▎']
>>> v = sparkbar.sparkbarh(a, uniform_width=True)
>>> print(v)
['████████', '██████▌ ', '███▎    ', '█▎      ']
```

## Running Tests

From this directory run:
```
pytest
```