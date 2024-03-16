from jinja2 import Environment, PackageLoader, select_autoescape
from jinja2.loaders import FileSystemLoader
from playwright.sync_api import ViewportSize, sync_playwright

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

    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

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
                genString, 'out/gen.pdf', options=options, configuration=config)

            # output = r.to_pdf()

            print("pdf generated")


    with sync_playwright() as p:

        headless_browser = True
        print("Launching " + ("Headless " if headless_browser else "") + "Browser...")

        browser = p.chromium.launch(headless=headless_browser)
        ua = "Mozilla/5.0 (Linux; Android 8.0.0; MI 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36"
        context = browser.new_context(user_agent=ua)
        page = context.new_page()
        page.set_content(genString)
        
        # breakpoint()
        
        page.emulate_media(media="screen")
        pw_pdf_file = "out/gen_pw.pdf"
        page.pdf(path=pw_pdf_file, print_background=True, format="A4", scale=0.6)
        print(f"{pw_pdf_file} generated")

if __name__ == "__main__":
    render_template()
