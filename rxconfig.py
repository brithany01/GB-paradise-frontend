import reflex as rx

config = rx.Config(
    app_name="GB_Paradise_Frontend",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)