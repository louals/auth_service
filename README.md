# auth_service

> Authentication microservice that manages signup and login. Provides secure auth endpoints with JWT token handling and OAuth2 support.



## Overview

Authentication microservice that manages signup and login. Provides secure auth endpoints with JWT token handling and OAuth2 support.

## Tech Stack

Python, FastAPI, JWT, OAuth2

## Features

- User signup and login
- JWT access token issuing and validation
- OAuth2 password flow support

## Getting Started

### Prerequisites

Make sure you have the tools required for this stack installed (e.g. Python 3.10+, Node.js 18+, or Android Studio).

### Installation & Usage

```bash
git clone https://github.com/<your-username>/auth_service.git
cd auth_service
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
Interactive API docs: http://localhost:8000/docs
> Adjust `main:app` if your entry module is named differently.

## Configuration

Set `SECRET_KEY` and token expiry values in a `.env` file.

## Contributing

Contributions are welcome. Fork the repo, create a feature branch, and open a pull request.

## License

Distributed under the MIT License (change as needed).

## Author

**Louai**: [GitHub](https://github.com/<louals>)
