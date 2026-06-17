
Pacientes={}


def creaId(Dic):
    id=len(Dic)
    return (id+1)

def agregar(Dic):
    nom=input('nombre: ')
    eda=int(input('edad: '))
    pes=int(input('peso: '))
    sex=input('sexo: ')
    id=creaId(Dic)
    Dic[id]={'nom':nom,'eda':eda,'pes':pes,'sex':sex}
    return Dic

def editar(Dic):
  id=int(input('id del paciente por editar:'))
  nom=input('nombre: ')
  eda=input('edad: ')
  pes=input('peso: ')
  sex=input('sexo: ')
  Dic[id]={'nom':nom,'eda':eda,'pes':pes,'sex':sex}

def borrar(Dic):
  id=int(input('id del paciente por borrar:'))
  Dic.pop(id)
  for i in list(Dic.keys()): 
    if i > id: 
        Dic[i-1] = Dic.pop(i)  
  return Dic

def verPacientes(Dic):
    print('\n********** LISTA **********\n')
    listaPaciente='ID'+'\t'+'NOMBRE'+'\t'+'EDAD'+'\t'+'PESO'+'\t'+'SEXO'+'\n'
    for i in Dic:
        listaPaciente+=str(i)+'\t'+Dic[i]['nom']+'\t'+str(Dic[i]['eda'])+'\t'+str(Dic[i]['pes'])+'\t'+Dic[i]['sex']+'\n'
    print(listaPaciente)
 

def menu():
    print('**********MENU**********')
    print('0-TERMINAR PROCESO\n1-CREAR PACIENTE\n2-EDITAR DATOS DE PACIENTE\n3-BORRAR PACIENTE\n4-LISTAR TODOS LOS PACIENTES')


menu()

op=int(input('operecion que desea realizar: '))

while op!=0:
    if op==1:
        print('****** CREAR PACIENTE ******')
        agregar(Pacientes)
    elif op==2:
        print('****** EDITAR UN PACIENTE ******')
        editar(Pacientes)
    elif op==3:
        print('****** BORRAR PACIENTE ******')
        borrar(Pacientes)
    elif op==4:
        print('****** LISTA DE PACIENTES ******')
        verPacientes(Pacientes)
    else:
        print('** opcion no valida **')

    menu()
    op=int(input('operecion que desea realizar: '))
