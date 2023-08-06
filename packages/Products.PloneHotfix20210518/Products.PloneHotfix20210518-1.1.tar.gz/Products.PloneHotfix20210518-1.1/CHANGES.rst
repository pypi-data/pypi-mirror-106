Changelog
=========


1.1 (2021-05-18)
----------------

- Allow using ``__name__`` in untrusted expressions.
  The previous expressions patch was too strict.
  This may be needed in case you have templates that use `__name__`.
  This does not happen often, but one example is the ``caching-controlpanel`` view,
  which with the previous version may give a 404 NotFound error.
  In some Plone versions browser views are affected (Plone 4.3 with five.pt, 5.0, 5.1, 5.2.0-5.2.2).
  In all Plone versions skin or through-the-web templates are affected.
  When you see more NotFound errors than normal, you should install this new version.
  If you are unsure: install this version.


1.0 (2021-05-18)
----------------

- Initial release
