from allure import step

@step("My test")
def test_something():
    assert 1 == 1

if __name__ == "__main__":
    allure.run("tests", clean=True)
