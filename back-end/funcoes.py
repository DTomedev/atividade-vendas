from conexao import conectar

def criar_tabela():
    conexao ,cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                categoria VARCHAR(50),
                preco NUMERIC(10,2),
                quantidade INT
                """);
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()   

#criar_tabela()

def inserir_produtos(nome, categoria, preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
            "INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES(%s, %s, %s, %s)",
            (nome, categoria, preco, quantidade)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir produto: {erro}")
        finally:
            cursor.close()
            conexao.close()

#inserir_produto("", "", , )

def listar_produtos():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
            "SELECT * FROM produtos ORDER BY ID",
            )
            return cursor.fetchall()
            
        except Exception as erro:
            print(f"Erro ao tentar listar produtos: {erro}")
        finally:
            cursor.close()
            conexao.close()
    
        
def atualizar_filme(id_produto, novo_preco, nova_quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
            "UPDATE filmes SET quantidade = %s WHERE Id = %s SET preco = %s",
            (id_produto, novo_preco, nova_quantidade)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao tentar atualizar produtos: {erro}")
        finally:
            cursor.close()
            conexao.close()


def deletar_filme(id_produto):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM filmes WHERE id = %s",
                (id_produto,)
                )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao tentar deletar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()