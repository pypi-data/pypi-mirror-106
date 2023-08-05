# from wordcloud import WordCloud
# import PIL
# import re
# import matplotlib.pyplot as plt
# import plotly.graph_objects as go
# import plotly.io as pio
# import plotly.express as px
# import numpy as np
# from wrapplotly.util import as_list

# wc = WordCloud(font_path = '/Library/Fonts/Microsoft/Arial.ttf', 
#                prefer_horizontal = 0.2, random_state=89860,
#                width = 800, height = 400).generate_from_frequencies({'hi':5, 'lo': 1, 'medium':3})
# plt.imshow(wc)
# plt.show()

# with open('test.svg', 'w') as fp:
#     fp.write(wc.to_svg())

# wc_svg = wc.to_svg(embed_image=True)
# for x in wc_svg.split('\n'):
#     if re.search('^<image', x):
#         src = x.split('href=')[-1][:-2]

# go.Figure(go.Image(source = src)).show()

# from io import BytesIO
# pil_img = wc.to_image() # PIL image object
# prefix = "data:image/png;base64,"
# with BytesIO() as stream:
#     pil_img.save(stream, format="png")
#     base64_string = prefix + base64.b64encode(stream.getvalue()).decode("utf-8")
# fig = go.Figure(go.Image(source=base64_string))
# fig.show()

# dir(plt.imshow(wc))
# [w for w in dir(plt.imshow(wc).axes) if 'lim' in w]
# plt.imshow(wc).axes.get_xlim()
# plt.imshow(wc).axes.get_ylim()

# for item in wc.layout_:
#     print(item)

# unnested = [dict(text = text, freq = freq, fontsize = fontsize, x = col, y = row, orientation = orientation, color = color)
#             for (text, freq), fontsize, (row, col), orientation, color in wc.layout_]

# font_obj = PIL.ImageFont.truetype(wc.font_path, 16)
# font_family = as_list(font_obj.getname())[0]
# font_obj.getsize('hi')

# #f = PIL.ImageFont.truetype(wc.font_path)
# #f.getname() #('Droid Sans Mono', 'Regular')

# calculate_centers = True
# # default for now is False
# calculate_centers = False if calculate_centers is None else calculate_centers

# box_factor = 1
# fig = go.Figure()
# fig = fig.add_trace(go.Image(z = wc.to_array(), hoverinfo = 'none'))
# # fig = fig.add_layout_image(dict(
# #         x=0,
# #         sizex=wc.width,
# #         y=0,
# #         sizey=wc.height,
# #         xref="x",
# #         yref="y",
# #         opacity=1.0,
# #         layer="below",
# #         sizing="stretch",
# #         source=wc.to_image()))

# for word in unnested[:3]:
#     if word['orientation'] is None:
#         textangle = 0
#     else:
#         textangle = 270
   
#     # create font object
#     font = PIL.ImageFont.truetype(wc.font_path, word['fontsize'])
#     # transpose font object
#     transposed_font = PIL.ImageFont.TransposedFont(font, orientation=word['orientation'])
#     img_grey = PIL.Image.new("L", (400, 400))
#     draw = PIL.ImageDraw.Draw(img_grey)
#     box_size = draw.textsize(word['text'], font=transposed_font)
#     #
#     x0 = word['x']
#     x1 = x0 + (box_size[0] * box_factor) + wc.margin
#     y0 = word['y']
#     y1 = y0 + (box_size[1] * box_factor) + wc.margin
        
#     hovertext = ('<b>Word:</b> {}<br><b>Relative Frequency:</b> {}'
#                  .format(word['text'], word['freq']))
#     hoverlabel = dict(bgcolor = word['color'],
#                       bordercolor = wc.background_color,
#                       font_family = font_family+', sans-serif',
#                       font_color = wc.background_color,
#                       font_size = 16)

#     fig = fig.add_trace(go.Scatter(x = [x0,x1,x1,x0,x0], y = np.array([y0, y0, y1, y1, y0]) -1, # -1 when using go.Image
#                                    fill = 'toself', 
#                                    text = hovertext, name = '', 
#                                    hoveron = 'fills', opacity = 0.5,
#                                    hoverlabel = hoverlabel))

# x_max = wc.width
# y_max = wc.height
# fig = fig.update_layout(yaxis_showgrid = not False, xaxis_showgrid = not False, 
#                         yaxis_zeroline = False, xaxis_zeroline = False,
#                         yaxis_range = [wc.height,0], yaxis_constrain = 'domain',
#                         yaxis_scaleanchor = 'x', yaxis_scaleratio = 1,
#                         xaxis_range = [0,wc.width], xaxis_constrain = 'domain',
#                         plot_bgcolor = wc.background_color,
#                         #paper_bgcolor = wc.background_color
#                         xaxis_showticklabels = not False,
#                         yaxis_showticklabels = not False,
#                         showlegend = False)
# fig.show()

# dir(font.font)

