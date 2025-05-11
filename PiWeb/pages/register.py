import reflex as rx

def signup_default() -> rx.Component:
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
                        "Create an account",
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
                    rx.text("Email address", size="3", weight="medium", text_align="left", width="100%"),
                    rx.input(placeholder="user@mail.com", type="email", size="3", width="100%"),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.text("Password", size="3", weight="medium", text_align="left", width="100%"),
                    rx.input(placeholder="Enter your password", type="password", size="3", width="100%"),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.box(
                    rx.checkbox(
                        "Agree to Terms and Conditions",
                        default_checked=True,
                        spacing="2",
                    ),
                    width="100%",
                ),
                rx.button("Register", size="3", width="100%"),
                rx.center(
                    rx.text("Already registered?", size="3"),
                    rx.link("Sign in", href="/", size="3"), 
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