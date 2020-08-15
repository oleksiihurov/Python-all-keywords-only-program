"""
Python all keywords only program
https://docs.python.org/3/reference/lexical_analysis.html#keywords

from import as
class def lambda
async await
global nonlocal del
try except finally
if elif else
for while with
pass continue break
not and or in is
None False True
return yield raise assert
"""


class foo:
    global _
    async def bar():
        def baz():
            nonlocal _
            del _
        try:
            if lambda: True:
                for _ in True and True:
                    continue
            elif False is False:
                while False or False:
                    break
            else:
                with not None:
                    pass
            yield
        except:
            assert await bar()
            raise
        finally:
            from keyword import kwlist as kwlist
            return
