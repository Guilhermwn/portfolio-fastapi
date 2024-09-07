import htpy as h
from pathlib import Path
from .base import base

def presentation_section():
    return h.section(
    class_="min-h-screen uk-section uk-flex uk-flex-center uk-flex-middle uk-flex-column bg-[#09090b]"
)[
    h.div(".uk-flex.uk-flex-row.uk-flex-center.gap-5.m-5")[
        h.blockquote('.text-white.uk-blockquote')['I was an ordinary person with ordinary skills. But even so, this didn\'t mean I could only do ordinary things.']
        # (h.a(
        #     class_="uk-button uk-button-text text-base text-white px-6 py-2 hover:bg-[#e4e5e9] hover:text-black",
        #     href="#",
        # )[f"{ name }"] for name in ['Links', 'Projetos', 'Sobre']),
    ],
    h.hr(".uk-divider-icon.w-2/3.mb-5.sm:w-1/2"),
    h.div(".uk-container.uk-flex.uk-flex-center.uk-flex-middle.uk-flex-wrap.gap-5")[
        h.div("#introduction-text")[h.h1(".uk-h1.text-white")["Guilherme Franco"]],
        h.div("#introduction-image")[
            h.img(
                ".w-36",
                src="assets/img/guilhermwn-light.png",
                alt="",
            )
        ],
    ],
]


def about_section():
    return h.section(
        class_="uk-section uk-width-1-1 uk-flex uk-flex-center uk-flex-middle bg-[#e4e5e9]"
    )[
        h.div(".uk-container.uk-width-large.uk-width-xlarge@s")[
            h.div(".uk-card")[
                h.div(".uk-card-header.uk-flex.uk-flex-center")[
                    h.img(
                        ".uk-card-media-top.rounded-full.w-32.h-32.object-cover",
                        src="assets/img/master.png",
                    )
                ],
                h.div(".uk-card-body")[
                    h.div(".uk-blockquote")[
                        h.h3(".uk-card-title.uk-h3")["Sobre mim"],
                        h.p(".uk-paragraph")[
                            "Meu nome é Guilherme, curso Engenharia Eletrônica na Universidade Federal de Sergipe. Trabalho com Python há 3 anos e já desenvolvi alguns projetos de script e interface."
                        ],
                    ],
                    h.hr(".uk-divider-icon.my-7"),
                    h.div(".uk-flex.uk-flex-center.uk-flex-middle.gap-8")[
                        h.i(".devicon-python-plain", style="font-size: 45px"),
                        h.i(".devicon-c-plain", style="font-size: 45px"),
                        h.i(".devicon-html5-plain", style="font-size: 45px"),
                        h.i(".devicon-latex-original", style="font-size: 45px"),
                    ],
                ],
            ]
        ]
    ]


def project_card(link:str, img:Path, title: str, description: str):
    return h.div[
        h.a(".uk-link-toggle", href=link)[
            h.div(".uk-card.uk-card-default.uk-link-text")[
                h.div(".uk-card-media-top.p-2")[
                    h.img(".rounded-lg", src=img, alt="")
                ],
                h.div(".uk-card-body")[
                    h.h3(".uk-h3")[title],
                    h.hr(".uk-divider-small.mt-5"),
                    h.p(".uk-paragraph")[description],
                ],
            ]
        ]
    ]


def projects_section():
    return [
        h.section(class_="uk-section bg-[#09090b]")[
            h.div(".uk-container")[
                h.div(".uk-flex.uk-flex-center")[h.h2(".uk-h2.text-white")["Projetos"]],
                h.hr(".uk-divider-icon.my-8"),
                # h.div(".uk-child-width-expand@s.uk-text-center", uk_grid=True)[
                h.div(".uk-child-width-expand@s.uk-text-center.uk-grid-small", uk_grid=True)[
                    project_card(link='https://github.com/Guilhermwn/Portfolio_HTML/tree/main/Website%20-%20Takhyon%20Helps',
                                img='assets/img/projetos/takhyon-helps.png', 
                                title='Tackhyon Helps', 
                                description='Website de apresentação e documentação para um bot do Discord'),
                    project_card(link='https://scicalcs.onrender.com',
                                img='assets/img/projetos/scicalcs-nicegui.png', 
                                title='SciCalcs',  
                                description='Website de auxílio estudantil construído usando Python e NiceGUI'),
                    project_card(link='https://github.com/Guilhermwn/embedded-utils/',
                                img='assets/img/projetos/embedded-utils.png', 
                                title='Embedded Utils', 
                                description='Ferramenta CLI de utilidades para programação embarcada'),
                ],
            ]
        ],
    ]


def homepage():
    return base(
        title='Homepage',
        content=[
            presentation_section(),
            about_section(),
            projects_section(),
        ]
    )