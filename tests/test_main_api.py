import pytest
from httpx import AsyncClient
from app.main import app

# pytest.mark.asyncio, bu testin asenkron olduğunu belirtir.
@pytest.mark.asyncio
async def test_read_root():
    """
    Test /api/ endpoint'inin doğru yanıt verip vermediğini kontrol eder.
    """
    # 'async with' ile test istemcisini asenkron olarak oluşturuyoruz.
    # app=app, test edilecek FastAPI uygulamasını belirtir.
    # base_url, test sırasında yapılacak isteklerin tam URL'ini oluşturmak için kullanılır.
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # /api/ endpoint'ine GET isteği gönder
        response = await ac.get("/api/")
    
    # 1. Durum kodunun 200 (OK) olduğunu doğrula
    assert response.status_code == 200
    
    # 2. Dönen JSON yanıtının beklenen içeriğe sahip olduğunu doğrula
    assert response.json() == {"message": "API is running!"}