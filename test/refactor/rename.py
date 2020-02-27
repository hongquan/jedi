"""
Test coverage for renaming is mostly being done by testing
`Script.get_references`.
"""

# -------------------------------------------------- no-name
#? 0 error {'new_name': 'blabla'}
1
# ++++++++++++++++++++++++++++++++++++++++++++++++++
There is no name under the cursor
# -------------------------------------------------- simple
def test1():
    #? 7 {'new_name': 'blabla'}
    test1()
    AssertionError
    return test1, test1.not_existing
# ++++++++++++++++++++++++++++++++++++++++++++++++++
--- refactor/rename.py
+++ refactor/rename.py
@@ -1,6 +1,6 @@
-def test1():
+def blabla():
     #? 7 {'new_name': 'blabla'}
-    test1()
+    blabla()
     AssertionError
-    return test1, test1.not_existing
+    return blabla, blabla.not_existing
# -------------------------------------------------- var-not-found
undefined_var
#? 0 {'new_name': 'lala'}
undefined_var
# ++++++++++++++++++++++++++++++++++++++++++++++++++
--- refactor/rename.py
+++ refactor/rename.py
@@ -1,4 +1,4 @@
 undefined_var
 #? 0 {'new_name': 'lala'}
-undefined_var
+lala
# -------------------------------------------------- different-scopes
def x():
    #? 7 {'new_name': 'v'}
    some_var = 3
    some_var
def y():
    some_var = 3
    some_var
# ++++++++++++++++++++++++++++++++++++++++++++++++++
--- refactor/rename.py
+++ refactor/rename.py
@@ -1,7 +1,7 @@
 def x():
     #? 7 {'new_name': 'v'}
-    some_var = 3
-    some_var
+    v = 3
+    v
 def y():
     some_var = 3
     some_var
# -------------------------------------------------- keyword-param1
#? 22 {'new_name': 'lala'}
def mykeywordparam1(param1):
    str(param1)
mykeywordparam1(1)
mykeywordparam1(param1=3)
mykeywordparam1(x, param1=2)
# ++++++++++++++++++++++++++++++++++++++++++++++++++
--- refactor/rename.py
+++ refactor/rename.py
@@ -1,7 +1,7 @@
 #? 22 {'new_name': 'lala'}
-def mykeywordparam1(param1):
-    str(param1)
+def mykeywordparam1(lala):
+    str(lala)
 mykeywordparam1(1)
-mykeywordparam1(param1=3)
-mykeywordparam1(x, param1=2)
+mykeywordparam1(lala=3)
+mykeywordparam1(x, lala=2)
# -------------------------------------------------- keyword-param2
def mykeywordparam2(param1):
    str(param1)
mykeywordparam2(1)
mykeywordparam2(param1=3)
#? 22 {'new_name': 'lala'}
mykeywordparam2(x, param1=2)
# ++++++++++++++++++++++++++++++++++++++++++++++++++
--- refactor/rename.py
+++ refactor/rename.py
@@ -1,7 +1,7 @@
-def mykeywordparam2(param1):
-    str(param1)
+def mykeywordparam2(lala):
+    str(lala)
 mykeywordparam2(1)
-mykeywordparam2(param1=3)
+mykeywordparam2(lala=3)
 #? 22 {'new_name': 'lala'}
-mykeywordparam2(x, param1=2)
+mykeywordparam2(x, lala=2)
# -------------------------------------------------- import
from import_tree.some_mod import foobar
#? 0 {'new_name': 'renamed'}
foobar
# ++++++++++++++++++++++++++++++++++++++++++++++++++
--- refactor/import_tree/some_mod.py
+++ refactor/import_tree/some_mod.py
@@ -1,4 +1,4 @@
-foobar = 3
+renamed = 3
 
 inline_var = 5 + 3
--- refactor/rename.py
+++ refactor/rename.py
@@ -1,4 +1,4 @@
-from import_tree.some_mod import foobar
+from import_tree.some_mod import renamed
 #? 0 {'new_name': 'renamed'}
