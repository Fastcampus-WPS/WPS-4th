from django.db import connection


def lsql():
    print(connection.queries[-1])
