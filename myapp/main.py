import sys
sys.path.append('C:\\Users\\oleks\\.vscode\\extensions\\algoritmika.algopython-20231012.151548.0\\temp\\orm\\myapp')
from myapp.models import *
admin_role = Role.objects.create(name='admin')
john = User.objects.create(name='John', email='john@example.com', role=admin_role)
