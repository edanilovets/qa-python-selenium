"""
Application address book
Tests for deletion groups
"""


def test_delete_first_group(app):
    app.group.delete_first_group()