# s
# [attr for attr in dir(wc) if re.search('_$', attr) is not None]
# wc.layout_
# wc.words_

# # create image
# import PIL
# img_grey = PIL.Image.new("L", (400, 400))
# draw = PIL.ImageDraw.Draw(img_grey)
# draw.text((0,0), 'medium', fill = 'white', font = font_obj)
# plt.imshow(img_grey)
# plt.show()
# img_grey.show()
# draw.textsize('MEDIUM', font = font_obj)

# # finding plotted size of image (grey scale)
# font_obj = PIL.ImageFont.truetype(wc.font_path, 48)
# transposed_font_obj = PIL.ImageFont.TransposedFont(font_obj, PIL.Image.ROTATE_90)
# # a) exactly
# img_grey = PIL.Image.new("L", (400, 400))
# draw = PIL.ImageDraw.Draw(img_grey)
# draw.text((0,0), 'medium', fill = 'white', font = font_obj)
# #plt.imshow(img_grey)
# #plt.show()
# img_array = np.asarray(img_grey)
# max_px_per_col = img_array.max(axis = 0)
# x0 = np.argmax((np.cumsum(max_px_per_col) != 0)) # first non-zero column
# x1 = np.argmax(np.cumsum(max_px_per_col)) # last non-zero column
# max_px_per_row = img_array.max(axis = 1)
# y0 = np.argmax((np.cumsum(max_px_per_row) != 0)) # first non-zero row
# y1 = np.argmax(np.cumsum(max_px_per_row)) # last non-zero column
# box_width = x1 - x0 
# box_width # 165
# box_height = y1 - y0
# box_height # 34
# # b) estimated using draw.textsize
# img_grey = PIL.Image.new("L", (400, 400))
# draw = PIL.ImageDraw.Draw(img_grey)
# box_width, box_height = draw.textsize('medium', font = font_obj)
# box_width # 172
# box_height # 44
# # same result as:
# # font_obj.getsize('medium')

# # finding plotted size of image (bw)
# font_obj = PIL.ImageFont.truetype(wc.font_path, 380)
# transposed_font_obj = PIL.ImageFont.TransposedFont(font_obj, PIL.Image.ROTATE_90)
# # a) exactly
# img_bw = PIL.Image.new("1", (400, 400))
# draw = PIL.ImageDraw.Draw(img_bw)
# draw.text((0,0), 'medium', fill = 'white', font = font_obj)
# img_bw.show()
# #plt.imshow(img_grey)
# #plt.show()
# img_array = np.asarray(img_grey)
# max_px_per_col = img_array.max(axis = 0)
# x0 = np.argmax((np.cumsum(max_px_per_col) != 0)) # first non-zero column
# x1 = np.argmax(np.cumsum(max_px_per_col)) # last non-zero column
# max_px_per_row = img_array.max(axis = 1)
# y0 = np.argmax((np.cumsum(max_px_per_row) != 0)) # first non-zero row
# y1 = np.argmax(np.cumsum(max_px_per_row)) # last non-zero column
# box_width = x1 - x0 
# box_width # 165
# box_height = y1 - y0
# box_height # 34
# # b) estimated using draw.textsize
# img_grey = PIL.Image.new("L", (400, 400))
# draw = PIL.ImageDraw.Draw(img_grey)
# box_width, box_height = draw.textsize('medium', font = font_obj)
# box_width # 172
# box_height # 44
# # same result as:
# # font_obj.getsize('medium')


# img_array.max(axis = 1) # max of every row


# font_sizes, positions, orientations, colors = [], [], [], []
# #
# font_obj = PIL.ImageFont.truetype(wc.font_path, 48)
# transposed_font_obj = PIL.ImageFont.TransposedFont(font_obj, PIL.Image.ROTATE_90)
# draw.text((100,100), 'medium', fill = 'white', font = font_obj)
# dir(draw)
# #
# font_obj = PIL.ImageFont.truetype(wc.font_path, 48)
# transposed_font_obj = PIL.ImageFont.TransposedFont(font_obj, PIL.Image.ROTATE_90)
# draw.text((100,100), 'medium', fill = 'white', font = font_obj)
# draw.text((100,300), 'medium', fill = 'white', font = font_obj)
# img_grey.show()



# dir(img_grey)

# draw.textsize('medium', font=font_obj)
# draw.textsize('medium', font=transposed_font_obj)

# font_obj.getsize('medium')
# np.array(font_obj.getsize('medium')) + wc.margin // 2

# word = unnested[1]
# wc.background_color
# PIL.ImageColor.getrgb(wc.background_color)
# a = wc.to_array()[0:5, 0:5,:]

# b = np.array([[[0,0,0],
#                [1,0,0],
#                [0,0,0]]])

# b == (0,0,0)

# type(PIL.Image.ROTATE_180)

# a = np.diag(np.arange(6))
# np.cumsum(a, axis = 1)
# np.cumsum(np.cumsum(1 * a, axis=1),axis=0).astype(np.uint32)