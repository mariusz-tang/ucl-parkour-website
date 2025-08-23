from staticjinja import Site


if __name__ == "__main__":
    site = Site.make_site(
        outpath="./build/",
        staticpaths=["./css/", "./img/", "./fonts/"]
    )
    site.render(use_reloader=True)
