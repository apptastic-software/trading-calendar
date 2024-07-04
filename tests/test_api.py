from fastapi.testclient import TestClient
from trading_calendar.main import app

client = TestClient(app)

def test_markets_all():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets")
        assert response.status_code == 200
        assert len(response.json()) == 56

def test_markets_one_mic():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets?mic=XNYS")
        assert response.status_code == 200
        assert len(response.json()) == 1

def test_markets_multiple_mics():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets?mic=XLON,XETR,XSTO,XSWX,XMAD")
        assert response.status_code == 200
        assert len(response.json()) == 5

def test_markets_bad_mic():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets?mic=ABCD")
        assert response.status_code == 422

def test_status_all():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets/status")
        assert response.status_code == 200
        print(response.json())
        assert len(response.json()) == 56

def test_status_one_mic():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets/status?mic=XNYS")
        assert response.status_code == 200
        assert len(response.json()) == 1

def test_status_multiple_mics():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets/status?mic=XLON,XETR,XSTO,XSWX,XMAD")
        assert response.status_code == 200
        assert len(response.json()) == 5

def test_status_bad_mic():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets/status?mic=ABCD")
        assert response.status_code == 422

def test_hours_all():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets/hours?start=2024-07-03&end=2024-07-03")
        assert response.status_code == 200
        assert len(response.json()) == 56

def test_hours_one_mic():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets/hours?mic=XNYS&start=2024-07-03&end=2024-07-05")
        assert response.status_code == 200
        assert len(response.json()) == 2

def test_hours_bad_mic():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets/hours?mic=ABCD&start=2024-07-03&end=2024-07-05")
        assert response.status_code == 422

def test_hours_bad_start_date():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets/hours?mic=XNYS&start=2024-06-50&end=2024-07-05")
        assert response.status_code == 422

def test_hours_bad_end_date():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets/hours?mic=XNYS&start=2024-07-03&end=2024-07-50")
        assert response.status_code == 422

def test_hours_start_date_after_end_date():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets/hours?mic=XNYS&start=2024-07-05&end=2024-07-03")
        assert response.status_code == 422

def test_holidays_all():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets/holidays?start=2024-07-05&end=2024-07-05")
        assert response.status_code == 200
        assert len(response.json()) == 1

def test_holidays_all_no_holiday():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets/holidays?start=2024-07-02&end=2024-07-02")
        assert response.status_code == 200
        assert len(response.json()) == 0    

def test_holidays_one_mic():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets/holidays?mic=XNYS&start=2024-07-03&end=2024-07-03")
        assert response.status_code == 200
        assert len(response.json()) == 1

def test_holidays_multiple_mics():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets/holidays?mic=XLON,XETR,XSTO,XSWX,XMAD&start=2024-06-06&end=2024-06-21")
        assert response.status_code == 200
        assert len(response.json()) == 2

def test_holidays_bad_mic():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets/holidays?mic=ABCD&start=2024-07-03&end=2024-07-03")
        assert response.status_code == 422

def test_holidays_bad_start_date():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets/holidays?mic=XNYS&start=2024-06-50&end=2024-07-03")
        assert response.status_code == 422

def test_holidays_bad_end_date():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets/holidays?mic=XNYS&start=2024-07-03&end=2024-07-50")
        assert response.status_code == 422

def test_holidays_start_date_after_end_date():
    with TestClient(app) as client:
        response = client.get("/api/v1/markets/holidays?mic=XNYS&start=2024-07-04&end=2024-07-03")
        assert response.status_code == 422
