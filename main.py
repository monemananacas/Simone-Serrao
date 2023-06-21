from src.models.store import Store
from src.models.user import User
from src.service.service_user import ServiceUser

store = Store()

name_1 = "Simone"
job_1 = "Qa"

user = User(name=name_1, job=job_1)


print("#primeiro Teste")
name_1 = 'simone'
job_1 = "Qa"


service = ServiceUser()
resultado = service.add_user(name=name_1, job=job_1)
print(service.store.bd[0].name)
print(service.store.bd[0].job)
print(resultado)

print("#Segundo Teste")
name_1 = None
job_1 = "Qa"

service = ServiceUser()
resultado = service.add_user(name=name_1, job=job_1)
print(service.store.bd)
print(resultado)


