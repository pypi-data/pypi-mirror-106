#load library
import pandas as pd
import scipy.stats as ss
import plotly.figure_factory as ff 
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier,AdaBoostClassifier,RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier 
from jupyter_dash import JupyterDash
import dash
#from scipy.stats import shapiro
import dash_table
from statsmodels.graphics.gofplots import qqplot
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_html_components import P
from dash_core_components import Dropdown,RangeSlider,Graph
from dash.dependencies import Input, Output
import dash.dependencies as ddp
import plotly.express as px
#import base64
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import io
from base64 import b64encode


class PD_EDA:
    def __init__(self,data,display='jupyter'):
      '''
      ########


      '''
        self.data=data
        self.display=display
    def plotly_dash_eda(self):
        data=self.data
        if 'Unnamed: 0' in data.columns.tolist():
            data.drop('Unnamed: 0',inplace=True,axis=1)
        cat_=[]
        int_=[]
        float_=[]
        for i in self.data.columns.tolist():
            if self.data[i].dtype in ['float64','float32','float16']:
                float_.append(i)
            if self.data[i].dtype in ['object']:
                if len(self.data[i].unique().tolist())<30:
                    cat_.append(i)
                else:
                    pass
            if self.data[i].dtype in ['int64','int32','int16','int8']:
                if len(self.data[i].unique().tolist())<30:
                    cat_.append(i)
                else:
                    int_.append(i)
        self.data[cat_]=self.data[cat_].astype('O')
        num_=int_+float_
        button_style = {'background-color': 'rgb(69, 190, 195)',
                      'color': 'white',
                      'height': '50px',
                      'width': '200px',
                      'margin-top': '50px',
                      'margin-left': '50px',
                     'fontSize':20,'border-radius': '25px'}

        def download_html(fig):
            buffer = io.StringIO()
            fig.write_html(buffer)
            html_bytes = buffer.getvalue().encode()
            href_="data:text/html;base64,"+ b64encode(html_bytes).decode()
            return href_

        page_style={'width': '96%','margin': '2%', 'display': 'inline-block','color':'white','fontSize': 20,
                     'padding': '10px 10px','border-radius': '25px',
                     'backgroundColor': 'rgb(57, 57, 63)','border': '2% solid rgb(173, 254, 8)'}

        title_style=style={'color':'rgb(249, 41, 216)', 'fontSize': 15,'font-family': "Sofia"}

        app_style_60_graph={'width': '54%','margin': '2%', 'display': 'inline-block','color':'white','fontSize': 10,
                   'padding': '10px 10px','border-radius': '25px',
                   'backgroundColor': 'rgb(193, 132, 239)','border': '2% solid rgb(255, 255, 255)',
                  'text-align': 'center',}

        app_style_30_graph={'width': '29%','margin': '2%', 'display': 'inline-block','color':'white','fontSize': 10,
                   'padding': '10px 10px','border-radius': '25px',
                   'backgroundColor': 'rgb(193, 132, 239)','border': '2% solid rgb(255, 255, 255)',
                  'text-align': 'center',}

        graph_1=html.Div([
                    html.Center(html.H1('Box plot '),
                    style=title_style),  

                    dcc.Checklist(
                         id='select1',
                         options=[
                         {'label': 'Grouped plot', 'value': 'B1'}],
                         value=[''],
                         labelStyle={'display': 'inline-block','color':'white'}
                         ),
                    html.P("Categorical variable :"),        
                   dcc.Dropdown(
                        id='bx1',
                        options=[{'label': i, 'value': i} for i in cat_],
                        value=cat_[0],
                        style={'color':'black'},
                        clearable=False),

                    html.P("Numeric variable :"),          
                    dcc.Dropdown(
                        id='bx2',
                        options=[{'label': i, 'value': i} for i in num_],
                        value=num_[0],
                         style={'color':'black'},
                        clearable=False),

                    html.P("Grouped variable :"),
                   dcc.Dropdown(
                        id='bx3',
                        options=[{'label': i, 'value': i} for i in cat_],
                        value=cat_[0],
                        style={'color':'black'},
                        clearable=False),

                    dcc.Graph(id='graph1',figure={}),

                     html.A(html.Button('Download as HTML',style=button_style),id="download1",download="plotly_graph_box.html")],         
                    style=page_style)

        graph_2=html.Div([
                html.Center(html.H1('Histogram plot'), 
                            style=title_style),

                dcc.Checklist(
                         id='select2',
                         options=[
                         {'label': 'Grouped plot', 'value': 'B1'}],
                         value=[''],
                         labelStyle={'display': 'inline-block','color':'white'}
                         ),
                html.P("Numeric variable :"),
                dcc.RadioItems(
                        id='hist_var1', 
                        options=[{'value': x, 'label': x} 
                        for x in num_],
                        value=num_[0], 
                        labelStyle={'display': 'inline-block','color':'white'}
                         ),
               html.P("Categorical variable :"),
                dcc.RadioItems(
                        id='hist_var2', 
                        options=[{'value': x, 'label': x} 
                        for x in cat_],
                        value=cat_[0], 
                        labelStyle={'display': 'inline-block','color':'white'}
                         ),

                dcc.Graph(id='graph2',figure={}),
                html.A(html.Button('Download as HTML',style=button_style),id="download2",download="plotly_graph_hist.html"),

                 html.P(" x axis variable :"),          
                    dcc.Dropdown(
                        id='h1',
                        options=[{'label': i, 'value': i} for i in num_],
                        value=num_[0],
                        style={'color':'black'},
                        clearable=False),
                    html.P(" y axis variable :"),          
                    dcc.Dropdown(
                        id='h2',
                        options=[{'label': i, 'value': i} for i in num_],
                        value=num_[1],
                        style={'color':'black'},
                        clearable=False),
                    html.P(" row variable :"),          
                    dcc.Dropdown(
                        id='h3',
                        options=[{'label': i, 'value': i} for i in cat_],
                        value=cat_[1],
                        style={'color':'black'},
                        clearable=False),
                    html.P(" column variable :"),          
                    dcc.Dropdown(
                        id='h4',
                        options=[{'label': i, 'value': i} for i in cat_],
                        value=cat_[2],
                        style={'color':'black'},
                        clearable=False),
                    dcc.Graph(id='graph21',figure={}),
                    html.A(html.Button('Download as HTML',style=button_style),id="download21",download="plotly_graph_bar_mat.html")],
                style=page_style)

        graph_3=html.Div([
                    html.Center(html.H1('Bar plot '),style=title_style), 
                    dcc.Checklist(
                         id='select3',
                         options=[
                         {'label': 'grouped plot', 'value':'group'}],
                         value=['stack'],
                         labelStyle={'display': 'inline-block','color':'white'}
                         ),

                    html.P(" function :"),
                    dcc.RadioItems(
                        id='fun', 
                        options=[{'value': x, 'label': x} 
                        for x in ['mean','sum','count','max','min']],
                        value='mean', 
                        labelStyle={'display': 'inline-block','color':'white'}
                         ),
                    html.P(" Numeric variable :"),          
                    dcc.Dropdown(
                        id='bar1',
                        options=[{'label': i, 'value': i} for i in num_],
                        value=num_[0],
                        style={'color':'black'},
                        clearable=False),

                   html.P(" Categorical variable :"),        
                   dcc.Dropdown(
                        id='bar2',
                        options=[{'label': i, 'value': i} for i in cat_],
                        value=cat_[:2],
                        clearable=False,
                        searchable=True,
                       style={'color':'black'},
                        multi=True),

                    dcc.Graph(id='graph3',figure={}),
                    html.A(html.Button('Download as HTML',style=button_style),id="download3",download="plotly_graph_bar.html")  ,     


                    html.P(" x axis variable :"),          
                    dcc.Dropdown(
                        id='s1',
                        options=[{'label': i, 'value': i} for i in cat_],
                        value=cat_[0],
                        style={'color':'black'},
                        clearable=False),
                    html.P(" y axis variable :"),          
                    dcc.Dropdown(
                        id='s2',
                        options=[{'label': i, 'value': i} for i in num_],
                        value=num_[0],
                        style={'color':'black'},
                        clearable=False),
                    html.P(" row variable :"),          
                    dcc.Dropdown(
                        id='s3',
                        options=[{'label': i, 'value': i} for i in cat_],
                        value=cat_[1],
                        style={'color':'black'},
                        clearable=False),
                    html.P(" column variable :"),          
                    dcc.Dropdown(
                        id='s4',
                        options=[{'label': i, 'value': i} for i in cat_],
                        value=cat_[2],
                        style={'color':'black'},
                        clearable=False),
                    dcc.Graph(id='graph31',figure={}),
                    html.A(html.Button('Download as HTML',style=button_style),id="download31",download="plotly_graph_bar_mat.html")],         
                    style=page_style)

        graph_4=html.Div([
                    html.Center(html.H1('pie plot '),
                    style=title_style),

                    html.P(" function :"),
                    dcc.RadioItems(
                        id='fun', 
                        options=[{'value': x, 'label': x} 
                        for x in ['mean','sum','count','max','min']],
                        value='mean' ,
                        labelStyle={'display': 'inline-block','color':'white'}
                         ),

                    html.P(" Numeric variable :"),          
                    dcc.Dropdown(
                        id='pie1',
                        options=[{'label': i, 'value': i} for i in num_],
                        value=num_[:1],
                        clearable=False,
                        style={'color':'black'},
                        multi=True),


                   html.P(" Categorical variable :"),        
                   dcc.Dropdown(
                        id='pie2',
                        options=[{'label': i, 'value': i} for i in cat_],
                        value=cat_[:2],
                        clearable=False,
                        multi=True),

                    dcc.Graph(id='graph4',figure={}),
                    html.A(html.Button('Download as HTML',style=button_style),id="download4",download="plotly_graph_pie.html")],         
                    style=page_style)
        graph_5=html.Div([
                    html.Center(html.H1('scatter plot '),
                    style=title_style),
             dcc.Checklist(
                         id='select5',
                         options=[
                         {'label': 'Group plot', 'value':'group'}],
                         value=[''],
                         labelStyle={'display': 'inline-block','color':'white'}
                         ),
                    html.P("X axis numeric variable :"),          
                    dcc.Dropdown(
                        id='scatt1',
                        options=[{'label': i, 'value': i} for i in num_],
                        value=num_[0],
                        style={'color':'black'},
                        clearable=False,
                       # multi=True
                    ),

                   html.P("Y axis numeric variable :"),        
                   dcc.Dropdown(
                        id='scatt2',
                        options=[{'label': i, 'value': i} for i in num_],
                        value=num_[1],
                        clearable=False,
                       style={'color':'black'},
                       # multi=True
                   ),

                   html.P(" grouped variable :"),        
                   dcc.Dropdown(
                        id='scatt3',
                        options=[{'label': i, 'value': i} for i in cat_],
                        value=cat_[0],
                        clearable=False,
                       style={'color':'black'},
                       # multi=True
                   ),

                    dcc.Graph(id='graph5',figure={}),
                    html.A(html.Button('Download as HTML',style=button_style),id="download5",download="plotly_graph_scatter.html"),

                  html.P(" multiple numeric variable :"),          
                    dcc.Dropdown(
                        id='scatt4',
                        options=[{'label': i, 'value': i} for i in num_],
                        value=num_,
                        clearable=False,
                        style={'color':'black'},
                        multi=True),
                dcc.Graph(id='graph5_1',figure={}),
                html.A(html.Button('Download as HTML',style=button_style),id="download51",download="plotly_graph_scatter.html")],         
                    style=page_style)

        graph_6=html.Div([
                    html.Center(html.H1('correlation plot '),
                    style=title_style),

                    html.P(" method :"),
                    dcc.RadioItems(
                        id='fun_1', 
                        options=[{'value': x, 'label': x} 
                        for x in ['pearson', 'kendall', 'spearman']],
                        value='pearson' ,
                        labelStyle={'display': 'inline-block','color':'white'}
                         ),

                    html.P(" numeric variable :"),          
                    dcc.Dropdown(
                        id='heat1',
                        options=[{'label': i, 'value': i} for i in num_],
                        value=num_[:2],
                        clearable=False,
                        style={'color':'black'},
                        multi=True),

                    dcc.Graph(id='graph6',figure={}),
                    html.A(html.Button('Download as HTML',style=button_style),id="download6",download="plotly_graph_corr.html")],         
                    style=page_style)

        a=[]
        input_list=[]
        for col in data.columns.tolist():
            if col in cat_:
                list_=data[col].unique().tolist()
                a.append(html.P(col+' :'))
                drop=dcc.Dropdown(id='drop_'+col,
                                  options=[{'label': val, 'value': val} for val in list_],
                                  value=list_,
                                  clearable=False, 
                                  multi=True)
                a.append(drop)
                input_list.append(ddp.Input('drop_'+col,'value'))
            if col in num_:
                list_=data[col].unique().tolist()
                min_=data[col].min()
                max_=data[col].max()
                a.append(html.P(col+' :'))
                s={}
                values=np.linspace(min_,max_, num=5)
                for value in values:
                    s.update({value:{'label':str(np.round(value,3)), 'style': {'color': 'white'}}})
                range_slider=dcc.RangeSlider(
                                    id='range_'+col,
                                    min=min_,
                                    max=max_,
                                    marks=s,
                                    value=[min_,max_],
                                    allowCross=False)
                a.append(range_slider)
                input_list.append( ddp.Input('range_'+col,'value'))
        #input_list.append(ddp.Input('download7','value'))
        graph_7=html.Div([

            html.Div([
            html.Div(a[:int(len(a)/2)],style={'width': '45%', 'margin': '2%','display': 'inline-block','padding': '10px 10px','border-radius': '25px','color':'black','fontSize': 20,'padding': '10px 10px'}),
            html.Div(a[int(len(a)/2):], style={'width': '45%','margin': '2%','display': 'inline-block','padding': '10px 10px','border-radius': '25px','color':'black','fontSize':20,'padding': '10px 10px'})],
            style={'color':'black','fontSize':20,'backgroundColor': 'rgb(222, 174, 254)'}),
            dash_table.DataTable(
                id='table',
                export_format='csv',
                export_headers='display',
                style_data_conditional=[{'if': {'row_index': 'odd'},'backgroundColor': 'rgb(208, 219, 239)','color':'black'},
                                        {'if':{'row_index': 'even'},'color':'black'}],
                style_header={'backgroundColor': 'rgb(222, 91, 243)','fontWeight': 'bold','color':'black','fontSize':20},
                sort_action='native',page_size=50)],
                style=page_style)



        graph_8=html.Div([
                    html.Center(html.H1('treemap plot '),
                    style=title_style),
                    html.P("Categorical variable :"),          
                    dcc.Dropdown(
                        id='tree1',
                        options=[{'label': i, 'value': i} for i in cat_],
                        value=cat_,
                        clearable=False,
                        style={'color':'black'},
                        multi=True),

                   html.P("numeric variable :"),        
                   dcc.Dropdown(
                        id='tree2',
                        options=[{'label': i, 'value': i} for i in num_],
                        value=num_[0],
                        clearable=False,
                       style={'color':'black'},
                       # multi=True   
                         ),

                    dcc.Graph(id='graph8',figure={}),
                    html.A(html.Button('Download as HTML',style=button_style),id="download8",download="plotly_graph_tree.html")],         
                    style=page_style)

        graph_9=html.Div([
                    html.Center(html.H1('covariance plot '),
                    style=title_style),

                    html.P(" numeric variable :"),          
                    dcc.Dropdown(
                        id='cov1',
                        options=[{'label': i, 'value': i} for i in num_],
                        value=num_[:2],
                        clearable=False,
                        style={'color':'black'},
                        multi=True),

                    dcc.Graph(id='graph9',figure={}),
                    html.A(html.Button('Download as HTML',style=button_style),id="download9",download="plotly_graph_cov.html")],         
                    style=page_style)

        graph_10=html.Div([
                    html.Center(html.H1('Features importance plot '),
                    style=title_style),

                    html.P(" classifier :"),
                    dcc.RadioItems(
                        id='imp1', 
                        options=[{'value': x, 'label': x} 
                        for x in ['Extra Trees Classifier','Ada Boost Classifier', 'Decision Tree Classifier', 'Random Forest Classifier']],
                        value='Ada Boost Classifier' ,
                        labelStyle={'display': 'inline-block','color':'white'}
                         ),

                    html.P(" target categorical variable :"),          
                    dcc.Dropdown(
                        id='imp2',
                        options=[{'label': i, 'value': i} for i in cat_],
                        value=cat_[0],
                        clearable=False,
                        style={'color':'black'},
                        #multi=True
                    ),

                    dcc.Graph(id='graph10',figure={}),
                    html.A(html.Button('Download as HTML',style=button_style),id="download10",download="plotly_graph_imp.html")],         
                    style=page_style)



        graph_17=html.Div([
                html.Div([dcc.Graph(id='graph11',figure={}),
                          html.A(html.Button('Download as HTML',style=button_style),id="download11",download="plotly_graph_scatter_summary.html")],style=app_style_60_graph),
                html.Div([dcc.Graph(id='graph12',figure={}),
                         html.A(html.Button('Download as HTML',style=button_style),id="download12",download="plotly_graph_summary.html")], style=app_style_30_graph)
                    ],style=page_style)

        graph_11=html.Div([
                    html.Center(html.H1('Summary plot of individual variable '),
                    style=title_style),

                    html.P("variable :"),          
                    dcc.Dropdown(
                        id='sum1',
                        options=[{'label': i, 'value': i} for i in num_+cat_],
                        value=num_[0] or cat_[0],
                        clearable=False,
                        style={'color':'black'}),
                        graph_17],style=page_style)

        sum_all=html.Div([
                    html.Center(html.H1('summary plot of all variables'),style=title_style),
                    dcc.Graph(id='graph_sum_all1',figure={}),
                    html.A(html.Button('Download as HTML',style=button_style),id="download_sum_all1",download="plotly_graph_summary_num.html"),
                    dcc.Graph(id='graph_sum_all2',figure={}),
                    html.A(html.Button('Download as HTML',style=button_style),id="download_sum_all2",download="plotly_graph_summary_cat.html")],
                    style=page_style)

        graph_13=html.Div([
                    html.Center(html.H1('Dotplot '),
                    style=title_style),

                    html.P("numeric variable :"),          
                    dcc.Dropdown(
                        id='dot1',
                        options=[{'label': i, 'value': i} for i in num_],
                        value=num_[0],
                        clearable=False,
                    style={'color':'black'}),
                   html.P("categorical variable :"),          
                    dcc.Dropdown(
                        id='dot2',
                        options=[{'label': i, 'value': i} for i in cat_],
                        value=cat_[:2],
                        clearable=False,
                        style={'color':'black'},
                        multi=True),

                    dcc.Graph(id='graph13',figure={}),
                    html.A(html.Button('Download as HTML',style=button_style),id="download13",download="plotly_graph_dot.html")],         
                    style=page_style)
        graph_14=html.Div([
                    html.Center(html.H1('Sunbrust plot '),
                    style=title_style),

                    html.P(" function :"),
                    dcc.RadioItems(
                        id='fun_14', 
                        options=[{'value': x, 'label': x} 
                        for x in ['mean','sum','max','min','count']],
                        value='count' ,
                        labelStyle={'display': 'inline-block','color':'white'}
                         ),

                    html.P("numeric variable :"),          
                    dcc.Dropdown(
                        id='sub1',
                        options=[{'label': i, 'value': i} for i in num_],
                        value=num_[0],
                        clearable=False,
                    style={'color':'black'}),


                   html.P("categorical variables :"),          
                    dcc.Dropdown(
                        id='sub2',
                        options=[{'label': i, 'value': i} for i in cat_],
                        value=cat_[:2],
                        clearable=False,
                        style={'color':'black'},
                        multi=True),

                 dcc.Graph(id='graph14',figure={}),
                 html.A(html.Button('Download as HTML',style=button_style),id="download14",download="plotly_graph_sub.html")],         
                    style=page_style)

        graph_15=html.Div([
                    html.Center(html.H1('pivot table '),
                    style=title_style),

                    html.P(" pivot function :"),
                    dcc.RadioItems(
                        id='fun1', 
                        options=[{'value': x, 'label': x} 
                        for x in ['mean','sum','count','max','min']],
                        value='sum' ,
                        labelStyle={'display': 'inline-block','color':'white'}
                         ),
                   html.P(" table function :"),       
                     dcc.Dropdown(
                        id='fun2',
                        options=[{'label': i, 'value': i} for i in ['sum','min','max','prod']],
                        value=['sum'],
                        clearable=False,
                        style={'color':'black'},
                        multi=True),

                   html.P(" Numeric variable :"),       
                     dcc.Dropdown(
                        id='piv1',
                        options=[{'label': i, 'value': i} for i in num_],
                        value=num_[:2],
                        clearable=False,
                        style={'color':'black'},
                        multi=True),

                  html.P(" categorical variable :"),       
                    dcc.Dropdown(
                        id='piv2',
                        options=[{'label': i, 'value': i} for i in cat_],
                        value=cat_[:2],
                        clearable=False,
                        style={'color':'black'},
                        multi=True),
                  dcc.Graph(id='graph15',figure={}),
                  html.A(html.Button('Download as HTML',style=button_style),id="download15",download="plotly_graph_pivot.html")],
                  style=page_style)


        graph_18=html.Div([
                    html.Center(html.H1('Line plot '),
                    style=title_style),
                    html.P("numeric variable :"),          
                    dcc.Dropdown(
                        id='line1',
                        options=[{'label': i, 'value': i} for i in num_],
                        value=num_[0],
                        clearable=False,
                    style={'color':'black'}),
                    dcc.Graph(id='graph18',figure={}),
                    html.A(html.Button('Download as HTML',style=button_style),id="download18",download="plotly_graph_line.html")],
                    style=page_style)


        graph_19=html.Div([
                    html.Center(html.H1('Outlier plot'),style=title_style),
                    html.P("numeric variable :"),          
                    dcc.Dropdown(
                        id='out1',
                        options=[{'label': i, 'value': i} for i in num_],
                        value=num_[0],
                        clearable=False,
                    style={'color':'black'}),
                   dcc.Graph(id='graph19',figure={}),
                    html.A(html.Button('Download as HTML',style=button_style),id="download19",download="plotly_graph_outlier.html")],
                    style=page_style)

        graph_normality=html.Div([
                    html.Center(html.H1('Normality test'),style=title_style),
                    html.P("numeric variable :"),          
                    dcc.Dropdown(
                        id='norm1',
                        options=[{'label': i, 'value': i} for i in num_],
                        value=num_[0],
                        clearable=False,
                    style={'color':'black'}),
                   dcc.Graph(id='normality',figure={}),
                    html.A(html.Button('Download as HTML',style=button_style),id="normality_dload",download="plotly_graph_normality.html")],
                    style=page_style)


        tabs_styles = {'height': '80%'}
        tab_style = {'borderBottom': '1px solid #d6d6d6','padding': '6px','border-radius': '25px'} #'fontWeight': 'bold'

        tab_selected_style = {'borderTop': '1px solid #d6d6d6','borderBottom': '1px solid #d6d6d6',
                          'backgroundColor': '#119DFF','color': 'white','padding': '6px','border-radius': '25px'}


        graph_map=html.Div([
                  dcc.Tabs(id="tabs_map", value='tab_1',
                children=[
                    dcc.Tab(label='correlation heatmap', value='tab_1',style=tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label='covariance heatmap ', value='tab_2',style=tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label='treemap', value='tab_3',style=tab_style, selected_style=tab_selected_style)],
                    style=tabs_styles),
                html.Div(id='tabs-content-map')])

        graph_statistics=html.Div([
                  dcc.Tabs(id="tabs_statistics", value='tab_1',
                children=[
                    dcc.Tab(label='Scatter plot', value='tab_1',style=tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label='Box plot', value='tab_2',style=tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label='Hist plot', value='tab_3',style=tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label='Bar plot', value='tab_4',style=tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label='Pie plot', value='tab_5',style=tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label='Line plot', value='tab_6',style=tab_style, selected_style=tab_selected_style)],
                    style=tabs_styles),
                html.Div(id='tabs-content-statistics')])

        graph_summary=html.Div([
                  dcc.Tabs(id="tabs_sum_all", value='tab_1',
                children=[
                    dcc.Tab(label='summary plot of all variables', value='tab_1',style=tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label='summary plot of individual variable', value='tab_2',style=tab_style, selected_style=tab_selected_style)],
                    style=tabs_styles),
                    html.Div(id='tabs-content-sum-all')])

        graph_others=html.Div([
                dcc.Tabs(id="tabs_others", value='tab_1',
                children=[
                    dcc.Tab(label='Features imprtance barpot', value='tab_1',style=tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label='Dot plot', value='tab_2',style=tab_style, selected_style=tab_selected_style),
                    dcc.Tab(label='Sunbrust plot', value='tab_3',style=tab_style, selected_style=tab_selected_style)],
                    style=tabs_styles),
                html.Div(id='tabs-content-others')])


        external_stylesheets = [dbc.themes.BOOTSTRAP]
        JupyterDash.infer_jupyter_proxy_config()
        if self.display=='jupyter':
            app = JupyterDash(__name__,external_stylesheets=external_stylesheets)
        if self.display=='localhost':
            app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
        app.title = 'DP-EDA'
        app.layout =html.Div([

                dcc.Tabs(id="tabs", value='tab-1',
                children=[
                dash_table.DataTable(data=data.to_dict('records'),columns=[{'id': c, 'name': c} for c in data.columns],
                style_data_conditional=[{'if': {'row_index': 'odd'},'backgroundColor': 'rgb(208, 219, 239)','color':'black'}],
                style_header={'backgroundColor': 'rgb(222, 91, 243)','fontWeight': 'bold','color':'black','fontSize':11}),

                dcc.Tab(label='filter data', value='tab_7',style=tab_style, selected_style=tab_selected_style),

                dcc.Tab(label='Statistical plots', value='tab_5',style=tab_style, selected_style=tab_selected_style),

                dcc.Tab(label='Map plots', value='tab_9',style=tab_style, selected_style=tab_selected_style),

                dcc.Tab(label=' Summary plot', value='tab_11',style=tab_style, selected_style=tab_selected_style),

                dcc.Tab(label='Outlier plot', value='tab_19',style=tab_style, selected_style=tab_selected_style),

                dcc.Tab(label='Normality test', value='tab_21',style=tab_style, selected_style=tab_selected_style),

                dcc.Tab(label=' Pivot table plot', value='tab_15',style=tab_style, selected_style=tab_selected_style),

                dcc.Tab(label=' Other plots', value='tab_14',style=tab_style, selected_style=tab_selected_style)],
                style=tabs_styles),
                html.Div(id='tabs-content') ])

        @app.callback(Output('tabs-content', 'children'),Input('tabs', 'value'))
        def render_content1(tab):
            if tab == 'tab_5':
                return graph_statistics
            if tab == 'tab_21':
                return graph_normality
            if tab == 'tab_7':
                return graph_7
            if tab=='tab_9':
                return graph_map
            if tab == 'tab_11':
                return graph_summary
            if tab == 'tab_14':
                return graph_others
            if tab =='tab_15':
                return graph_15
            if tab =='tab_19':
                return graph_19

        @app.callback(Output('tabs-content-map', 'children'),Input('tabs_map', 'value'))
        def render_content2(tab):
            if tab == 'tab_1':
                return graph_6
            if tab == 'tab_2':
                return graph_9
            if tab== 'tab_3':
                return graph_8

        @app.callback(Output('tabs-content-sum-all', 'children'),Input('tabs_sum_all', 'value'))
        def render_content3(tab):
            if tab == 'tab_1':
                return sum_all
            if tab == 'tab_2':
                return graph_11


        @app.callback(Output('tabs-content-others', 'children'),Input('tabs_others', 'value'))
        def render_content4(tab):
            if tab == 'tab_1':
                return graph_10
            if tab == 'tab_2':
                return graph_13
            if tab== 'tab_3':
                return graph_14

        @app.callback(Output('tabs-content-statistics', 'children'),Input('tabs_statistics', 'value'))
        def render_content5(tab):
            if tab == 'tab_1':
                return graph_5
            if tab == 'tab_2':
                return graph_1
            if tab == 'tab_3':
                return graph_2
            if tab == 'tab_4':
                return graph_3
            if tab == 'tab_5':
                return graph_4
            if tab == 'tab_6':
                return graph_18
        @app.callback(Output("graph1", "figure"),Output("download1", "href"),Input('bx1','value'),Input('bx2','value'),
                      Input('bx3','value'),Input('select1','value'),Input('download1','value'))
        def my_graph1(bx1,bx2,bx3,select,dload):
            if select==['']:
                fig = px.box(data, x=bx1, y=bx2)
                #fig.update_layout(plot_bgcolor='white',paper_bgcolor='white',font_color='black')
                fig.update_layout(template='plotly_white')
                fig.update_layout(title='<b>Box plot<b>',title_x=0.5)
                return fig,download_html(fig)
            else:
                fig = px.box(data, x=bx1, y=bx2,color=bx3)
                fig.update_traces(quartilemethod="exclusive")
                #fig.update_layout(plot_bgcolor='white',paper_bgcolor='white',font_color='black')
                fig.update_layout(title='<b>Box plot<b>',title_x=0.5)
                fig.update_layout(template='plotly_white')
                return fig,download_html(fig)

        @app.callback(Output("graph2", "figure"),Output("download2", "href"),Input('hist_var1','value'),
                      Input('hist_var2','value'),Input('select2','value'),Input('download2','value'))
        def my_graph2(hist_var1,hist_var2,select,dload):
            if select==['']:
                fig = px.histogram(data, x=hist_var1,histnorm='probability density')
                #fig.update_layout(plot_bgcolor='white',paper_bgcolor='white',font_color='black')
                fig.update_layout(template='plotly_white')
                fig.update_layout(title='<b>Histogram (variable ={}<b>'.format(hist_var1),title_x=0.5)
                return fig ,download_html(fig)
            else:
                fig = px.histogram(data, x=hist_var1, color=hist_var2,histnorm='probability density')
                #fig.update_layout(plot_bgcolor='white',paper_bgcolor='white',font_color='black')
                fig.update_layout(title='<b>Histogram (variable ={} , group variable={}<b>'.format(hist_var1,hist_var2),title_x=0.5)
                fig.update_layout(template='plotly_white')
                return fig, download_html(fig)

        @app.callback(Output("graph3", "figure"),Output("download3", "href"),Input('bar1','value'),
                      Input('bar2','value'),Input('select3','value'),Input('fun','value'),Input('download3','value'))
        def my_graph3(bar1,bar2,select3,fun,dload):
            if len(bar2)==1:
                df=pd.pivot_table(data,values=[bar1],columns=[bar2[0]],aggfunc=fun)
                var_1=[df.columns.tolist()[i] for i in range(df.shape[1])]
                var_2=df.values.tolist()[0]
                df=pd.DataFrame({bar2[0]:var_1,bar1:var_2})  
                fig = px.bar(df,x=bar2[0], y=bar1,color=bar1,text=bar1)
                fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
                fig.update_layout(uniformtext_minsize=4, uniformtext_mode='hide')
                #fig.update_layout(plot_bgcolor='white',paper_bgcolor='white',font_color='black')
                fig.update_layout(title='<b>bar plot (variable ={} grpup by= {} )<b>'.format(bar1,bar2[0]),title_x=0.5)
                fig.update_layout(template='plotly_white')
                return fig , download_html(fig)
            if len(bar2)>1 :
                df=pd.pivot_table(data,values=[bar1],columns=[bar2[0],bar2[1]],aggfunc=fun)
                var_1=[df.columns.tolist()[i][0] for i in range(df.shape[1])]
                var_2=df.values.tolist()[0]
                var_3=[df.columns.tolist()[i][1] for i in range(df.shape[1])]
                df=pd.DataFrame({bar2[0]:var_1,bar2[1]:var_3,bar1:var_2}) 
                df[bar2[:2]]=df[bar2[:2]].astype('O')
                fig = px.bar(df,x=bar2[0],y=bar1, color=bar2[1],text=bar1)
                fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
                fig.update_layout(uniformtext_minsize=6, uniformtext_mode='hide')
                #fig.update_layout(plot_bgcolor='white',paper_bgcolor='white',font_color='black') 
                fig.update_layout(barmode=select3[-1])
                fig.update_layout(title='<b>bar plot (variable ={} group by = {})<b>'.format(bar1,bar2[:2]),title_x=0.5)
                fig.update_layout(template='plotly_white')
                return fig, download_html(fig)
        @app.callback(Output("graph4", "figure"),Output("download4", "href"),Input('pie1','value'),
                      Input('pie2','value'),Input('fun','value'),Input('download4','value'))
        def my_graph4(pie1,pie2,fun,dload):
            #if pie1!=[] and pie2!=[]:        
            a=[]
            for i in range(len(pie1)*len(pie2)):
                a.append({'type':'domain'})
            a=np.reshape(a,(len(pie1),len(pie2)))
            a=a.tolist()
            title_list=['({},{})'.format(i,j) for i in pie1  for j in pie2 ]
            fig = make_subplots(rows=len(pie1), cols=len(pie2),specs=a,subplot_titles=title_list)
            for i in range(0,len(pie1)):
                for j in range(0,len(pie2)):
                    df=pd.pivot_table(data,values=[pie1[i]],columns=[pie2[j]],aggfunc=fun)
                    var_1=[df.columns.tolist()[n] for n in range(df.shape[1])]
                    var_2=df.values.tolist()[0]             
                    fig.add_trace(go.Pie(labels=var_1, values=var_2,name=pie2[j]),row=i+1, col=j+1)
            fig.update_traces(hole=.3)
            fig.update_traces(textinfo='percent+value+label')
            fig.update_traces(textposition='inside')    #textfont_size=14
            fig.update_layout(uniformtext_minsize=4)
            fig.update_layout(autosize=False) #width=1200,height=1200
            fig.update_layout(title='<b>bar plot (variable ={} group by = {})<b>'.format(pie1,pie2),title_x=0.5)
            fig.update_layout(template='simple_white')
            return fig, download_html(fig)


        @app.callback(Output("graph5", "figure"),Output("graph5_1", "figure"),
                      Output("download5", "href"),Output("download51", "href"),Input('scatt1','value'),
                      Input('scatt2','value'),Input('scatt3','value'),
                      Input('scatt4','value'),Input('select5','value'),
                     Input('download5','value'),Input('download51','value'))
        def my_graph5(scatt1,scatt2,scatt3,scatt4,select,dload,dload1):
            if select==['']:
                fig = px.scatter(data, x=scatt1, y=scatt2, hover_data=[scatt1,scatt2])
                fig.update_layout(title='<b>Scatter plot<b>',title_x=0.5)
                fig.update_layout(template='plotly_white',title_x=0.5)

                fig2 = px.scatter_matrix(data,dimensions=scatt4)
                #fig.update_layout(plot_bgcolor='white',paper_bgcolor='white',font_color='black')
                #fig2.update_layout(plot_bgcolor='white',paper_bgcolor='white',font_color='black')
                fig2.update_layout(title='<b>Scatter matrix plot<b>',dragmode='select',hovermode='closest',title_x=0.5)
                fig2.update_layout(template='plotly_white')
                return fig,fig2,download_html(fig),download_html(fig2)
            else:
                fig = px.scatter(data, x=scatt1, y=scatt2,color=scatt3, hover_data=[scatt1,scatt2])
                fig2 = px.scatter_matrix(data,dimensions=scatt4,color=scatt3)
                #fig.update_layout(plot_bgcolor='white',paper_bgcolor='white',font_color='black')
                #fig2.update_layout(plot_bgcolor='white',paper_bgcolor='white',font_color='black')
                #fig2.update_layout(title='Scatter matrix',dragmode='select',width=1000,height=1000,hovermode='closest')
                fig.update_layout(template='plotly_white')
                fig2.update_layout(template='plotly_white')
                fig.update_layout(title='<b>Scatter plot<b>',title_x=0.5)
                fig2.update_layout(title='<b>Scatter plot<b>',title_x=0.5)
                return fig,fig2,download_html(fig),download_html(fig2)

        @app.callback(Output("graph6", "figure"),Output("download6", "href"),Input('heat1','value'),
                      Input('fun_1','value'),Input('download6','value'))
        def my_graph6(heat1,fun1,dload):
                df=data[heat1]
                corr=df.corr(method=fun1)
                corr=corr.round(decimals=3)
                fig = ff.create_annotated_heatmap(corr.values[::-1], x=corr.columns.tolist(), y=corr.index.tolist()[::-1], annotation_text=corr.values[::-1], showscale=True)
                fig.update_layout(title='<b>correlation heatmap<b>',title_x=0.5)
                fig.update_layout(template='simple_white')
                return fig,download_html(fig) 
        @app.callback(Output("table", "columns"),Output("table", "data"),input_list)
        #@app.callback(Output("graph7", "figure"),Output("download7", "href"),input_list)
        def my_graph7(*v):
            query_list1=''
            data_table=data.copy()
            #data_table.dropna(inplace=True)
            col=data_table.columns.tolist()
            for i in range(len(col)):
                if col[i] in cat_:
                    q1=str(col[i])+ ' in @v['+str(i)+'] and '
                    query_list1=query_list1+q1
                if col[i] in num_ :
                    q1=str(v[i][0])+'<'+str(col[i])+'<'+str(v[i][1])+' and '
                    query_list1=query_list1+q1
            df=data_table.query(query_list1[:-4],engine='python')
            columns=[{"name": i, "id": i} for i in df.columns]
            data_=df.to_dict('records')
            #fig = ff.create_table(df.sample(20))
            return columns,data_
            #fig_d = ff.create_table(df)
            #return fig ,download_html(fig_d)

        @app.callback(Output("graph8", "figure"),Output("download8", "href"),Input('tree1','value'),Input('tree2','value'),
                      Input('download8','value'))
        def my_graph8(tree1,tree2,dload):
            df=data.copy()
            fig = px.treemap(df, path=tree1, values=tree2,color_continuous_scale='RdBu',hover_name=tree1[0],hover_data=tree1)
            fig.update_layout(title='<b>Tree map<b>',title_x=0.5)
            fig.update_layout(template='simple_white')
            return fig ,download_html(fig)

        @app.callback(Output("graph9", "figure"),Output("download9", "href"),Input('cov1','value'),Input('download9','value'))
        def my_graph9(cov,dload):

                df=data[cov]
                covar=df.cov()
                covar=covar.round(decimals=3)
                fig = ff.create_annotated_heatmap(covar.values[::-1], x=covar.columns.tolist(), y=covar.index.tolist()[::-1], annotation_text=covar.values[::-1], showscale=True)
                fig.update_layout(title='<b>covariance heatmap<b>',title_x=0.5)
                fig.update_layout(template='simple_white')
                return fig ,download_html(fig)
        @app.callback(Output("graph10", "figure"),Output("download10", "href"),Input('imp2','value'),
                      Input('imp1','value'),Input('download10','value'))
        def my_graph10(imp2,imp1,dload):
            df=data.dropna().copy()
            obj_df = df.select_dtypes(include=['object']).copy()
            df[obj_df.columns.tolist()] = df[obj_df.columns.tolist()].astype('category')
            for i in obj_df.columns.tolist():
                df[i] = df[i].cat.codes

            X = df.drop(imp2,axis=1)  #independent columns
            y = df[imp2]   #target column i.e price range
            clf = ['Extra Trees Classifier','Ada Boost Classifier', 'Decision Tree Classifier', 'Random Forest Classifier']
            model_list = [ExtraTreesClassifier(),AdaBoostClassifier(),DecisionTreeClassifier(),RandomForestClassifier()]
            model=model_list[clf.index(imp1)]
            model.fit(X,y)
            feat_importances = pd.DataFrame({'Variable':X.columns,'importance':model.feature_importances_})
            fig = px.bar(feat_importances,x='Variable',y='importance')
            fig.update_layout(template='simple_white')
            return fig , download_html(fig)

        @app.callback(Output("graph11", "figure"),Output("graph12", "figure"),
                      Output("download11", "href"),Output("download12", "href"),
                      Input('sum1','value'),Input('download11','value'),Input('download12','value'))
        def plot_summary(col_name,dload,dload1):
            if col_name in num_:
                df=data.dropna().copy()
                var=df[col_name].values
                summary_df=pd.DataFrame({
                           'variable name ':col_name,
                          'missing values ':[data[col_name].isna().sum()+data[col_name].isnull().sum()],
                          'min':[np.min(var)],'mean':[np.mean(var)],
                          'D1' : [np.percentile(var,10)],
                          'Q1' : [np.percentile(var,25)],
                          'Interquartile Range ':[ss.iqr(var)],
                          'median ':[np.median(var)],'Mode ':[ss.mode(var).mode],
                          'Q3' : [np.percentile(var,75)],
                          'D9' : [np.percentile(var,90)],
                          'max':[np.mean(var)],'varince':[np.mean(var)],
                          'Coefficent of variation ':[ss.variation(var)],
                          '2nd central moment ':[ss.moment(var,moment=2)],
                          '3rd central moment ':[ss.moment(var,moment=3)],
                          'kurtosis ':[ss.kurtosis(var)],'skewness ':[ss.skew(var)],
                          'length ':len(var)                            
                          }).T
                summary_df.columns=['value']
                df1=pd.DataFrame()
                df1['statistics']=summary_df.index
                df1['value'] =summary_df.value.values
                summary_df=round(df1,3)
                fig1 = ff.create_table(summary_df)
                for i in range(len(fig1.layout.annotations)):
                    fig1.layout.annotations[i].font.size = 20
                group_labels = [col_name] 
                fig2 = ff.create_distplot([var], group_labels,bin_size=0.1)
                #fig1.update_layout(plot_bgcolor='white',paper_bgcolor='white',font_color='black')
                #fig2.update_layout(plot_bgcolor='white',paper_bgcolor='white',font_color='black')
                fig1.update_layout(template='simple_white')
                fig2.update_layout(template='simple_white')
                return fig1,fig2 ,download_html(fig1),download_html(fig2)
            if col_name in cat_:
                df=data.copy()
                df1=pd.DataFrame()
                df1[col_name]=df[col_name].value_counts().index
                df1['count']=df[col_name].value_counts().values
                fig1 = ff.create_table(df1)
                fig2=px.bar(df1,x=col_name,y='count',color='count')
                #fig1.update_layout(plot_bgcolor='white',paper_bgcolor='white',font_color='black')
                #fig2.update_layout(plot_bgcolor='white',paper_bgcolor='white',font_color='black')
                fig1.update_layout(template='simple_white')
                fig2.update_layout(template='simple_white')
                return fig1, fig2 ,download_html(fig1),download_html(fig2)
        @app.callback(Output("graph13", "figure"),Output("download13", "href"),Input('dot1','value'),
                      Input('dot2','value'),Input('download13','value'))
        def my_graph13(n1,n2,dload):
                v2=n2
                v1=[n1]
                df=pd.pivot_table(data,values=v1,columns=v2,aggfunc='sum')
                df1=pd.DataFrame()
                for i in range(len(v2)) :
                    df1[v2[i]]=[df.columns.tolist()[n][i] for n in range(df.shape[1])]
                for j in range(len(v1)):
                    df1[v1[j]]=df.values[j]
                fig = px.scatter(df1, x=v1[0], y=v2[0], color=v2[1],size=v1[0])
                fig.update_layout(template='simple_white')
                return fig , download_html(fig)    
        @app.callback(Output("graph14", "figure"),Output("download14", "href"),Input('sub1','value'),
                      Input('sub2','value'),Input('fun_14','value'),Input('download14','value'))
        def my_graph14(v1,v2,fun14,dload):
            print(v2)
            v1=[v1]
            print(v1)
            df=pd.DataFrame()
            df=pd.pivot_table(data,values=v1,columns=v2,aggfunc=fun14)
            df1=pd.DataFrame()
            for i in range(len(v2)) :
                if len(v2)==1:
                    df1[v2[i]]=[df.columns.tolist()[n] for n in range(df.shape[1])]

                else:
                    df1[v2[i]]=[df.columns.tolist()[n][i] for n in range(df.shape[1])] 

            for j in range(len(v1)):
                df1[v1[j]]=df.values[j]
            fig = px.sunburst(df1, path=v2, values=v1[0])
            fig.update_layout(template='simple_white')
            return fig , download_html(fig)
        @app.callback(Output("graph15", "figure"),Output("download15", "href"),Input('piv1','value'),Input('piv2','value'),
                      Input('fun1','value'),Input('fun2','value'),Input('download15','value'))
        def my_graph15(v1,v2,fun1,fun2,dload):
            # fun=['sum','min','max','prod']
            df=pd.DataFrame()
            df=pd.pivot_table(data,values=v1,columns=v2,aggfunc=fun1)
            df1=pd.DataFrame()
            for i in range(len(v2)):
                if len(v2)==1:
                    df1[v2[i]]=[df.columns.tolist()[n] for n in range(df.shape[1])]

                else:
                    df1[v2[i]]=[df.columns.tolist()[n][i] for n in range(df.shape[1])]
            for j in range(len(v1)):
                df1[v1[j]]=df.values[j]
            no_rows=df1.shape[0]

            for funs in fun2:
                if funs =='sum':
                    df1['Grand sum']=df1[v1].sum(axis=1)
                    df1=df1.append(df1.iloc[:no_rows,:].sum(numeric_only=True), ignore_index=True)
                    df1=df1.fillna('Grand sum')
                if funs =='min':
                    df1['Grand minimum']=df1[v1].min(axis=1)
                    df1=df1.append(df1.iloc[:no_rows,:].min(numeric_only=True), ignore_index=True)
                    df1=df1.fillna('Grand min')
                if funs =='max':
                    df1['Grand maximum']=df1[v1].max(axis=1)
                    df1=df1.append(df1.iloc[:no_rows,:].max(numeric_only=True), ignore_index=True)
                    df1=df1.fillna('Grand max')
                if funs =='prod':
                    df1['Grand product']=df1[v1].prod(axis=1)
                    df1=df1.append(df1.iloc[:no_rows,:].prod(numeric_only=True), ignore_index=True)
                    df1=df1.fillna('Grand prod')
                if funs =='mean':
                    df1['Grand mean']=df1[v1].mean(axis=1)
                    df1=df1.append(df1.iloc[:no_rows,:].mean(numeric_only=True), ignore_index=True)
                    #df1=df1.fillna('Grand mean')
            df1=round(df1,3)
            fig = ff.create_table(df1)
            # Make text size large
            for i in range(len(fig.layout.annotations)):
                fig.layout.annotations[i].font.size = 12

            return fig ,download_html(fig)

        @app.callback(Output("graph31", "figure"),Output("download31", "href"),Input('s1','value'),Input('s2','value'),
                      Input('s3','value'),Input('s4','value'),Input('download31','value'))
        def my_graph31(s1,s2,s3,s4,s5):
            df=data.copy()
            fig = px.bar(df, x=s1, y=s2, facet_row=s3, facet_col=s4)
            fig.update_layout(title='<b>bar subplots<b>',
                xaxis_title=s1,
                yaxis_title=s2,             
                width=1200, height=1000,font=dict(size=10),
                title_x=0.5,
                margin=dict(l=10, r=10, t=200, b=10))
            fig.update_layout(template='simple_white')
            return fig,download_html(fig)
        @app.callback(Output("graph21", "figure"),Output("download21", "href"),Input('h1','value'),Input('h2','value'),
                      Input('h3','value'),Input('h4','value'),Input('download21','value'))
        def my_graph21(h1,h2,h3,h4,h5):
            df=data.copy()
            fig = px.histogram(df, x=h1, y=h2,facet_row=h3, facet_col=h4)
            fig.update_layout(title='<b>histogram subplots<b>',
                xaxis_title=h1,
                yaxis_title=h2,             
                width=1200, height=1000,font=dict(size=10),
                title_x=0.5,
                margin=dict(l=10, r=10, t=200, b=10))
            fig.update_layout(template='simple_white')
            return fig,download_html(fig)

        @app.callback(Output("graph18", "figure"),Output("download18", "href"),Input('line1','value'),Input('download18','value'))
        def my_graph18(n1,dload):
                df=data.copy()
                df['obs']=range(len(data))
                fig = px.line(df, x="obs", y=n1)
                fig.update_layout(template='simple_white')
                return fig,download_html(fig)

        @app.callback(Output("graph19", "figure"),Output("download19", "href"),
                      Input('out1','value'),Input('download19','value'))
        def my_graph19(v1,dload):
            df = data.copy()
            df1=pd.DataFrame()
            df1['observation no']=range(len(df))
            df1[v1]=df[v1]
            var=df1[v1]
            lcl=np.percentile(var,25)-1.5*ss.iqr(var)
            ucl=np.percentile(var,75)+1.5*ss.iqr(var)
            outlier=lambda x:'inlier' if lcl<x<ucl else 'outlier'
            df1['class']=df[v1].apply(outlier).values
            fig1=px.scatter(df1,y=v1,x='observation no',color='class',size=v1)
            fig1.add_trace(go.Scatter(x=[0,len(df1)],y=[lcl,lcl],mode="lines+text",name="Lower limit",text=["<b>Q1-1.5*IQR<b>", ",<b>Q1-1.5*IQR<b>"],textposition="bottom center"))
            fig1.add_trace(go.Scatter(x=[0,len(df1)],y=[ucl,ucl],mode="lines+text",name="Upper limit",text=["<b>Q3+1.5*IQR<b>", "<b>Q3+1.5*IQR<b>"],textposition="bottom center"))
            fig1.update_layout(title='<b>Outlier detection<b>',title_x=0.5)
            fig1.update_layout(template='plotly_white')
            return fig1 ,download_html(fig1)

        @app.callback(Output("graph_sum_all1", "figure"),Output("graph_sum_all2", "figure"),Output("download_sum_all1", "href"),
                      Output("download_sum_all2", "href"),Input('download_sum_all1','value'),Input('download_sum_all2','value'))
        def my_graph_summary_all(dload1,dload2):
            df=data.copy()
            df1=df.describe(exclude=[np.number]).T
            df1['Missing values']=df.select_dtypes(include=['object']).isnull().sum().values
            table_cat = ff.create_table(df1, index=True, index_title='variables')
            df2=df.describe().T
            df2['Missing']=df.select_dtypes(include=[np.number]).isnull().sum().values+df.select_dtypes(include=[np.number]).isna().sum().values
            df2[' IQR']=df.select_dtypes(include=[np.number]).apply(lambda x :ss.iqr(x),axis=0).values
            df2[' CV']=df.select_dtypes(include=[np.number]).apply(lambda x :ss.variation(x),axis=0).values
            df2[' kurtosis']=df.select_dtypes(include=[np.number]).apply(lambda x :ss.kurtosis(x),axis=0).values
            df2[' skewness']=df.select_dtypes(include=[np.number]).apply(lambda x :ss.skew(x),axis=0).values
            df2=round(df2,3)
            table_num = ff.create_table(df2, index=True, index_title='<b>variables<b>')
            return table_cat,table_num,download_html(table_cat),download_html(table_num)

        @app.callback(Output("normality", "figure"),Output("normality_dload", "href"),
                      Input('norm1','value'),Input("normality_dload",'value'))
        def normality_test(v1,dload):
            df = data.copy()
            var=df[v1].values
            qqplot_data = qqplot(var, line='s').gca().lines
            fig = go.Figure()
            fig.add_trace({'type': 'scatter','x': qqplot_data[0].get_xdata(),'y': qqplot_data[0].get_ydata(),'mode': 'markers',
                'marker': {'color': 'red'}})
            fig.add_trace({'type': 'scatter','x': qqplot_data[1].get_xdata(),'y': qqplot_data[1].get_ydata(),'mode': 'lines',
                'line': {'color': 'blue'}})

            fig['layout'].update({ 'xaxis': {'title': 'Theoritical Quantities','zeroline': False},'yaxis': {'title': 'Sample Quantities'},
                                 'showlegend': False}) #'width': 800,'height': 700
            fig.update_layout(title='<b>Quantile-Quantile Plot<b>',title_x=0.5)

            fig.update_layout(template='plotly_white')  
            return fig , download_html(fig)
        
        if self.display=='jupyter':
            app.run_server(mode='inline')
        if self.display=='localhost': 
            app.run_server()
               