-foobar
+renamed
# -------------------------------------------------- module
from import_tree import some_mod
#? 0 {'new_name': 'renamedm'}
some_mod
# ++++++++++++++++++++++++++++++++++++++++++++++++++
rename from refactor/import_tree/some_mod.py
rename to refactor/import_tree/renamedm.py
--- refactor/rename.py
+++ refactor/rename.py
@@ -1,4 +1,4 @@
-from import_tree import some_mod
+from import_tree import renamedm
 #? 0 {'new_name': 'renamedm'}
-some_mod
+renamedm
# -------------------------------------------------- import-not-found
#? 20 {'new_name': 'lala'}
import undefined_import
haha( undefined_import)
# ++++++++++++++++++++++++++++++++++++++++++++++++++
--- refactor/rename.py
+++ refactor/rename.py
@@ -1,4 +1,4 @@
 #? 20 {'new_name': 'lala'}
-import undefined_import
-haha( undefined_import)
+import lala
+haha( lala)
# -------------------------------------------------- in-package-with-stub
#? 31 {'new_name': 'renamedm'}
from import_tree.pkgx import pkgx
# ++++++++++++++++++++++++++++++++++++++++++++++++++
--- refactor/import_tree/pkgx/__init__.py
+++ refactor/import_tree/pkgx/__init__.py
@@ -1,3 +1,3 @@
-def pkgx():
+def renamedm():
     pass
--- refactor/import_tree/pkgx/__init__.pyi
+++ refactor/import_tree/pkgx/__init__.pyi
@@ -1,2 +1,2 @@
-def pkgx() -> int: ...
+def renamedm() -> int: ...
--- refactor/import_tree/pkgx/mod.pyi
+++ refactor/import_tree/pkgx/mod.pyi
@@ -1,2 +1,2 @@
-from . import pkgx
+from . import renamedm
--- refactor/rename.py
+++ refactor/rename.py
@@ -1,3 +1,3 @@
 #? 31 {'new_name': 'renamedm'}
-from import_tree.pkgx import pkgx
+from import_tree.pkgx import renamedm
# -------------------------------------------------- package-with-stub
#? 18 {'new_name': 'renamedp'}
from import_tree.pkgx
# ++++++++++++++++++++++++++++++++++++++++++++++++++
rename from refactor/import_tree/pkgx
rename to refactor/import_tree/renamedp
--- refactor/import_tree/pkgx/mod2.py
+++ refactor/import_tree/renamedp/mod2.py
@@ -1,2 +1,2 @@
-from .. import pkgx
+from .. import renamedp
--- refactor/rename.py
+++ refactor/rename.py
@@ -1,3 +1,3 @@
 #? 18 {'new_name': 'renamedp'}
-from import_tree.pkgx
+from import_tree.renamedp
# -------------------------------------------------- weird-package-mix
if random_undefined_variable:
    from import_tree.pkgx import pkgx
else:
    from import_tree import pkgx
#? 4 {'new_name': 'rename'}
pkgx
# ++++++++++++++++++++++++++++++++++++++++++++++++++
rename from refactor/import_tree/pkgx
rename to refactor/import_tree/rename
--- refactor/import_tree/pkgx/__init__.py
+++ refactor/import_tree/rename/__init__.py
@@ -1,3 +1,3 @@
-def pkgx():
+def rename():
     pass
--- refactor/import_tree/pkgx/__init__.pyi
+++ refactor/import_tree/rename/__init__.pyi
@@ -1,2 +1,2 @@
-def pkgx() -> int: ...
+def rename() -> int: ...
--- refactor/import_tree/pkgx/mod.pyi
+++ refactor/import_tree/rename/mod.pyi
@@ -1,2 +1,2 @@
-from . import pkgx
+from . import rename
--- refactor/import_tree/pkgx/mod2.py
+++ refactor/import_tree/rename/mod2.py
@@ -1,2 +1,2 @@
-from .. import pkgx
+from .. import rename
--- refactor/rename.py
+++ refactor/rename.py
@@ -1,7 +1,7 @@
 if random_undefined_variable:
-    from import_tree.pkgx import pkgx
+    from import_tree.rename import rename
 else:
-    from import_tree import pkgx
+    from import_tree import rename
 #? 4 {'new_name': 'rename'}
-pkgx
+rename
