import pytest
from pages.sale_page import SalePage
from pages.customer_account_create import CustomerAccountCreate
from pages.collections_eco_friendly import CollectionsEcoFriendly


@pytest.fixture()
def customer_account_create(page):
    return CustomerAccountCreate(page)


@pytest.fixture()
def collections_eco_friendly(page):
    return CollectionsEcoFriendly(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)
