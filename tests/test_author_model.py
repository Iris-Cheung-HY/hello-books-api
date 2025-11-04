from app.models.author import Author
import pytest

def test_from_dict_returns_book():
    # Arrange
    author_data = {
        "name": "Iris Cheung 2"
    }

    # Act
    new_book = Author.from_dict(author_data)

    # Assert
    assert new_book.name == "Iris Cheung 2"
