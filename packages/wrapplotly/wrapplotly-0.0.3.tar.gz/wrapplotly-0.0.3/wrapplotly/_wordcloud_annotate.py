# from wordcloud import WordCloud
# import PIL
# import re
# import matplotlib.pyplot as plt
# import plotly.graph_objects as go
# import plotly.io as pio
# import numpy as np
# from wrapplotly.util import as_list
# wc = WordCloud(font_path = '/Library/Fonts/Microsoft/Arial.ttf', 
#                prefer_horizontal = 0.2, 
#                random_state=89860).generate_from_frequencies({'hi':5, 'lo': 1, 'medium':3})
# plt.imshow(wc)
# plt.show()
# dir(plt.imshow(wc))
# [w for w in dir(plt.imshow(wc).axes) if 'lim' in w]
# plt.imshow(wc).axes.get_xlim()
# plt.imshow(wc).axes.get_ylim()

# for item in wc.layout_:
#     print(item)

# unnested = [dict(text = t, freq = f, fontsize = fs, x = x, y = y, orientation = o, col = c)
#             for (t, f), fs, (y, x), o, c in wc.layout_]
# # note the swapping of x and y

# font_family = as_list(PIL.ImageFont.truetype(wc.font_path).getname())[0]
# #f = PIL.ImageFont.truetype(wc.font_path)
# #f.getname() #('Droid Sans Mono', 'Regular')

# fig = go.Figure()
# for word in unnested[:]:
#     if word['orientation'] is None:
#         textangle = 0
#     elif word['orientation'] == 2:
#         textangle = 270

#     #text = word['text']
#     #xanchor = 'left'
#     #yanchor = 'top' # might change if we flip the y-axis
#     #showarrow = False

#     font = dict(size = word['fontsize'] * 1,
#                 color = word['col'],
#                 family = font_family+', sans-serif')
#     hovertext = ('<b>Word:</b> {}<br><b>Relative Frequency:</b> {}'
#                  .format(word['text'], word['freq']))
#     hoverlabel = dict(bgcolor = word['col'],
#                       bordercolor = word['col'],
#                       font_family = font_family+', sans-serif',
#                       font_color = wc.background_color
#                       )
#     fig = fig.add_annotation(text = word['text'],
#                        x = word['x'],
#                        y = word['y'],
#                        borderpad = wc.margin,
#                        textangle = textangle,
#                        font = font,
#                        hovertext = hovertext,
#                        hoverlabel = hoverlabel,
#                        xanchor = 'left',
#                        yanchor = 'top',
#                        showarrow = False)

# x_max = wc.width
# y_max = wc.height
# fig = fig.update_layout(yaxis_showgrid = False, xaxis_showgrid = False, 
#                         yaxis_zeroline = False, xaxis_zeroline = False,
#                         yaxis_range = [wc.height,0], yaxis_constrain = 'domain',
#                         yaxis_scaleanchor = 'x', yaxis_scaleratio = 1,
#                         xaxis_range = [0,wc.width], xaxis_constrain = 'domain',
#                         plot_bgcolor = wc.background_color,
#                         #paper_bgcolor = wc.background_color
#                         margin={"l": 0, "r": 0, "t": 0, "b": 0},
#                         width = wc.width, height = wc.height,
#                         xaxis_showticklabels = False,
#                         yaxis_showticklabels = False
#                         )
# #fig.show()
# fig.write_image('eg.png', scale = 1)

# img_obj = PIL.Image.open('eg.png')
# img_obj.show()
# fig = go.Figure().update_layout(yaxis_range = [wc.height,0], yaxis_constrain = 'domain',
#                         yaxis_scaleanchor = 'x', yaxis_scaleratio = 1,
#                         xaxis_range = [0,wc.width], xaxis_constrain = 'domain',)
# fig = fig.add_layout_image(
#         x=0,
#         sizex=img_obj.width,
#         y=0,
#         sizey=img_obj.height,
#         xref="x",
#         yref="y",
#         opacity=1.0,
#         layer="below",
#         source=wc.to_image()
# )

# fig.show()


# go.Figure(go.Image(source = img_obj)).show()


# [attr for attr in dir(wc) if re.search('_$', attr) is not None]
# wc.layout_
# wc.words_