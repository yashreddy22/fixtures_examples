#Example 1
import pytest

@pytest.fixture
def value():
	num=20
	return num

def test_add(add):
	assert num==20


#Example 2
import pytest

@pytest.fixture
def user():
	return{
		"username":"yaswanth nikhil",
		"email":"yaswanth@gmail.com",
		"age":23
	{

def test_user_name(user):
	assert user["username"]=="yaswanth nikhil"

def test_user_mail(user):
	assert user["email"]=="yaswanth@gmail.com"

def test_user_age(user):
	assert user["age"]==23


