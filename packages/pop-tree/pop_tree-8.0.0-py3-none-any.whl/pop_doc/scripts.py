#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Dict

import pop.hub


def start():
    hub = pop.hub.Hub()
    hub.pop.sub.add(dyne_name="doc")
    hub.pop.sub.add(dyne_name="tree")

    hub.pop.config.load(["pop_doc", "pop_tree", "rend"], cli="pop_doc")

    for dyne in hub._dynamic:
        if not hasattr(hub, dyne):
            hub.pop.sub.add(dyne_name=dyne)
        try:
            hub.pop.sub.load_subdirs(hub[dyne], recurse=True)
        except AttributeError:
            ...

    tree = hub.tree.init.traverse()
    for key in hub.OPT.pop_doc.ref.split("."):
        if key in tree:
            tree = tree[key]
        else:
            for v in tree.values():
                if not isinstance(v, Dict):
                    continue
                elif key in v:
                    tree = v[key]
                    break
    ret = hub.tree.init.refs(tree)

    if not ret:
        raise KeyError(f"Reference does not exist on the hub: {hub.OPT.pop_doc.ref}")

    print(hub.output[hub.OPT.rend.output].display(ret))
