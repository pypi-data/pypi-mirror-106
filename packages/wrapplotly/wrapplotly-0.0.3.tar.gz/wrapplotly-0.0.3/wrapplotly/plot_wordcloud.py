from wordcloud import WordCloud
import PIL
import plotly.graph_objects as go
import numpy as np
# workaround for interactive vs CLI usage
if '__file__' in dir():
    from util import as_list
else:
    from wrapplotly.util import as_list

def plot_wordcloud(wc, hovertextsize = 32, **kwargs):
    '''
    Plots a wordcloud object.
    
    Parameters
    ----------
    wc: wordcloud.wordcloud.WordCloud object
    hovertextsize: int
        Size of the hovertext
    **kwargs: keyword arguments passed onto fig.update_layout()
    '''
    width = wc.width
    height = wc.height
    font_family = as_list(PIL.ImageFont.truetype(wc.font_path).getname())[0]
    fig = go.Figure().add_layout_image(dict(
            x=0,
            sizex=width,
            y=0,
            sizey=height,
            xref="x",
            yref="y",
            opacity=1.0,
            layer="below",
            sizing="stretch", # has no effect because size of image is size of entire fig below
            source=wc.to_image()))

    unnested_layout = [
        dict(text = text, freq = freq, fontsize = fontsize, x = col, y = row, 
             orientation = orientation, color = color)
            for (text, freq), fontsize, (row, col), orientation, color in wc.layout_]

    for word in unnested_layout:
        # create font object
        font = PIL.ImageFont.truetype(wc.font_path, word['fontsize'])
        # transpose font object
        transposed_font = PIL.ImageFont.TransposedFont(font, orientation=word['orientation'])
        # creating image
        img_grey = PIL.Image.new("L", (height, width))
        draw = PIL.ImageDraw.Draw(img_grey)
        # calculate box size
        box_width, box_height = draw.textsize(word['text'], font=transposed_font)
        x0 = word['x']
        x1 = x0 + box_width + wc.margin
        y0 = word['y']
        y1 = y0 + box_height + wc.margin

        hovertext = ('<b>Word:</b> {}<br><b>Relative Frequency:</b> {:.3f}'
                    .format(word['text'], word['freq']))
        hoverlabel = dict(bgcolor = word['color'],
                        bordercolor = wc.background_color,
                        font_family = font_family+', sans-serif',
                        font_color = wc.background_color,
                        font_size = hovertextsize)
        # add filled transparent boxes with non-transparent hovering
        fig = fig.add_trace(go.Scatter(x = [x0,x1,x1,x0,x0], y = np.array([y0, y0, y1, y1, y0]) -1, # -1 when using go.Image
                                    fill = 'toself',
                                    text = hovertext, name = '', 
                                    hoveron = 'fills', opacity = 0.0,
                                    hoverlabel = hoverlabel))

    fig = fig.update_layout(yaxis_showgrid = False, xaxis_showgrid = False, 
                            yaxis_zeroline = False, xaxis_zeroline = False,
                            yaxis_range = [height,0], yaxis_constrain = 'domain',
                            yaxis_scaleanchor = 'x', yaxis_scaleratio = 1,
                            xaxis_range = [0,width], xaxis_constrain = 'domain',
                            plot_bgcolor = wc.background_color,
                            xaxis_showticklabels = False,
                            yaxis_showticklabels = False,
                            showlegend = False)
    return fig.update_layout(**kwargs)

# example below -------------

# import re
# import requests
# from bs4 import BeautifulSoup
# from matplotlib.colors import ListedColormap
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction._stop_words import ENGLISH_STOP_WORDS

# url = 'https://en.wikipedia.org/wiki/Grenada'
# req = requests.get(url)
# # available parsers: 'html.parser','lxml','html5lib'
# soup = BeautifulSoup(req.text, 'lxml')

# vectorizer = CountVectorizer().fit([soup.get_text()])
# counts = vectorizer.transform([soup.get_text()])

# short_english_stopwords = [w for w in ENGLISH_STOP_WORDS if len(w) <= ]
# digit_words = [w for w in vectorizer.get_feature_names() if re.match('^\d{1,3}$', w) is not None]
# manually_added = ['edit','retrieved','from','with','identifierswikipedia','articles']

# counts_dict = {k: v for k, v in zip(vectorizer.get_feature_names(), counts.toarray()[0])
#                 if k not in (set(short_english_stopwords)|set(digit_words)|set(manually_added))}

# rgb = np.asarray([(191,45,47),(50,120,96),(246,209,75),(255,255,255)]) # last colour is white
# cmap = ListedColormap(rgb[:3] / 255 ,name = 'grenada')
# wc = WordCloud(font_path = '/Library/Fonts/Microsoft/Arial.ttf', 
#                colormap = cmap, mode = 'RGB', prefer_horizontal = 0.2, 
#                random_state=89860,min_font_size=8, max_words=100, background_color='black',
#                width = 800, height = 400).generate_from_frequencies(counts_dict)

# fig = plot_wordcloud(wc)
# fig = fig.update_layout(title = 'Top 100 Words on English Wikipedia Page for "Grenada" 🇬🇩',
#                         title_font_size = 60, title_font_color = 'black',
#                         title_font_family = 'arial',
#                         #margin = dict(l = 80, r = 80, t = 120, b = 80)
#                         )

# fig = fig.add_annotation(text = '<i>By Jillian Augustine, PhD. (@jill_codes)</i>',
#                          x = 0.975, y = 0, xref = 'paper', yref = 'paper', 
#                          xanchor = 'right', yanchor = 'top', yshift = 0, 
#                          showarrow = False, font_size = 48, font_color = 'black',
#                          font_family = 'arial',
#                          align = 'right')
# # fig.show()
# # update for png
# (fig.update_annotations(font_size = 16)
#     .update_layout(title_font_size = 20)
#     .write_image('eg.png'))
# # update for html
# (fig.update_annotations(font_size = 16)
#     .update_layout(title_font_size = 20)
#     .update_traces(hoverlabel_font_size = 16, selector = dict(type = 'scatter'))
#     .write_html('eg.html'))