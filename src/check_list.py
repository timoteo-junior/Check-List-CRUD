from datetime import datetime

class Tarefa:
    def __init__(self, descricao, vencimento):
        self.descricao = descricao
        self.vencimento = vencimento
        self.concluida = False

    def __str__(self):
        status = "Concluida" if self.concluida else "Pendente"
        return f"[{status}] {self.descricao} — Vence em: {self.vencimento}"


class ToDoList:
    def __init__(self):
        self.tarefas = []

    # CREATE
    def adicionar_tarefa(self, descricao, vencimento):
        nova = Tarefa(descricao, vencimento)
        self.tarefas.append(nova)
        print("Tarefa adicionada com sucesso!")

    # READ
    def listar_tarefas(self, status=None):
        print("\n--- LISTA DE TAREFAS ---")

        for t in self.tarefas:
            if status == "pendente" and t.concluida:
                continue
            if status == "concluida" and not t.concluida:
                continue
            print(t)

    # UPDATE
    def marcar_concluida(self, indice):
        try:
            self.tarefas[indice].concluida = True
            print("Tarefa marcada como concluida!")
        except:
            print("Indice invalido.")

    # DELETE
    def remover_tarefa(self, indice):
        try:
            self.tarefas.pop(indice)
            print("Tarefa removida!")
        except:
            print("Indice invalido.")


def menu():
    todo = ToDoList()

    while True:
        print("\n--- MENU ---")
        print("1. Adicionar tarefa")
        print("2. Listar todas")
        print("3. Listar pendentes")
        print("4. Listar concluídas")
        print("5. Marcar tarefa como concluida")
        print("6. Remover tarefa")
        print("0. Sair")

        op = input("Escolha: ")

        if op == "1":
            descricao = input("Descrição: ")
            venc = input("Data de vencimento (DD/MM/AAAA): ")
            todo.adicionar_tarefa(descricao, venc)

        elif op == "2":
            todo.listar_tarefas()

        elif op == "3":
            todo.listar_tarefas("pendente")

        elif op == "4":
            todo.listar_tarefas("concluida")

        elif op == "5":
            indice = int(input("Número da tarefa: "))
            todo.marcar_concluida(indice)

        elif op == "6":
            indice = int(input("Número da tarefa: "))
            todo.remover_tarefa(indice)

        elif op == "0":
            break

        else:
            print("Opcao invalida!")


menu()
