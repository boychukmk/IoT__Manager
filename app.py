import logging
from aiohttp import web
from models import Device, initialize_db

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def setup_db(app):
    """
    Initialize the database.
    """
    initialize_db()

async def create_device(request):
    """
    Create a new device.
    """
    try:
        data = await request.json()
        required_fields = ['name', 'type', 'login', 'password', 'location_id', 'api_user_id']
        if not all(field in data for field in required_fields):
            return web.json_response({'error': 'Missing fields'}, status=400)

        device = Device.create(
            name=data['name'],
            type=data['type'],
            login=data['login'],
            password=data['password'],
            location=data['location_id'],
            api_user=data['api_user_id']
        )
        logger.info(f"Device created with ID {device.id}")
        return web.json_response({'id': device.id}, status=201)
    except Exception as e:
        logger.error(f"Error creating device: {e}")
        return web.json_response({'error': str(e)}, status=500)

async def get_device(request):
    """
    Retrieve a device by ID.
    """
    device_id = request.match_info.get('id')
    try:
        device = Device.get(Device.id == device_id)
        return web.json_response({
            'name': device.name,
            'type': device.type,
            'login': device.login,
            'password': device.password,
            'location_id': device.location.id,
            'api_user_id': device.api_user.id
        })
    except Device.DoesNotExist:
        return web.json_response({'error': 'Device not found'}, status=404)
    except Exception as e:
        logger.error(f"Error retrieving device: {e}")
        return web.json_response({'error': str(e)}, status=500)

async def update_device(request):
    """
    Update an existing device.
    """
    device_id = request.match_info.get('id')
    try:
        data = await request.json()
        required_fields = ['name', 'type', 'login', 'password', 'location_id', 'api_user_id']
        if not all(field in data for field in required_fields):
            return web.json_response({'error': 'Missing fields'}, status=400)

        Device.update(
            name=data['name'],
            type=data['type'],
            login=data['login'],
            password=data['password'],
            location=data['location_id'],
            api_user=data['api_user_id']
        ).where(Device.id == device_id).execute()
        logger.info(f"Device with ID {device_id} updated")
        return web.Response(text='Device updated', status=200)
    except Device.DoesNotExist:
        return web.json_response({'error': 'Device not found'}, status=404)
    except Exception as e:
        logger.error(f"Error updating device: {e}")
        return web.json_response({'error': str(e)}, status=500)

async def delete_device(request):
    """
    Delete a device by ID.
    """
    device_id = request.match_info.get('id')
    try:
        query = Device.delete().where(Device.id == device_id)
        if query.execute() == 0:
            return web.json_response({'error': 'Device not found'}, status=404)
        logger.info(f"Device with ID {device_id} deleted")
        return web.Response(text='Device deleted', status=200)
    except Exception as e:
        logger.error(f"Error deleting device: {e}")
        return web.json_response({'error': str(e)}, status=500)

app = web.Application()
app.router.add_post('/devices', create_device)
app.router.add_get('/devices/{id}', get_device)
app.router.add_put('/devices/{id}', update_device)
app.router.add_delete('/devices/{id}', delete_device)

if __name__ == '__main__':
    app.on_startup.append(setup_db)
    web.run_app(app, host='127.0.0.1', port=8000)
