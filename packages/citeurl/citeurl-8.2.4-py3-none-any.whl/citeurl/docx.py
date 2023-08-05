from docx import Document

#            hyperlink_docx(
#                input_file=args.input,
#                output_file=args.output,
#                citations=citator.list_citations(text),
#                link_detailed_ids=False if args.link_ids == 'none' else True,
#                link_plain_ids=True if args.link_ids == 'all' else False
#            )

def read_docx(filename: str):
    "get a string with the visible text of the given docx file"
    doc = Document(docx=filename)
    paragraph_texts = [p.text for p in doc.paragraphs]
    return '\n\n'.join(paragraph_texts)

def hyperlink_docx(
    input_file: str,
    output_file: str,
    citations: list,
    link_detailed_ids: bool=True,
    link_plain_ids: bool=False,
):
    print("didn't do anything")
