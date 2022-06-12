import streamlit as st
st.set_page_config(page_title="Churn Dashboard",
                   page_icon=":bar_chart:", layout="wide")

import pandas as pd

import seaborn as sns
sns.set(style="darkgrid")

import plotly.express as px

st.markdown("<h1 style='text-align: center; color: yellow;'><span> 📊 </span>Dashboard</h1>",
            unsafe_allow_html=True)



df = pd.read_csv('Kickstarter1.csv')
# %%
df = df.drop(['Unnamed: 7'] , axis=1)

# %%


# %%
categorical = ['name' , 'category' , 'status']
numeric = ['goal' , 'pledged' , 'backers']

# %%


# %%


# %%
df1 = df.dropna()

# %%
df1=df1[df1['deadline ']!='GBP']
df1=df1[df1['deadline ']!='CAD']
df1=df1[df1['deadline ']!='USD']

# %%
df1['deadline_year'] = pd.DatetimeIndex(df1['deadline ']).year

# %%
df1 = df1[df1.status!='undefined']
# %%
df1['id'] = df1.index


# %%
category  = ['Hardware', 'Gadgets', 'Web', 'Apps', 'Technology', 'Software',
       'Flight', 'Makerspaces', 'Fabrication Tools', 'Sound',
       'DIY Electronics', 'Camera Equipment', '3D Printing', 'Wearables',
       'Space Exploration', 'Robots']

year = [2015, 2016, 2012, 2011, 2014, 2013, 2017, 2010, 2009]

status = ['failed', 'canceled', 'successful', 'live', 'suspended']

# %%
df2 = pd.DataFrame(columns = year , index = category)

# %%
df3 = df1.groupby(['deadline_year','category ']).count().reset_index()

# %%
df3['count'] = df3['id']

# %%
df3 = df3.drop(['name ', 'deadline ', 'goal ', 'pledged ',
       'status', 'backers ', 'id'] , axis=1)


# %%
fig1 = px.line(df3, 
              x="deadline_year" ,
              y='count',
              color='category ',
              markers=True,
              title="Change in categories over ther years",
              labels={
                     "deadline_year": "Year",
                     "count": "Count",
                     "category ": "Category"
                 },
              )
fig1.update_layout(
        xaxis=dict(tickmode="linear"),
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False)),)

st.plotly_chart(fig1, use_container_width=True)

# %%
df5 = df1.drop(['name ', 'deadline ', 'goal ', 'pledged ',
       'backers '] , axis=1)

# %%
df6 = pd.DataFrame(columns= ['year' , 'category' , 'success rate'])

year.sort()

# %%
year.sort()

# %%
year. reverse()


g1 = df5.groupby('deadline_year')
for y in year:
    if(y in g1.groups.keys()):
        g2 = g1.get_group(y).groupby('category ')
        for c in category:
            if(c in g2.groups.keys()):

                g3 = g2.get_group(c).groupby('status')
                successful = g3.get_group('successful').count().id if ('successful' in g3.groups.keys()) else 0
                canceled = g3.get_group('canceled').count().id if ('canceled' in g3.groups.keys()) else 0
                failed = g3.get_group('failed').count().id if ('failed' in g3.groups.keys()) else 0
                live = g3.get_group('live').count().id if ('live' in g3.groups.keys()) else 0
                suspended = g3.get_group('suspended').count().id if ('suspended' in g3.groups.keys()) else 0
                total = successful + canceled + failed + live + suspended
                
                rate = 0
                if total > 0:
                    rate = round((successful / total) , 2)
                d = {'year': y, 'category': c, 'success rate': rate}
                df6 = df6.append(d, ignore_index = True)
            else:
                rate = 0
                d = {'year': y, 'category': c, 'success rate': rate}
                df6 = df6.append(d, ignore_index = True)

    else:
        rate = 0
        for c in category:
            d = {'year': y, 'category': c, 'success rate': rate}
            df6 = df6.append(d, ignore_index = True)
    




# %%
fig2 = px.line(df6, 
              x="year" ,
              y='success rate',
              color='category',
              markers=True,
              title="Success Rate of projects for each Category over the Years",
              labels={
                     "year": "Year",
                     "success rate": "Success Rate",
                     "category": "Category"
                 },
              )

fig2.update_layout(
        xaxis=dict(tickmode="linear"),
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False)),)

st.plotly_chart(fig2, use_container_width=True)

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

