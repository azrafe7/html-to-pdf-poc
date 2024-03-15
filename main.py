from jinja2 import Environment, PackageLoader, select_autoescape
from jinja2.loaders import FileSystemLoader

import pdfkit


def render_template():
    env = Environment(
        loader=PackageLoader("main"),
        autoescape=select_autoescape()
    )

    template = env.get_template("base.html")

    text = "Generated executive summary of results, key themes and trends and impact score compared to the previous period"

    # jslink = url_for('static/login_auth', filename='index.js')

    genString = template.render(
        businessName="Mr Wong",
        startDate="March 1, 2024",
        endDate="March 30, 2024",
        summaryText=text,
    )

    # Open a file in write mode (w)
    with open("out/gen.html", "w") as file:
        # Write the string to the file
        file.write(genString)
        print("rendered")

        with open('out/gen.html') as f:
            # pdfkit.from_file(
            #     f, 'out/gen.pdf', css='/Users/joshheslin/Development/cloutly/pdf-templates/templates/tailwind.css')
            # options = {
            #     'user-style-sheet': ""
            # }

            # r = pdfkit.PDFKit('html', 'string', verbose=True)
            # print(' '.join(r.command()))
            options = {'enable-local-file-access': None}

            pdfkit.from_string(
                genString, 'out/gen.pdf', options=options)

            # output = r.to_pdf()

            print("pdf generated")


if __name__ == "__main__":
    render_template()
