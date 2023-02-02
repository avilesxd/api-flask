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

# How to run application?

### Steps:

1. Create a virtual environment

- windows

```bash
python3 -m venv <name_of_virtualenv>
```

- linux

```bash
python3 -m venv <name_of_virtualenv>
```

2. Activate the virtual environment

- windows

```bash
.\env\Scripts\activate
```

- linux

```bash
source /venv/bin/activate
```

3. Install requirements.txt

```bash
pip install -r requirements.txt
```

4. Run app.py file

- windows

```bash
python .\src\app.py
```

- linux

```bash
python3 ./src/app.py
```

# Routes

The available endpoints are:

- GET `/games` : Returns a list with all games
- GET `/games/<id>` : Returns all the information about a specific game
- GET `/companies` : Returns a list with all companies
- GET `/companies/<id>` : Returns all the information about a specific company
- GET `/photos` : Returns a list with all photos

## Author

- Ignacio Avilés ([@avilesxd](https://www.instagram.com/avilesxd/))

## Contributing

See the [contributing guide](https://github.com/avilesxd/api-flask/blob/main/CONTRIBUTING.md) to learn how to contribute to the repository and the development workflow.

## Security

If you believe you have found a security vulnerability, we encourage you to responsibly disclose this and not open a public issue. We will investigate all legitimate reports. Email `nacho72001@gmail.com` to disclose any security vulnerabilities.

## License

[MIT](https://github.com/avilesxd/api-flask/blob/main/LICENSE) by Ignacio Avilés
