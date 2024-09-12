# Poetry demo

To add packages to poetry

```sh
poetry add fastapi uvicorn

# in a group
poetry add pytest --group test
```

To run server

```sh
poetry run uvicorn poetry_demo:main --port 8080 --reload
```