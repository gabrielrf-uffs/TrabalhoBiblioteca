class Livro:
  titulo=''
  autor=''
  ano=''
  codigo=''
  status=''
def menuLivro():
  print('1.Cadastrar livro\n2.Consultar livro\n3.Alterar dados\n4.Remover livro\n5.Listar todos\n6.Realizar empréstimo\n7.Realizar devolução\n8.Sair')
  op=int(input('Opção: '))
  return op
def cadastrarLivro():
  print('----------------------')
  livro=Livro()
  livro.titulo=input('Título: ')
  livro.autor=input('Autor: ')
  livro.ano=input('Ano: ')
  livro.codigo=input('Código: ')
  livro.status='Disponível'
  print('----------------------')
  print('Livro cadastrado com sucesso!')
  print('----------------------')
  return livro
def consultarLivro(c):
  x=0
  print('----------------------')
  coua=input('Código ou autor: ')
  print('----------------------')
  for i in range(len(c)):
    if c[i].codigo==coua or c[i].autor==coua:
      print('Título:',c[i].titulo)
      print('Autor:',c[i].autor)
      print('Ano:',c[i].ano)
      print('Código:',c[i].codigo)
      print('Status:',c[i].status)
      print('----------------------')
      x+=1
  if x==0:
    print('----------------------')
    print('Livro não encontrado!')
    print('----------------------')
def alterarLivro(l):
  print('----------------------')
  código=input('Código: ')
  print('----------------------')
  for i in range(len(l)):
    if l[i].codigo==código:
      print('Título:',l[i].titulo)
      print('Autor:',l[i].autor)
      print('Ano:',l[i].ano)
      print('----------------------')
      x=int(input('1.Título\n2.Autor\n3.Ano\n0.Sair\nOpção: '))
      if x==1:
        print('----------------------')
        l[i].titulo=input('Título: ')
        print('----------------------')
        print('Livro alterado com sucesso!')
        print('----------------------')
      if x==2:
        print('----------------------')
        l[i].autor=input('Autor: ')
        print('----------------------')
        print('Livro alterado com sucesso!')
        print('----------------------')
      if x==3:
        print('----------------------')
        l[i].ano=input('Ano: ')
        print('----------------------')
        print('Livro alterado com sucesso!')
        print('----------------------')
      if x==0:
        print('----------------------')
        print('Livro não alterado')
        print('----------------------')
      return
  print('----------------------')
  print('Livro não encontrado!')
  print('----------------------')
def removerLivro(l):
  print('----------------------')
  codigo=input('Código: ')
  print('----------------------')
  for i in range(len(l)):
    if l[i].codigo==codigo:
      print('Título:',l[i].titulo)
      print('Autor:',l[i].autor)
      print('Ano:',l[i].ano)
      print('Código:',l[i].codigo)
      print('Status:',l[i].status)
      print('----------------------')
      print('Deseja remover este livro?')
      print('1.Sim\n2.Não')
      x=int(input('Opção: '))
      if x==1:
        l.pop(i)
        print('----------------------')
        print('Livro removido com sucesso!')
        print('----------------------')
      if x==2:
        print('----------------------')
        print('Livro não removido!')
        print('----------------------')
      return
def listarLivro(l):
  if len(l)==0:
    print('----------------------')
    print('Nenhum livro cadastrado!')
    print('----------------------')
  else:
    print('----------------------')
    for i in range(len(l)):
      print('Título:',l[i].titulo)
      print('Autor:',l[i].autor)
      print('Ano:',l[i].ano)
      print('Código:',l[i].codigo)
      print('Status:',l[i].status)
      print('----------------------')
def emprestarLivro(l):
  print('----------------------')
  codigo=input('Código: ')
  print('----------------------')
  for i in range(len(l)):
    if l[i].codigo==codigo:
      print('Título:',l[i].titulo)
      print('Autor:',l[i].autor)
      print('Ano:',l[i].ano)
      if l[i].status=='Disponível':
        print('----------------------')
        print('Deseja emprestar este livro?')
        print('1.Sim\n2.Não')
        x=int(input('Opção: '))
        if x==1:
          l[i].status='Emprestado'
          print('----------------------')
          print('Livro emprestado com sucesso!')
          print('----------------------')
        if x==2:
          print('----------------------')
          print('Livro não emprestado!')
          print('----------------------')
        return
      else:
        print('----------------------')
        print('Livro já emprestado!')
        print('----------------------')
        return
  print('----------------------')
  print('Livro não encontrado!')
  print('----------------------')
def devolverLivro(l):
  print('----------------------')
  codigo=input('Código: ')
  print('----------------------')
  for i in range(len(l)):
    if l[i].codigo==codigo:
      print('Título:',l[i].titulo)
      print('Autor:',l[i].autor)
      print('Ano:',l[i].ano)
      if l[i].status=='Emprestado':
        print('----------------------')
        print('Deseja devolver este livro?')
        print('1.Sim\n2.Não')
        x=int(input('Opção: '))
        if x==1:
          l[i].status='Disponível'
          print('----------------------')
          print('Livro devolvido com sucesso!')
          print('----------------------')
          return
        if x==2:
          print('----------------------')
          print('Livro não devolvido!')
          print('----------------------')
        return
      else:
        print('----------------------')
        print('Livro já disponível!')
        print('----------------------')
livros=[]
x=menuLivro()
while x!=0:
  if x==1:
    livros.append(cadastrarLivro())
    x=menuLivro()
  if x==2:
    consultarLivro(livros)
    x=menuLivro()
  if x==3:
    alterarLivro(livros)
    x=menuLivro()
  if x==4:
    removerLivro(livros)
    x=menuLivro()
  if x==5:
    listarLivro(livros)
    x=menuLivro()
  if x==6:
    emprestarLivro(livros)
    x=menuLivro()
  if x==7:
    devolverLivro(livros)
    x=menuLivro()
  if x==8:
    break
print('----------------------')
print('Programa encerrado!')