from src.service.service_user import ServiceUser

class TestServiceUser:

 def test_add_user_success(self):
  # Setup
  name_1 = "Fulano"
  job_1 = "DEV"
  resultado_esperado = "Usuário do tipo string foi adicionado com sucesso"
  service = ServiceUser()

  # Chamada
  resultado = service.add_user(name=name_1, job=job_1)

  # Avaliação
  assert resultado_esperado == resultado

 def test_add_user_null(self):
  # Setup
  name_1 = None
  job_1 = "Eng"
  resultado_esperado = "Usuario não adicionado pois é nulo"
  service = ServiceUser()

  # Chamada
  resultado = service.add_user(name=name_1, job=job_1)

  # Avaliação
  assert resultado_esperado == resultado

 def test_add_user_invalid(self):
   # Setup
   name_1 = 1
   job_1 = "Eng"
   resultado_esperado = "Usuário não é do tipo string"
   service = ServiceUser()

   # Chamada
   resultado = service.add_user(name=name_1, job=job_1)

   # Avaliacao
   assert resultado_esperado == resultado

 def test_add_user_not_exist(self):
  # Setup
  name_1 = "Simone"
  job_1 = "QA"
  resultado_esperado = "Usuário já existe"
  service = ServiceUser()

  # Adicionando um usuário inicialmente
  service.add_user(name=name_1, job=job_1)

  # Chamada com mesmo nome de usuário
  resultado = service.add_user(name=name_1, job="QA")

  # Avaliação
  assert resultado_esperado == resultado

 def test_add_user_double(self):
  # Setup
  name_1 = "Simone"
  job_1 = "QA"
  resultado_esperado = "Usuário já existe"
  service = ServiceUser()
  # Adicionar o usuário pela primeira vez
  resultado = service.add_user(name=name_1, job=job_1)

  # Tentar adicionar o mesmo usuário novamente

  resultado = service.add_user(name=name_1, job=job_1)

  assert resultado == resultado_esperado

 def test_remove_user_success(self):
  # Setup
  name_1 = "Simone"
  job_1 = "QA"
  resultado_esperado = "Usuário removido com sucesso"
  service = ServiceUser()
  resultado = service.add_user(name=name_1, job=job_1)

  # Chamada
  resultado = service.remove_user(name=name_1)

  # Avaliacao
  assert resultado_esperado == resultado

 def test_remove_null_user(self):
  # Setup
  name = None
  resultado_esperado = 'Usuário não encontrado'
  service = ServiceUser()

  # Chamada
  resultado = service.remove_user(name=name)

  # Avaliacao
  assert resultado_esperado == resultado

 def test_remove_user_404(self):
  # Setup
  name_1 = "Mone"
  job_1 = "QA"
  resultado_esperado = "Usuário não encontrado"
  service = ServiceUser()

  # Chamada
  resultado = service.remove_user(name=name_1)

  # Avaliacao
  assert resultado_esperado == resultado

 def test_remove_invalid_user(self):
  # Setup
   name_1 = "Pyton"
   service = ServiceUser()

   # Trying to delete user
   resultado_esperado = "Usuário não encontrado"
   resultado = service.remove_user(name=name_1)

  # Avaliação
   assert resultado_esperado == resultado

 def test_update_user_success(self):
  # Setup
  name_1 = "Simone"
  job_1 = "Tester"
  resultado_esperado = "Job atualizado com sucesso"
  service = ServiceUser()

  service.add_user(name_1, job_1)  # Adiciona o usuário antes de atualizar

  # Chamada
  resultado = service.update_user(name=name_1, new_job=job_1)

  # Avaliacao
  assert resultado_esperado == resultado

 def test_update_job_null_user(self):
  # Setup
  name_1 = None
  job_1 = 'Líder'
  resultado_esperado = 'Usuário não encontrado'
  service = ServiceUser()

  # Chamada
  resultado = service.update_user(name=name_1, new_job=job_1)

  # Avaliação
  assert resultado_esperado == resultado

 def test_update_job_invalid_user(self):
   #Setup
   name = 'Mone'
   job = 'PO'
   resultado_esperado = 'Usuário não encontrado'
   service = ServiceUser()

   #Chamada
   resultado = service.update_user(name=name, new_job=job)

   #Avaliação
   assert resultado_esperado == resultado

 def test_select_user_success(self):
  # Setup
  name = 'Simone'
  resultado_esperado = "Job: QA"
  service = ServiceUser()

  # Chamada
  resultado = service.select_user(name=name)

  # Avaliação

  assert resultado_esperado == resultado

 def test_select_invalid_user(self):
        #Setup
        name = 'Cicrano'
        resultado_esperado = 'Usuario não encontrado'
        service = ServiceUser()

        #Chamada
        resultado = service.select_user(name=name)

        #Avaliação
        assert resultado_esperado == resultado

 def test_select_null_user(self):
  # Setup
  name = None
  resultado_esperado = 'Usuario não encontrado'
  service = ServiceUser()

  # Chamada
  resultado = service.select_user(name=name)

  # Avaliação
  assert resultado_esperado == resultado















