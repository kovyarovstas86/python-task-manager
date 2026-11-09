import unittest
from src.main import add_task, show_tasks, remove_task, tasks


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        tasks.clear()

    def test_add_task(self):
        self.assertTrue(add_task("Купить молоко"))
        self.assertEqual(len(tasks), 1)

    def test_reject_empty_task(self):
        self.assertFalse(add_task("   "))

    def test_remove_task(self):
        add_task("Позаниматься Git")
        self.assertTrue(remove_task(1))
        self.assertEqual(len(tasks), 0)


if __name__ == "__main__":
    unittest.main()
