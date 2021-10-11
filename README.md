# dt-range

python datetime generator

## Usage

```shell
$ pip install dt-range
```

## GitHub Actions

- **pychecker**

  python code check (black, flake8, isort, mypy)
  - [Repository](https://github.com/nanato12/pychecker)
  - [Marketplace](https://github.com/marketplace/actions/pychecker)

## design

```python
def dt_range(start, end, **kwargs):
  for hour in range(ceil((end - start) / timedelta(**kwargs))):
        yield start + timedelta(day)
```
