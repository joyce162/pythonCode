import pytest

if __name__ == '__main__':
     # pytest.main(['-vs','./testcase','-m','smoke'])

    pytest.main(['-vs', './testcase/Login/test_login.py'])
    # pytest.main()