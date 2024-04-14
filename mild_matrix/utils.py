
import collections


def split_list(list1d: list, n: int, mode="l") -> list:
    if not isinstance(list1d, collections.Iterable):
        raise TypeError("The given object is not an iterable object.")
    if mode != "l" and mode != "n":
        raise ValueError("The 'mode' parameter must be 'l' or 'n', current = {mode}")
    num = n
    length_list = len(list1d)
    if mode == "n":
        if length_list % num != 0:
            raise ValueError(
                "The length of the given list and the sublist length must have a divider relationship."
            )
        num = int(length_list / num)
        mode = "l"
    if mode == "l":
        if num <= 1:
            return list1d
        if len(list1d) % num != 0:
            raise ValueError(
                f"The length of sublist, {num}, must be a divider of original list, {len(list1d)}. "
            )
        rlist = []
        for i in range(0, int(length_list / num)):
            ni = num * i
            rlist.append([list1d[ni : ni + num]][0])
    return rlist