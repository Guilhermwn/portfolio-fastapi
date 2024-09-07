import htpy as h

def base(title:str, content:h.Element):
    return h.html(".dark", lang="en")[
        h.head[
            h.link(
                "#favicon",
                rel="icon",
                type="image/x-icon",
                href="/assets/favicon.ico",
            ),
            h.meta(charset="UTF-8"),
            h.meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            h.link(
                rel="stylesheet",
                href="https://unpkg.com/franken-ui-releases@0.0.13/dist/default.min.css",
            ),
            h.link(
                rel="stylesheet",
                type="text/css",
                href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css",
            ),
            h.script(src="https://cdn.tailwindcss.com"),
            h.title[f"Guilhermwn - { title }"],
        ],
        h.body[
            content,
            h.script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.5/dist/js/uikit.min.js"),
            h.script(
                src="https://cdn.jsdelivr.net/npm/uikit@3.21.5/dist/js/uikit-icons.min.js"
            ),
        ],
    ]

