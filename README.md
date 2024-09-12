# Poetry demo

Create a new project

```sh
poetry new --src poetry-demo
poetry-demo
├── pyproject.toml
├── README.md
├── src
│   └── poetry_demo
│       └── __init__.py
└── tests
    └── __init__.py
```

To add packages to poetry

```sh
poetry add fastapi uvicorn

# in a group
poetry add pytest --group test
```

To run server

```sh
# poetry_demo.main:app project_folder.entry_app_file:fastapi_variable_app
poetry run uvicorn poetry_demo.main:app --port 8080 --reload
```

