import pytest
import sys

async def test_predict_success(client):
    payload = {"features": [2, 39.5, 16.7, 178.0, 3250.0, 1]}
    response = await client.post("/predict", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "prediction" in data
    assert isinstance(data["prediction"],  int)



@pytest.mark.parametrize("values", [sys.float_info.max, -sys.float_info.max, sys.float_info.min, -sys.float_info.min, float('inf'), float('-inf')])
async def test_predict_overflow_values(client, values):
    payload = {"features": [values, 0., 0., 0., 0., 0.]}
    response = await client.post("/predict", json=payload)

    assert response.status_code == 422


@pytest.mark.parametrize("features", [[], [None, None, None, None, None, None], None, ["string", 39.5, 16.7], [2, 39.5, "invalid", 178.0, 3250.0, 1], [2, 39.5, 16.7, 178.0], ])
async def test_predict_invalid_values(client, features):
    payload = {"features": features}

    response = await client.post("/predict", json=payload)

    assert response.status_code == 422


@pytest.mark.parametrize("keys", ["not_features", "feature_list", "input_data", "data"])
async def test_predict_invalid_keys(client, keys):
    payload = {keys: [2, 39.5, 16.7, 178.0, 3250.0, 1]}

    response = await client.post("/predict", json=payload)

    assert response.status_code == 422