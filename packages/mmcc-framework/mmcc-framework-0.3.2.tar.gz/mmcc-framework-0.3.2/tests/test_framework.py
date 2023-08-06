from unittest import TestCase

from mmcc_framework.activity import Activity, ActivityType
from mmcc_framework.framework import Framework, Response, CTX_COMPLETED
from mmcc_framework.process import Process
from mmcc_framework.nlu_adapters import NoNluAdapter


class TestFrameworkBehaviourOR(TestCase):
    @staticmethod
    def callback_getter(_):
        return lambda d, k, c, a: Response(k, c, True, choice=d["choice"] if "choice" in d else "")

    def setUp(self) -> None:
        self.my_framework = Framework(
            Process(first_activity_id="start",
                    activities=[Activity("start", "gateway", ActivityType.START),
                                Activity("gateway", "end", ActivityType.OR, ["xor", "par", "or"]),
                                Activity("xor", None, ActivityType.XOR, ["A", "B"]),
                                Activity("A", None, ActivityType.TASK),
                                Activity("B", None, ActivityType.TASK),
                                Activity("par", None, ActivityType.PARALLEL, ["C", "D"]),
                                Activity("C", None, ActivityType.TASK),
                                Activity("D", None, ActivityType.TASK),
                                Activity("or", None, ActivityType.OR, ["E", "F"]),
                                Activity("E", None, ActivityType.TASK),
                                Activity("F", None, ActivityType.END),
                                Activity("end", None, ActivityType.END)]),
            {"my_key": "a value"},
            {"ctx_key": "ctx value"},
            self.callback_getter,
            NoNluAdapter([]),
            lambda k: None)

    def test_path_1(self):
        path = [["", "gateway", []],
                ["xor", "xor", ["gateway"]],
                ["A", "A", ["gateway"]],
                ["", "gateway", ["gateway"]],
                ["par", "par", ["gateway"]],
                ["C", "C", ["gateway"]],
                ["", "par", ["gateway"]],
                ["D", "D", ["gateway", "par"]],
                ["", "par", ["gateway", "par"]],
                [None, "gateway", ["gateway"]],
                ["or", "or", ["gateway"]],
                ["E", "E", ["gateway", "or"]],
                ["", "or", ["gateway", "or"]],
                [None, "gateway", ["gateway"]],
                ["or", "or", ["gateway"]],
                ["F", "F", ["gateway", "or"]],
                ["", "F", ["gateway", "or"]]]
        for index, step in enumerate(path):
            self.my_framework.handle_data_input({"choice": step[0]} if step[0] != "" else {"data": "value"})
            self.assertEqual(self.my_framework._current.id, step[1], f"Step index when test failed: {index}, "
                                                                     f"expected: {step[1]}")
            self.assertEqual(self.my_framework._ctx[CTX_COMPLETED], step[2], f"Step index when test failed: {index}")

    def test_path_2(self):
        path = [["", "gateway", []],
                ["xor", "xor", ["gateway"]],
                ["B", "B", ["gateway"]],
                ["", "gateway", ["gateway"]],
                ["or", "or", ["gateway"]],
                ["E", "E", ["gateway", "or"]],
                ["", "or", ["gateway", "or"]],
                [None, "gateway", ["gateway"]],
                ["par", "par", ["gateway"]],
                ["D", "D", ["gateway"]],
                ["", "par", ["gateway"]],
                ["C", "C", ["gateway", "par"]],
                ["", "par", ["gateway", "par"]],
                ["D", "D", ["gateway", "par"]],
                ["", "par", ["gateway", "par"]],
                [None, "gateway", ["gateway"]],
                [None, "end", []],
                ["", "end", []]]
        for index, step in enumerate(path):
            self.my_framework.handle_data_input({"choice": step[0]} if step[0] != "" else {"data": "value"})
            self.assertEqual(self.my_framework._current.id, step[1], f"Step index when test failed: {index}, "
                                                                     f"expected: {step[1]}")
            self.assertEqual(self.my_framework._ctx[CTX_COMPLETED], step[2], f"Step index when test failed: {index}")


