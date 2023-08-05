from wordcloud import WordCloud
import PIL
import plotly.graph_objects as go
import numpy as np
import re
import requests
from bs4 import BeautifulSoup
from matplotlib.colors import ListedColormap
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction._stop_words import ENGLISH_STOP_WORDS

# workaround for interactive vs CLI usage
if ('__file__' in dir()) and (__name__ == '__main__'):
    from plot_wordcloud import plot_wordcloud
else:
    from wrapplotly import plot_wordcloud

url = 'https://en.wikipedia.org/wiki/Grenada'
req = requests.get(url)
# available parsers: 'html.parser','lxml','html5lib'
soup = BeautifulSoup(req.text, 'lxml')

vectorizer = CountVectorizer().fit([soup.get_text()])
counts = vectorizer.transform([soup.get_text()])

short_english_stopwords = [w for w in ENGLISH_STOP_WORDS if len(w) <= 3]
digit_words = [w for w in vectorizer.get_feature_names() if re.match('^\d{1,3}$', w) is not None]
manually_added = ['edit','retrieved','from','with','identifierswikipedia','articles',
                  'citation']

counts_dict = {k: v for k, v in zip(vectorizer.get_feature_names(), counts.toarray()[0])
                if k not in (set(short_english_stopwords)|set(digit_words)|set(manually_added))}

rgb = np.asarray([(191,45,47),(50,120,96),(246,209,75),(255,255,255)]) # last colour is white
cmap = ListedColormap(rgb[:3] / 255 ,name = 'grenada')
wc = WordCloud(font_path = '/Library/Fonts/Microsoft/Arial.ttf', 
               colormap = cmap, mode = 'RGB', prefer_horizontal = 0.2, 
               random_state=89860,min_font_size=8, max_words=100, background_color='black',
               width = 800, height = 400).generate_from_frequencies(counts_dict)

fig = plot_wordcloud(wc)
fig = fig.update_layout(title = 'Top 100 Words on English Wikipedia Page for "Grenada" 🇬🇩',
                        title_font_size = 60, title_font_color = 'black',
                        title_font_family = 'arial',
                        #margin = dict(l = 80, r = 80, t = 120, b = 80)
                        )

fig = fig.add_annotation(text = '<i>By Jillian Augustine, PhD. (@jill_codes)</i>',
                         x = 0.975, y = 0, xref = 'paper', yref = 'paper', 
                         xanchor = 'right', yanchor = 'top', yshift = 0, 
                         showarrow = False, font_size = 48, font_color = 'black',
                         font_family = 'arial',
                         align = 'right')
fig.show()

(fig.update_annotations(font_size = 16)
    .update_layout(title_font_size = 20)
    .update_traces(hoverlabel_font_size = 16, selector = dict(type = 'scatter'))
    .write_html('eg.html'))