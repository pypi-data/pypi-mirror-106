from Products.PageTemplates import Expressions
from zExceptions import NotFound


_orig_boboAwareZopeTraverse = Expressions.boboAwareZopeTraverse


def boboAwareZopeTraverse(object, path_items, econtext):
    """Traverses a sequence of names, first trying attributes then items.

    This uses zope.traversing path traversal where possible and interacts
    correctly with objects providing OFS.interface.ITraversable when
    necessary (bobo-awareness).

    Our change: disallow any item starting with an underscore.
    """
    for name in list(path_items):
        if name.startswith("_") and name != "__name__":
            raise NotFound(name)
    return _orig_boboAwareZopeTraverse(object, path_items, econtext)


Expressions.boboAwareZopeTraverse = boboAwareZopeTraverse
Expressions.ZopePathExpr._TRAVERSER = staticmethod(boboAwareZopeTraverse)

# But wait, in Zope 2 you can use five.pt,
# which has a BoboAwareZopeTraverse class.
# And in early Zope 4, the same is true for Products.PageTemplates
# You either have one or both.
try:
    from Products.PageTemplates.expression import BoboAwareZopeTraverse
except ImportError:
    try:
        from five.pt.expressions import BoboAwareZopeTraverse
    except ImportError:
        BoboAwareZopeTraverse = None

if BoboAwareZopeTraverse is not None:
    BoboAwareZopeTraverse._orig_traverse = BoboAwareZopeTraverse.traverse

    def traverse(cls, base, request, path_items):
        """See ``zope.app.pagetemplate.engine``."""
        for name in list(path_items):
            if name.startswith("_") and name != "__name__":
                raise NotFound(name)
        return cls._orig_traverse(base, request, path_items)

    BoboAwareZopeTraverse.traverse = classmethod(traverse)
