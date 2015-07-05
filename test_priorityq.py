from __future__ import unicode_literals
import pytest

from priorityq import PriorityQ, QNode


@pytest.fixture()
def QNode_list():
    QNode_list = [
        QNode(10),
        QNode(5, 2),
        QNode(100, 1)
    ]
    return QNode_list


@pytest.fixture()
def base_pqueue(QNode_list):
    return base_pqueue(QNode_list)


def test_QNode_init_no_priority():
    node1 = QNode(10)
    assert node1.val == 10
    assert node1.priority is None


def test_QNode_init_with_priority():
    node1 = QNode('string', 0)
    assert node1.val == 'string'
    assert node1.priority is 0
    assert node1.val, node1.priority == ('string', 0)


def test_QNode_val_comparison():
    node1 = QNode(10)
    node2 = QNode(5)
    assert node1 > node2


def test_QNode_priority_comparison():
    node1 = QNode(10, 0)
    node2 = QNode(10)
    assert node1 < node2


def test_QNode_equal_priority_comparison():
    node1 = QNode(10, 1)
    node2 = QNode(5, 1)
    assert node1 > node2


def test_QNode_equality_comparison():
    node1 = QNode(10, 10)
    node2 = QNode(10, 10)
    assert node1 == node2


def test_PriorityQ_init_empty():
    pqueue = PriorityQ()
    assert isinstance(pqueue, PriorityQ)
    assert len(pqueue) == 0


def test_PriorityQ_init_iterable_no_QNodes():
    pqueue = PriorityQ([10, 9, 8, 7, 6, 5])
    assert len(pqueue) == 6
    assert pqueue[0].val == 5
    assert pqueue[0].priority is None


def test_PriorityQ_init_iterable_with_QNodes(QNode_list):
    pqueue = PriorityQ(QNode_list)
    assert len(pqueue) == 3
    assert pqueue[0].val == 100
    assert pqueue[0].priority == 1


def test_insert_item_not_QNode_to_empty():
    queue = PriorityQ()
    queue.insert(50)
    assert len(queue) == 1
    assert queue[0].val == 50
    assert queue[0].priority is None


def test_insert_item_QNode_to_empty():
    node1 = QNode(10, 0)
    pqueue = PriorityQ()
    pqueue.insert(node1)
    assert len(pqueue) == 1
    assert pqueue[0].val == 10
    assert pqueue[0].priority == 0


def test_insert_item_not_QNode_to_filled(base_pqueue):
    base_pqueue.insert(500)
    assert len(base_pqueue) == 4
    assert base_pqueue[0].val == 100
    assert base_pqueue[0].priority == 1


def test_insert_QNode_to_filled(base_pqueue):
    node1 = QNode(10, 0)
    base_pqueue.insert(node1)
    assert len(base_pqueue) == 4
    assert base_pqueue[0].val == 10
    assert base_pqueue[0].priority == 0


def test_pop(base_pqueue):
    
