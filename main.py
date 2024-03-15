from jinja2 import Environment, PackageLoader, select_autoescape
import pdfkit


def render_template():
    env = Environment(
        loader=PackageLoader("main"),
        autoescape=select_autoescape()
    )

    template = env.get_template("base2.html")

    genString = template.render(
        businessName="Mr Wong",
        go="here"
    )

    # Open a file in write mode (w)
    with open("out/gen.html", "w") as file:
        # Write the string to the file
        file.write(genString)
        print("rendered")

        with open('out/gen.html') as f:
            pdfkit.from_string(genString, 'out/gen.pdf')
            print("pdf generated")


if __name__ == "__main__":
    render_template()
