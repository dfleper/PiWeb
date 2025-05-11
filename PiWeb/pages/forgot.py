import reflex as rx

def forgot_password() -> rx.Component:
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
                        "Forgot your password?",
                        size="6",
                        as_="h2",
                        text_align="center",
                        width="100%",
                    ),
                    rx.text(
                        "Enter your email and we'll send you a reset link.",
                        text_align="center",
                        opacity="0.8",
                        width="100%",
                    ),
                    direction="column",
                    spacing="5",
                    width="100%",
                ),
                rx.vstack(
                    rx.text("Email address", size="3", weight="medium", text_align="left", width="100%"),
                    rx.input(placeholder="user@email.com", type="email", size="3", width="100%"),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.button("Send Reset Link", size="3", width="100%"),
                rx.center(
                    rx.link("Back to Sign In", href="/", size="3"),
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
