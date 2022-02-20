# `autodoc` Linking

Sphinx `autodoc` is great, especially with Napoleon for docstring styles.
Also, the `sphinx-autodoc-typehints` extension makes sense of your type hints.

But did you know the combination provides links from your type hint, to your class that implements it?
Let's take a look.

## Agenda

1. Note that Sphinx won't rebuild on `.py` changes.
2. Start with this repo, with just `sphinx.ext.napoleon`.
3. Run `sphinx-autobuild` and view `/autodoc_linking/api` in a browser.
4. Edit `conf.py` and enable `sphinx_autodoc_typehints`, look at results.
5. Comment out `Guardian` from `api.md` and show the result (no more linking.)
6. Point out the two `py:ref` cases:
   - In the narrative of `api.md`
   - In the docstring for `Player`, which overrides the generated title
7. Mention the Intersphinx implications.

```{toctree}
:maxdepth: 2
:caption: "Contents:"

api/index
```
