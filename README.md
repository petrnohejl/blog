Jestřáblog
==========

Jestřáblog is my personal blog. It is powered by [Python](http://www.python.org/), [Pelican](http://getpelican.com), [Markdown](http://daringfireball.net/projects/markdown/) and [Jinja2](http://jinja.pocoo.org/). Blog is hosted on [GitHub Pages](http://pages.github.com/) as a static website and is available at [blog.petrnohejl.cz](http://blog.petrnohejl.cz).

Special thanks to [Honza](https://github.com/honzajavorek) for inspiration and discovering Pelican.


How to use
----------

Python dependencies:

- [Pelican](https://pypi.python.org/pypi/pelican/)
- [Markdown](https://pypi.python.org/pypi/Markdown)
- [MS Visual C++ Compiler for Python](http://aka.ms/vcpython27)
- [Fabric](https://pypi.python.org/pypi/Fabric)
- [GitHub Pages Import](https://pypi.python.org/pypi/ghp-import)

Use Fabric commands to build and publish Pelican blog:

```
fab build             Build website with development settings
fab build_production  Build website with production settings
fab clean             Clean output
fab commit_ghp        Build and deploy website to GitHub Pages
fab commit_master     Commit web sources to Git repo
fab new               Create new article template
fab publish           Push web sources, build and deploy website
fab rebuild           Clean and build
fab regenerate        Autoreloading building of website with development settings
fab reserve           Build and run server
fab serve             Run server
```

TLDR:

- Create a new article with `fab new`
- Check article preview locally with `fab reserve`
- Publish the article with `fab publish`
- Push master and gh-pages branches


Written by
----------

[Petr Nohejl](http://petrnohejl.cz)


License
-------

Copyright 2014 Petr Nohejl
