from fastapi import FastAPI
from fastapi.testclient import TestClient

from applications.routes import guard_rails_routes


def _build_app():
    app = FastAPI()
    app.include_router(guard_rails_routes.router)
    return app


def test_validate_input_returns_200():
    client = TestClient(_build_app())

    response = client.post("/validate-input", json={"message": "What is your experience?"})

    assert response.status_code == 200
    assert response.json()["allowed"] is True


def test_validate_input_returns_422_for_missing_message():
    client = TestClient(_build_app())

    response = client.post("/validate-input", json={})

    assert response.status_code == 422


def test_validate_output_returns_200():
    client = TestClient(_build_app())

    response = client.post(
        "/validate-output",
        json={"output": "some answer", "source_context": "some answer context"},
    )

    assert response.status_code == 200
    assert "is_grounded" in response.json()


def test_validate_output_returns_422_for_missing_fields():
    client = TestClient(_build_app())

    response = client.post("/validate-output", json={})

    assert response.status_code == 422
