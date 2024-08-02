import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Тест фильтра по валюте
def test_filter_by_currency(transactions):
    transaction_filter = filter_by_currency(transactions, "USD")
    assert next(transaction_filter)["id"] == 939719570
    assert next(transaction_filter)["id"] == 142264268
    assert next(transaction_filter)["id"] == 895315941

def test_transaction_descriptions(transactions):
    descriptions_generator = transaction_descriptions(transactions)
    assert next(descriptions_generator) == "Перевод организации"
    assert next(descriptions_generator) == "Перевод со счета на счет"
    assert next(descriptions_generator) == "Перевод со счета на счет"
    assert next(descriptions_generator) == "Перевод с карты на карту"
    assert next(descriptions_generator) == "Перевод организации"

def test_card_number_generator() -> None:
    generator = card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"
