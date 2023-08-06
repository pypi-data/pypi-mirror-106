Changelog
=========


1.2 (2021-05-19)
----------------

- Allow accessing ``_authenticator`` from plone.protect.
  It fixes a NotFound error when submitting a PloneFormGen form,
  see `issue 229 <https://github.com/smcmahon/Products.PloneFormGen/pull/229>`_.
  Should solve similar cases as well.

- Fixed the expressions patch.
  It unintentionally changed the behavior of the ``TrustedBoboAwareZopeTraverse`` class as well.
  Most importantly, it let this class use ``restrictedTraverse``, so it did unwanted security checks:
  this class is used for expressions in trusted templates on the file system.
  Needed for all Plone versions, except 4.3 when it does not have the optional ``five.pt`` package.
  One test is: login as Editor and go to the ``@@historyview`` of a page.
  If you get an ``Unauthorized`` error, you should upgrade to the new version.
  If you are unsure: install this version.


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
