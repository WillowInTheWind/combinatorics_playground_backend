# # from tex2img import LatexCompiler
# # from tex2img import Latex2PNG
#
# def pdf():
#     renderer = LatexCompiler()
#     tex = r'''
#     \documentclass{article}
#     \usepackage{amsmath}
#     \begin{document}
#     This is a LaTeX document.
#     \[
#         \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
#     \]
#     \end{document}
#     '''
#     pdf_data = renderer.compile(tex)
#     with open('output.pdf', 'wb') as f:
#         f.write(pdf_data)
#
# def tikz_to_png(code):
#     #TODO: rendering code
#     return code
#
# def Validate_tikz(code):
#     #TODO: Actually validate
#     return True
#
#
#
# if __name__ == "__main__":
#     import tikz
#
#     pic = tikz.Picture('thick')
#
#     circle_size = 0.42
#     circle_pos = [(0, 0), (1, 0), (2, 0), (2, 1), (1, 2)]
#
#     with pic.path('draw') as draw:
#         draw.at(0 + 0j).grid_to(3 + 3j)
#
#     with pic.path('fill') as fill:
#         for pos in circle_pos:
#             fill.at(pos).circle(circle_size)
#
#     print(pic.make())