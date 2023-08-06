import pytest
import asyncio
import logging
from httpx import AsyncClient
from task_manager.common_api.Api import CommonApi, APIv1
from task_manager.common_api.Api.auth_controller.dataclases import AuthResponse, RefreshTokenResponse, NewPasswordRequest


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
@pytest.mark.asyncio
async def test_auth():
    async with AsyncClient(app=CommonApi, base_url="http://test") as ac:
        response = await ac.post(APIv1+"/auth", json={
            "email": "test@test.ru",
            "passwordHash": "test"
        })
    assert response.status_code == 200
    auth_resp = AuthResponse.parse_obj(response.json())

    yield auth_resp
    access_token = auth_resp.credentionals.accessToken
    async with AsyncClient(app=CommonApi, base_url="http://test") as ac:
        response = await ac.post(APIv1+"/logout", headers={
            "Authorization": f"Bearer {access_token}"
        })
    assert response.status_code == 200
    assert response.json() == {"status":0}

    

@pytest.mark.asyncio
async def test_refresh(test_auth: AuthResponse):
    refresh_token = test_auth.credentionals.refreshToken
    async with AsyncClient(app=CommonApi, base_url="http://test") as ac:
        response = await ac.post(APIv1+"/refresh", headers={
            "Authorization": f"Bearer {refresh_token}"
        })
    assert response.status_code == 200
    RefreshTokenResponse.parse_obj(response.json())

@pytest.mark.asyncio
async def test_check_token(test_auth: AuthResponse):
    access_token = test_auth.credentionals.accessToken
    async with AsyncClient(app=CommonApi, base_url="http://test") as ac:
        response = await ac.get(APIv1+"/check-token", headers={
            "Authorization": f"Bearer {access_token}"
        })
    assert response.status_code == 200
    assert response.json() == {"status":0}


@pytest.mark.asyncio
class TestUserInfo:
    async def test_user_info_1(self,test_auth: AuthResponse):
        uuid = test_auth.user.id
        access_token = test_auth.credentionals.accessToken
        async with AsyncClient(app=CommonApi, base_url="http://test") as ac:
            response = await ac.get(APIv1+f"/user/{uuid}", headers={
                "Authorization": f"Bearer {access_token}"
            })
        assert response.status_code == 200

    async def test_user_info_2(self,test_auth: AuthResponse):
        uuid = test_auth.user.id
        async with AsyncClient(app=CommonApi, base_url="http://test") as ac:
            response = await ac.get(APIv1+f"/user/{uuid}")
        assert response.status_code == 401


@pytest.mark.asyncio
async def test_change_password(test_auth: AuthResponse):
    access_token = test_auth.credentionals.accessToken
    async with AsyncClient(app=CommonApi, base_url="http://test") as ac:
        response = await ac.put(APIv1+"/user/change-password",json={
            "passwordHashOld": "test",
            "passwordHashNew": "test1",
        }, headers={
             "Authorization": f"Bearer {access_token}"
        })
    assert response.status_code == 200
    logging.info("Поменяли пароль")


    async with AsyncClient(app=CommonApi, base_url="http://test") as ac:
        response = await ac.put(APIv1+"/user/change-password", json={
            "passwordHashOld": "test1",
            "passwordHashNew": "test",
        }, headers={
             "Authorization": f"Bearer {access_token}"
        })
    assert response.status_code == 200
    logging.info("Вернули пароль обратно")


@pytest.mark.asyncio
class TestUpdateUser:
    async def test_update_user_1(self, test_auth: AuthResponse):
        access_token = test_auth.credentionals.accessToken
        async with AsyncClient(app=CommonApi, base_url="http://test") as ac:
            response = await ac.put(APIv1+"/user/update", json={
                "name": "test",
                "surname": "test",
                "email": "test@test.ru",
                "about": "test",
                "telegram": "test",
                "phone": "test",
                "skype": "test",
                "slack": "test"
            }, headers={
                "Authorization": f"Bearer {access_token}"
            })
        assert response.status_code == 200

    async def test_update_user_2(self, test_auth: AuthResponse):
        access_token = test_auth.credentionals.accessToken
        async with AsyncClient(app=CommonApi, base_url="http://test") as ac:
            response = await ac.put(APIv1+"/user/update", json={
                "name": "test",
                "surname": "test",
                "email": "test",
                "about": "test",
                "telegram": "test",
                "phone": "test",
                "skype": "test",
                "slack": "test"
            }, headers={
                "Authorization": f"Bearer {access_token}"
            })
        assert response.status_code == 400

