import plotly.express as px
import quantnote_template # Import your template here

# load demo data
from plotly.data import tips
df = tips()
df = df[['smoker', 'size', 'tip']].groupby(by=['smoker', 'size'], as_index=False).mean()

# Plot with the new template
fig = px.bar(df, x='size', y='tip', color='smoker',
             template='quantnote', title='Template Example')


fig.show()