class TestFrameworkBehaviourPAR(TestCase):
    @staticmethod
    def callback_getter(_):
        return lambda d, k, c, a: Response(k, c, True, choice=d["choice"] if "choice" in d else "")

    def setUp(self) -> None:
        self.my_framework = Framework(
            Process(first_activity_id="start",
                    activities=[Activity("start", "gateway", ActivityType.START),
                                Activity("gateway", "end", ActivityType.PARALLEL, ["xor", "par", "or"]),
                                Activity("xor", None, ActivityType.XOR, ["A", "B"]),
                                Activity("A", None, ActivityType.TASK),
                                Activity("B", None, ActivityType.TASK),
                                Activity("par", None, ActivityType.PARALLEL, ["C", "D"]),
                                Activity("C", None, ActivityType.TASK),
                                Activity("D", None, ActivityType.TASK),
                                Activity("or", None, ActivityType.OR, ["E", "F"]),
                                Activity("E", None, ActivityType.TASK),
                                Activity("F", None, ActivityType.END),
                                Activity("end", None, ActivityType.END)]),
            {"my_key": "a value"},
            {"ctx_key": "ctx value"},
            self.callback_getter,
            NoNluAdapter([]),
            lambda k: None)

    def test_path_1(self):
        path = [["", "gateway", []],
                ["xor", "xor", []],
                ["A", "A", []],
                ["", "gateway", []],
                ["par", "par", []],
                ["C", "C", []],
                ["", "par", []],
                ["D", "D", ["par"]],
                ["", "par", ["par"]],
                [None, "gateway", []],
                ["or", "or", ["gateway"]],
                ["E", "E", ["gateway", "or"]],
                ["", "or", ["gateway", "or"]],
                [None, "gateway", ["gateway"]],
                ["or", "or", ["gateway"]],
                ["F", "F", ["gateway", "or"]],
                ["", "F", ["gateway", "or"]]]
        for index, step in enumerate(path):
            self.my_framework.handle_data_input({"choice": step[0]} if step[0] != "" else {"data": "value"})
            self.assertEqual(self.my_framework._current.id, step[1], f"Step index when test failed: {index}, "
                                                                     f"expected: {step[1]}")
            self.assertEqual(self.my_framework._ctx[CTX_COMPLETED], step[2], f"Step index when test failed: {index}")

    def test_path_2(self):
        path = [["", "gateway", []],
                ["xor", "xor", []],
                ["B", "B", []],
                ["", "gateway", []],
                ["or", "or", []],
                ["E", "E", ["or"]],
                ["", "or", ["or"]],
                [None, "gateway", []],
                ["par", "par", ["gateway"]],
                ["D", "D", ["gateway"]],
                ["", "par", ["gateway"]],
                ["C", "C", ["gateway", "par"]],
                ["", "par", ["gateway", "par"]],
                ["D", "D", ["gateway", "par"]],
                ["", "par", ["gateway", "par"]],
                [None, "gateway", ["gateway"]],
                [None, "end", []],
                ["", "end", []]]
        for index, step in enumerate(path):
            self.my_framework.handle_data_input({"choice": step[0]} if step[0] != "" else {"data": "value"})
            self.assertEqual(self.my_framework._current.id, step[1], f"Step index when test failed: {index}, "
                                                                     f"expected: {step[1]}")
            self.assertEqual(self.my_framework._ctx[CTX_COMPLETED], step[2], f"Step index when test failed: {index}")


class TestFrameworkBehaviourXOR(TestCase):
    @staticmethod
    def callback_getter(_):
        return lambda d, k, c, a: Response(k, c, True, choice=d["choice"] if "choice" in d else "")

    def setUp(self) -> None:
        self.my_framework = Framework(
            Process(first_activity_id="start",
                    activities=[Activity("start", "gateway", ActivityType.START),
                                Activity("gateway", "end", ActivityType.XOR, ["xor", "par", "or"]),
                                Activity("xor", None, ActivityType.XOR, ["A", "B"]),
                                Activity("A", None, ActivityType.TASK),
                                Activity("B", None, ActivityType.TASK),
                                Activity("par", None, ActivityType.PARALLEL, ["C", "D"]),
                                Activity("C", None, ActivityType.TASK),
                                Activity("D", None, ActivityType.TASK),
                                Activity("or", None, ActivityType.OR, ["E", "F"]),
                                Activity("E", None, ActivityType.TASK),
                                Activity("F", None, ActivityType.END),
                                Activity("end", None, ActivityType.END)]),
            {"my_key": "a value"},
            {"ctx_key": "ctx value"},
            self.callback_getter,
            NoNluAdapter([]),
            lambda k: None)

    def test_path_1a(self):
        path = [["", "gateway", []],
                ["xor", "xor", []],
                ["A", "A", []],
                ["", "end", []],
                ["", "end", []]]
        for index, step in enumerate(path):
            self.my_framework.handle_data_input({"choice": step[0]} if step[0] != "" else {"data": "value"})
            self.assertEqual(self.my_framework._current.id, step[1], f"Step index when test failed: {index}, "
                                                                     f"expected: {step[1]}")
            self.assertEqual(self.my_framework._ctx[CTX_COMPLETED], step[2], f"Step index when test failed: {index}")

    def test_path_1b(self):
        path = [["", "gateway", []],
                ["par", "par", []],
                ["C", "C", []],
                ["", "par", []],
                ["D", "D", ["par"]],
                ["", "par", ["par"]],
                [None, "end", []],
                ["", "end", []]]
        for index, step in enumerate(path):
            self.my_framework.handle_data_input({"choice": step[0]} if step[0] != "" else {"data": "value"})
            self.assertEqual(self.my_framework._current.id, step[1], f"Step index when test failed: {index}, "
                                                                     f"expected: {step[1]}")
            self.assertEqual(self.my_framework._ctx[CTX_COMPLETED], step[2], f"Step index when test failed: {index}")

    def test_path_1c(self):
        path = [["", "gateway", []],
                ["or", "or", []],
                ["F", "F", ["or"]],
                ["", "F", ["or"]]]
        for index, step in enumerate(path):
            self.my_framework.handle_data_input({"choice": step[0]} if step[0] != "" else {"data": "value"})
            self.assertEqual(self.my_framework._current.id, step[1], f"Step index when test failed: {index}, "
                                                                     f"expected: {step[1]}")
            self.assertEqual(self.my_framework._ctx[CTX_COMPLETED], step[2], f"Step index when test failed: {index}")

    def test_path_2a(self):
        path = [["", "gateway", []],
                ["par", "par", []],
                ["D", "D", []],
                ["", "par", []],
                ["C", "C", ["par"]],
                ["", "par", ["par"]],
                ["D", "D", ["par"]],
                ["", "par", ["par"]],
                [None, "end", []],
                ["", "end", []]]
        for index, step in enumerate(path):
            self.my_framework.handle_data_input({"choice": step[0]} if step[0] != "" else {"data": "value"})
            self.assertEqual(self.my_framework._current.id, step[1], f"Step index when test failed: {index}, "
                                                                     f"expected: {step[1]}")
            self.assertEqual(self.my_framework._ctx[CTX_COMPLETED], step[2], f"Step index when test failed: {index}")


