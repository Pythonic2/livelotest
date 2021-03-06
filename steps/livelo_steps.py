from behave import *
from pages.livelo_home_page import LiveloHomePage
from pages.lilevo_header_page import LiveloHeaderPage
from pages.lilevo_products_page import LiveloProductsPage
from pages.lilevo_cart_page import LilevoCartPage
from nose.tools import assert_equals


livelohomepage = LiveloHomePage()

liveloheaderpage = LiveloHeaderPage()

lilevoproductspage = LiveloProductsPage()

lilevocartpage = LilevoCartPage()


""" steps do bdd """

@given(u'que acesso a página da lilevo')
def step_impl(context):
    livelohomepage.acess_page('https://www.livelo.com.br/')
    livelohomepage.coockies()


@given(u'que preencho o campo de pesquisa com Berço')
def step_impl(context):

    liveloheaderpage.search_for_product()


@given(u'escolho um produto e clico nele')
def step_impl(context):
   lilevoproductspage.choose_product()


@given(u'clico no botão adicionar ao carrinho')
def step_impl(context):
    lilevoproductspage.add_to_cart()


@when(u'clico no botao não quero o desconto')
def step_impl(context):
    lilevoproductspage.dont_want_discount()



@then(u'devo visualizar o produto no carrinho')
def step_impl(context):
   assert_equals(lilevocartpage.get_text_cart,'Seu carrinho')
