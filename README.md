# postgrespython

Description. 
The package postgrespython is used to:
	- execute query in postgres

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package_name

```bash
pip install -i https://test.pypi.org/simple/ postgrespython==0.0.2
```

## Usage

```python
from postgrespython.connection import PyPostgres

db = PyPostgres(host='localhost',database='postgres',user='postgres',password='postgres')
result = db.executarSelect("SELECT * FROM TABLE_A")
```

## Author
Matheus Guanaz
