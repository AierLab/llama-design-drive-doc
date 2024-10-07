# install and run

```bash
uv install

# execute at anywhere
start-server
```

# Run all tests
> Currently running on Python3.10

```bash
cd backend

python3.10 -m pytest -v
```

# Run individual test scripts
## Example: API functional tests

```bash
cd backend/tests/functional

pytest functional_api_test.py
```
