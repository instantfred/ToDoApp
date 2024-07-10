from .utils import *
from ..routers.users import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
  response = client.get('/user')
  assert response.status_code == status.HTTP_200_OK
  assert response.json()['username'] == 'freddydev'
  assert response.json()['email'] == 'freddy@mail.com'
  assert response.json()['role'] == 'admin'
  assert response.json()['first_name'] == 'Freddy'
  assert response.json()['last_name'] == 'Ramirez'
  assert response.json()['phone_number'] == '123-456-7890'


def test_change_password_success(test_user):
  response = client.put('/user/password', json={'password': 'password', 'new_password': 'new_password'})
  assert response.status_code == status.HTTP_200_OK


def test_change_password_fail(test_user):
  response = client.put('/user/password', json={'password': 'wrong_password', 'new_password': 'new_password'})
  assert response.status_code == status.HTTP_401_UNAUTHORIZED
  assert response.json() == {'detail': 'Error on password change'}


def test_change_phone_number_success(test_user):
  response = client.put('/user/phone_number/9999999999')
  assert response.status_code == status.HTTP_204_NO_CONTENT