class TestFramework(TestCase):
    @staticmethod
    def callback_getter(_):
        return lambda d, k, c, a: Response(k, c, True)

    def setUp(self) -> None:
        self.my_kb = {"my_key": "a value"}
        self.my_ctx = {"ctx_key": "ctx value"}
        self.my_callback = self.callback_getter
        self.my_nlu = NoNluAdapter([])
        self.my_save = lambda k: None

    def test_init(self):
        my_proc = Process([Activity("one", None, ActivityType.START)], "one")

        my_framework = Framework(my_proc, self.my_kb, self.my_ctx, self.my_callback, self.my_nlu, self.my_save)
        self.assertEqual(my_framework._process, my_proc)
        self.assertEqual(my_framework._kb, self.my_kb)
        self.assertEqual(my_framework._ctx, self.my_ctx)
        self.assertEqual(my_framework._callback_getter.callbacks, self.my_callback)
        self.assertEqual(my_framework._nlu, self.my_nlu)
        self.assertEqual(my_framework._on_save, self.my_save)

    def test_init_dict(self):
        proc_dic = {
            "first_activity_id": "one",
            "activities": [{"my_id": "one", "next_id": None, "my_type": "task"}]
        }
        my_framework = Framework(proc_dic, self.my_kb, self.my_ctx, self.my_callback, self.my_nlu, self.my_save)
        self.assertEqual(my_framework._process.first.id, proc_dic["first_activity_id"])
        self.assertEqual(my_framework._process.activities[0].id, proc_dic["activities"][0]["my_id"])
        self.assertEqual(my_framework._process.activities[0].next_id, proc_dic["activities"][0]["next_id"])
        self.assertEqual(my_framework._process.activities[0].type.value, proc_dic["activities"][0]["my_type"])
        self.assertEqual(my_framework._kb, self.my_kb)
        self.assertEqual(my_framework._ctx, self.my_ctx)
        self.assertEqual(my_framework._callback_getter.callbacks, self.my_callback)
        self.assertEqual(my_framework._nlu, self.my_nlu)
        self.assertEqual(my_framework._on_save, self.my_save)

    def test_init_callback(self):
        my_proc = Process([Activity("one", None, ActivityType.START)], "one")

        def proc_call():
            return my_proc

        def kb_call():
            return self.my_kb

        my_framework = Framework(proc_call, kb_call, self.my_ctx, self.my_callback, self.my_nlu, self.my_save)

        self.assertEqual(my_framework._process, my_proc)
        self.assertEqual(my_framework._kb, self.my_kb)
        self.assertEqual(my_framework._ctx, self.my_ctx)
        self.assertEqual(my_framework._callback_getter.callbacks, self.my_callback)
        self.assertEqual(my_framework._nlu, self.my_nlu)
        self.assertEqual(my_framework._on_save, self.my_save)

    def test_init_callback_dict(self):
        proc_dic = {
            "first_activity_id": "one",
            "activities": [{"my_id": "one", "next_id": None, "my_type": "task"}]
        }

        def proc_call():
            return proc_dic

        def kb_call():
            return self.my_kb

        my_framework = Framework(proc_call, kb_call, self.my_ctx, self.my_callback, self.my_nlu, self.my_save)
        self.assertEqual(my_framework._process.first.id, proc_dic["first_activity_id"])
        self.assertEqual(my_framework._process.activities[0].id, proc_dic["activities"][0]["my_id"])
        self.assertEqual(my_framework._process.activities[0].next_id, proc_dic["activities"][0]["next_id"])
        self.assertEqual(my_framework._process.activities[0].type.value, proc_dic["activities"][0]["my_type"])
        self.assertEqual(my_framework._kb, self.my_kb)
        self.assertEqual(my_framework._ctx, self.my_ctx)
        self.assertEqual(my_framework._callback_getter.callbacks, self.my_callback)
        self.assertEqual(my_framework._nlu, self.my_nlu)
        self.assertEqual(my_framework._on_save, self.my_save)
