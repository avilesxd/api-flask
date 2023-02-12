<p align="center">
  <a href="https://github.com/avilesxd/api-flask">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="src\static\favicon.ico">
      <img src="src\static\favicon.ico" height="128">
    </picture>
    <h1 align="center">API - Flask</h1>
  </a>
</p>

<p align="center">
  <a aria-label="License" href="src\static\license.svg">
    <img alt="" src="https://img.shields.io/badge/License-MIT-blue">
  </a>
  <a aria-label="Contribute" href="https://github.com/avilesxd/api-flask/blob/main/CONTRIBUTING.md">
    <img src="src\static\contribute.svg" alt="contribute svg logo"></img>
  </a>
  <a aria-label="python-version" href="https://www.python.org/">
    <img src="src\static\python.svg" alt="python svg logo"></img>
  </a>
</p>

<div align="center">

[![CodeQL](https://github.com/avilesxd/api-flask/actions/workflows/codeql.yml/badge.svg)](https://github.com/avilesxd/api-flask/actions/workflows/codeql.yml)

</div>

## Run Locally

Clone the project

```bash
  git clone https://github.com/avilesxd/api-flask.git

```

Go to the project directory

```bash
  cd api-flask

```

Create a virtual environment

- Windows

```bash
python3 -m venv <name_of_virtualenv>

```

- Linux

```bash
python3 -m venv <name_of_virtualenv>

```

Activate the virtual environment

- Windows

```bash
.\env\Scripts\activate

```

- Linux

```bash
source /venv/bin/activate

```

Install requirements

```bash
pip install -r requirements.txt

```

- add new dependencies?, use the following command:

```bash
pip freeze > requirements.txt

```

Run app file

- Windows

```bash
python .\src\app.py

```

- Linux

```bash
python3 ./src/app.py

```

## Running Tests

To run tests, run the following command

- Windows

```bash
python .\src\tests\test_routes_api.py

```

- Linux

```bash
python3 ./src/tests/test_routes_api.py

```

- Windows or Linux

```bash
pytest -v

```

## API routes

| Methods | Route             | Description                                          |
| :------ | :---------------- | :--------------------------------------------------- |
| `GET`   | `/games`          | Returns a list with all games                        |
| `GET`   | `/games/<id>`     | Returns all the information about a specific game    |
| `GET`   | `/companies`      | Returns a list with all companies                    |
| `GET`   | `/companies/<id>` | Returns all the information about a specific company |
| `GET`   | `/photos`         | Returns a list with all photos                       |

## Author

- Ignacio Avilés ([@avilesxd](https://www.instagram.com/avilesxd/))

## Contributors

- IgnS27

## Contributing

Contributions are always welcome!

See [contributing.md](https://github.com/avilesxd/api-flask/blob/main/CONTRIBUTING.md) for ways to get started.

Please adhere to this project's [code of conduct](https://github.com/avilesxd/api-flask/blob/main/CODE_OF_CONDUCT.md).

## Security

If you believe you have found a security vulnerability, we encourage you to responsibly disclose this and not open a public issue. We will investigate all legitimate reports. Email `nacho72001@gmail.com` to disclose any security vulnerabilities.

## License

[MIT](https://github.com/avilesxd/api-flask/blob/main/LICENSE) by Ignacio Avilés
