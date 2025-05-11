import reflex as rx
from rxconfig import config
from PiWeb.pages import register

class State(rx.State):
    """The app state."""
    ...

def login_default() -> rx.Component:
    return rx.center( 
        rx.card(
            rx.vstack(
                rx.center(
                    rx.image(
                        src="/logo.png",
                        width="7em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Sign in to your account",
                        size="6",
                        as_="h2",
                        text_align="center",
                        width="100%",
                    ),
                    direction="column",
                    spacing="5",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Email address",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="user@email.com",
                        type="email",
                        size="3",
                        width="100%",
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            "Password",
                            size="3",
                            weight="medium",
                        ),
                        rx.link(
                            "Forgot password?",
                            href="#",
                            size="3",
                        ),
                        justify="between",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Enter your password",
                        type="password",
                        size="3",
                        width="100%",
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.button("Sign in", size="3", width="100%"),
                rx.center(
                    rx.text("New here?", size="3"),
                    rx.link("Sign up", href="/register", size="3"),
                    opacity="0.8",
                    spacing="2",
                    direction="row",
                ),
                spacing="6",
                width="100%",
            ),
            size="4",
            max_width="28em",
            width="100%",
        ),
        height="100vh", 
        width="100vw",  
    )

app = rx.App()
app.add_page(login_default, route="/", title="Login | Piweb")
app.add_page(register.signup_default, route="/register", title="Register | PiWeb")

