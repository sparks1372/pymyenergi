import pytest
from pymyenergi.client import MyenergiClient
from pymyenergi.eddi import Eddi
from pymyenergi.harvi import Harvi
from pymyenergi.zappi import Zappi

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio

conn = {}


async def test_init(bypass_client_fetch_data):
    client = MyenergiClient(conn)
    await client.refresh()
    assert len(client.devices) == 0


async def test_init_error(error_on_client_fetch_data):
    client = MyenergiClient(conn)
    with pytest.raises(Exception):
        assert await client.refresh()


async def test_get_all_devices(client_fetch_data_fixture):
    client = MyenergiClient(conn)
    devices = await client.get_devices()
    assert len(devices) == 5


async def test_get_eddi_devices(client_fetch_data_fixture):
    client = MyenergiClient(conn)
    devices = await client.get_devices("eddi")
    assert len(devices) == 1
    assert isinstance(devices[0], Eddi)


async def test_get_zappi_devices(client_fetch_data_fixture):
    client = MyenergiClient(conn)
    devices = await client.get_devices("zappi")
    assert len(devices) == 2
    assert isinstance(devices[1], Zappi)


async def test_get_harvi_devices(client_fetch_data_fixture):
    client = MyenergiClient(conn)
    devices = await client.get_devices("harvi")
    assert len(devices) == 2
    assert isinstance(devices[1], Harvi)
