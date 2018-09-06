"""
Application address book
Test if data from UI matches data from DB
"""


def test_db_matches_ui(app, db):
    ui_groups = app.group.get_group_list()
    db_groups = db.get_group_list()
    ui_groups.sort(key=lambda x: int(x.gid), reverse=True)
    db_groups.sort(key=lambda x: int(x.gid), reverse=True)

    print()
    print(ui_groups)
    print(db_groups)

    assert ui_groups == db_groups
