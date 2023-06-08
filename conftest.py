import pytest
import time
from datetime import datetime

@pytest.fixture(scope='class')
def start_end_time():
    print(f'\nStart time: {datetime.now().time()}')
    yield
    print(f'\nEnd time: {datetime.now().time()}')


@pytest.fixture
def duration():
    start_time = time.time()
    yield
    end_time = time.time()
    print('\nDuration: {} seconds'.format(end_time - start_time))
