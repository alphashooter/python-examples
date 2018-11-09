from typing import Any, Union, Optional, Iterable


class Node(object):
    def __init__(self, value: Any):
        self.value: Any = value
        self.next: Optional[Node] = None


class LinkedList(object):
    def __init__(self, iterable: Optional[Iterable] = None):
        self.__head = Node(None)
        self.__length = 0

        if iterable is not None:
            # append elements from the given iterable
            last = self.__head
            for value in iterable:
                node = Node(value)
                last.next = node
                last = node
                self.__length += 1

    def insert(self, index: int, value: Any) -> None:
        if index < 0:
            index = self.__length + index

        # check index range
        assert 0 <= index <= self.__length, 'index is out of range'

        if index == self.__length:
            self.append(value)
            return

        raise NotImplementedError()

    def append(self, value: Any) -> None:
        raise NotImplementedError()

    def erase(self, index: int) -> None:
        raise NotImplementedError()

    def __iter__(self):
        node = self.__head.next
        while node is not None:
            yield node.value
            node = node.next

    def __get_single(self, index: int) -> Any:
        if index < 0:
            index = self.__length + index

        # check index range
        assert 0 <= index < self.__length, 'index is out of range'

        node = self.__head
        for i in range(-1, index):
            node = node.next
        return node.value

    def __get_slice(self, index: slice) -> 'LinkedList':
        raise NotImplementedError()

    def __getitem__(self, index: Union[int, slice]):
        if isinstance(index, int):
            return self.__get_single(index)
        elif isinstance(index, slice):
            return self.__get_slice(index)
        else:
            raise TypeError('expected int or slice, but got %s' % type(index).__name__)

    def __set_single(self, index: int, value: Any) -> None:
        if index < 0:
            index = self.__length + index

        # check index range
        assert 0 <= index < self.__length, 'index is out of range'

        node = self.__head
        for i in range(-1, index):
            node = node.next
        node.value = value

    def __set_slice(self, index: slice, values: Iterable) -> None:
        # use built-in function zip()
        raise NotImplementedError()

    def __setitem__(self, index: Union[int, slice], value: Any):
        if isinstance(index, int):
            self.__set_single(index, value)
        elif isinstance(index, slice):
            self.__set_slice(index, value)
        else:
            raise TypeError('expected int or slice, but got %s' % type(index).__name__)

    def __del_single(self, index: int) -> None:
        self.erase(index)

    def __del_slice(self, index: slice) -> None:
        # convert slice into range
        seq = range(*index.indices(self.__length))
        if index.step > 0:
            # force reversed pass
            seq = reversed(seq)
        for index in seq:
            self.__del_single(index)

    def __delitem__(self, index: Union[int, slice]) -> None:
        if isinstance(index, int):
            self.__del_single(index)
        elif isinstance(index, slice):
            self.__del_slice(index)
        else:
            raise TypeError('expected int or slice, but got %s' % type(index).__name__)

    def __len__(self):
        return self.__length
