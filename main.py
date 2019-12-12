
def is_dictionary(value):
    return isinstance(value, dict)

def is_list(value):
    return isinstance(value, list)


def dict_map(modifier, dictionary):
    new_dict = dict()

    for (key, value) in dictionary.items():
        new_dict[key] = modifier(value)

    return new_dict

def apply_to_leafs(applier):
    def recur(root):
        if is_list(root):
            return list(map(apply_to_leafs(applier), root))
        if is_dictionary(root):
            return dict_map(apply_to_leafs(applier), root)

        # if none of the above options are fulfilled
        # we assume that we have a leaf
        leaf = root
        return applier(leaf)

    return recur
