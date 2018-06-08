import pytest
import task

def test_turn_off_print_access():
    task.turn_off_print_access('a@gmail.com')
    row = task.c.execute("SELECT printer_access FROM employees WHERE email = 'a@gmail.com'")
    y=task.c.fetchone()[0]
    assert y == 0

def test_turn_on_print_access():
    task.turn_on_print_access('a@gmail.com')
    row = task.c.execute("SELECT printer_access FROM employees WHERE email = 'a@gmail.com'")
    y=task.c.fetchone()[0]
    assert y == 1

def test_turn_off_storage_access():
    task.turn_off_storage_access('a@gmail.com')
    row = task.c.execute("SELECT storage_access FROM employees WHERE email = 'a@gmail.com'")
    y=task.c.fetchone()[0]
    assert y == 0

def test_turn_on_storage_access():
    task.turn_on_storage_access('a@gmail.com')
    row = task.c.execute("SELECT storage_access FROM employees WHERE email = 'a@gmail.com'")
    y=task.c.fetchone()[0]
    assert y == 1

def test_turn_off_phone_access():
    task.turn_off_phone_access('a@gmail.com')
    row = task.c.execute("SELECT phone_access FROM employees WHERE email = 'a@gmail.com'")
    y=task.c.fetchone()[0]
    assert y == 0

def test_turn_on_phone_access():
    task.turn_on_phone_access('a@gmail.com')
    row = task.c.execute("SELECT phone_access FROM employees WHERE email = 'a@gmail.com'")
    y=task.c.fetchone()[0]
    assert y == 1
