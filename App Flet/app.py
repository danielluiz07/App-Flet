from sqlalchemy import create_engine, create_mock_engine
from sqlalchemy.orm import sessionmaker

import flet as ft
from models import Produto 

CONN = "sqlite:///projeto2.db"

engine = create_engine(CONN, echo = True) 
Session = sessionmaker(bind=engine)
session = Session()

def main(page: ft.Page):
    page.title= "Cadastro App"

    lista_produtos = ft.ListView()

    def cadastrar(e):
        try:
            novo_produto = Produto(titulo=produto.value, preco=preco.value)
            session.add(novo_produto)
            session.commit()
            lista_produtos.controls.append(ft.Container(
                    ft.Text(produto.value),
                    bgcolor=ft.colors.BLACK12,
                    padding=15,
                    alignment=ft.alignment.center,
                    margin=3,
                    border_radius=10
                ))
            txt_erro.visible = False
            txt_acert.visible = True
        except:
            txt_erro.visible = True
            txt_acert.visible = False
        page.update
        print("Produto salvo com sucesso")

    txt_erro = ft.Container(ft.Text('ERROR! Ao salvar o produto'), visible=False, bgcolor=ft.colors.RED, padding=10, alignment=ft.alignment.center)
    txt_acert = ft.Container(ft.Text('Produto salvo com sucesso!'), visible=False,  bgcolor=ft.colors.GREEN, padding=10, alignment=ft.alignment.center)

    txtTitulo = ft.Text('Titulo do Produto:')
    produto = ft.TextField(label="Digite o titulo do produto... ", text_align=ft.TextAlign.LEFT)
    txtPreco = ft.Text('Preço do Produto:')
    preco = ft.TextField(value="0", label="Digite o preco do produto", text_align=ft.TextAlign.LEFT)
    btnProduto = ft.ElevatedButton('Cadastrar', on_click=cadastrar)

    page.add(
        txt_acert,
        txt_erro,
        txtTitulo, 
        produto,
        txtPreco,
        preco,
        btnProduto,
    )

    for p in session.query(Produto).all():
        lista_produtos.controls.append(
            ft.Container(
                ft.Text(p.titulo),
                bgcolor=ft.colors.BLACK12,
                padding=15,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=10
            )  
            )

        page.add(
            lista_produtos,
        )

ft.app(target=main)