# Puppyplace Products API

This project uses:
- Python 3.9
- Poetry
- Django
- Django Rest Framework
- MS SQL Server


## How to install

1. Create a virtual environment:
```shell
python -m venv .venv
```

2. Active the virtual environment:
```shell
source .venv/bin/activate
```

3. Install the dependencies:
```shell
make install-deps
```

4. Add MS SQL Server
```shell
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=Docker10#" -p 1433:1433 --name sqlserver -h sqlserver -d mcr.microsoft.com/mssql/server:2019-latest
```
Connect to the database `master` and create the `PUPPYPLACEDB`

Copy the file `local.env` to `.env` file

5. Run
```
make run
```
