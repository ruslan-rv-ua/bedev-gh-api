# bedev-gh-api

Very simple github API "proxy" 😊.

- built with modern `FastAPI` framework
- fully asynchronous
- data validation
- API documentation, including OpenAPI schema

## Install it

1. Clone the repo

    ```console
    git clone https://github.com/ruslan-rv-ua/bedev-gh-api
    cd bedev-gh-api
    ```
1. Install deps

    Using poetry (recomended):

    ```console
    poetry install
    ```

    Or with pip:
   
    ```console
    pip install -r requirements.txt
    ```

1. To create issues you need GitHub token.

    Set it with environment variable:

    ```console
    export GITHUB_TOKEN="your token"
    ```

    Or create `.env` file in project's root dir with folloing content:

    ```
    GITHUB_TOKEN="your token"
    ```

## Run it

```console
uvicorn app.main:app
```

## Try it

Open documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Press `Try it out` button under every endpoint and play with it!
