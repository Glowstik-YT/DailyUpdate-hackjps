# imports for the program
from tkinter import *
import requests
import json
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import datetime
from scipy.ndimage.filters import gaussian_filter1d

country_dict = {'Afghanistan': 'AF',
                'Albania': 'AL',
                'Algeria': 'DZ',
                'Angola': 'AO',
                'Argentina': 'AR',
                'Armenia': 'AM',
                'Australia': 'AU',
                'Austria': 'AT',
                'Azerbaijan': 'AZ',
                'Bahamas': 'BS',
                'Bangladesh': 'BD',
                'Belarus': 'BY',
                'Belgium': 'BE',
                'Belize': 'BZ',
                'Benin': 'BJ',
                'Bhutan': 'BT',
                'Bolivia': 'BO',
                'Bosnia and Herzegovina': 'BA',
                'Botswana': 'BW',
                'Brazil': 'BR',
                'Brunei Darussalam': 'BN',
                'Bulgaria': 'BG',
                'Burkina Faso': 'BF',
                'Burundi': 'BI',
                'Cambodia': 'KH',
                'Cameroon': 'CM',
                'Canada': 'CA',
                'Central African Republic': 'CF',
                'Chad': 'TD',
                'Chile': 'CL',
                'China': 'CN',
                'Colombia': 'CO',
                'Congo': 'CG',
                'Costa Rica': 'CR',
                'Croatia': 'HR',
                'Cuba': 'CU',
                'Cyprus': 'CY',
                'Czechia': 'CZ',
                'Democratic Republic of Congo': 'CD',
                'Denmark': 'DK',
                'Diamond Princess Cruise Ship': 'DP',
                'Djibouti': 'DJ',
                'Dominican Republic': 'DO',
                'Ecuador': 'EC',
                'Egypt': 'EG',
                'El Salvador': 'SV',
                'Equatorial Guinea': 'GQ',
                'Eritrea': 'ER',
                'Estonia': 'EE',
                'Ethiopia': 'ET',
                'Falkland Islands': 'FK',
                'Fiji': 'FJ',
                'Finland': 'FI',
                'France': 'FR',
                'French Guiana': 'GF',
                'French Southern Territories': 'TF',
                'Gabon': 'GA',
                'Gambia': 'GM',
                'Georgia': 'GE',
                'Germany': 'DE',
                'Ghana': 'GH',
                'Greece': 'GR',
                'Greenland': 'GL',
                'Guatemala': 'GT',
                'Guinea': 'GN',
                'Guinea-Bissau': 'GW',
                'Guyana': 'GY',
                'Haiti': 'HT',
                'Honduras': 'HN',
                'Hong Kong': 'HK',
                'Hungary': 'HU',
                'Iceland': 'IS',
                'India': 'IN',
                'Indonesia': 'ID',
                'Iran': 'IR',
                'Iraq': 'IQ',
                'Ireland': 'IE',
                'Israel': 'IL',
                'Italy': 'IT',
                'Ivory Coast': 'CI',
                'Jamaica': 'JM',
                'Japan': 'JP',
                'Jordan': 'JO',
                'Kazakhstan': 'KZ',
                'Kenya': 'KE',
                'Korea': 'KP',
                'Kosovo': 'XK',
                'Kuwait': 'KW',
                'Kyrgyzstan': 'KG',
                'Lao': 'LA',
                'Latvia': 'LV',
                'Lebanon': 'LB',
                'Lesotho': 'LS',
                'Liberia': 'LR',
                'Libya': 'LY',
                'Lithuania': 'LT',
                'Luxembourg': 'LU',
                'Macedonia': 'MK',
                'Madagascar': 'MG',
                'Malawi': 'MW',
                'Malaysia': 'MY',
                'Mali': 'ML',
                'Mauritania': 'MR',
                'Mexico': 'MX',
                'Moldova': 'MD',
                'Mongolia': 'MN',
                'Montenegro': 'ME',
                'Morocco': 'MA',
                'Mozambique': 'MZ',
                'Myanmar': 'MM',
                'Namibia': 'NA',
                'Nepal': 'NP',
                'Netherlands': 'NL',
                'New Caledonia': 'NC',
                'New Zealand': 'NZ',
                'Nicaragua': 'NI',
                'Niger': 'NE',
                'Nigeria': 'NG',
                'North Korea': 'KP',
                'Norway': 'NO',
                'Oman': 'OM',
                'Pakistan': 'PK',
                'Palestine': 'PS',
                'Panama': 'PA',
                'Papua New Guinea': 'PG',
                'Paraguay': 'PY',
                'Peru': 'PE',
                'Philippines': 'PH',
                'Poland': 'PL',
                'Portugal': 'PT',
                'Puerto Rico': 'PR',
                'Qatar': 'QA',
                'Republic of Kosovo': 'XK',
                'Romania': 'RO',
                'Russia': 'RU',
                'Rwanda': 'RW',
                'Saudi Arabia': 'SA',
                'Senegal': 'SN',
                'Serbia': 'RS',
                'Sierra Leone': 'SL',
                'Singapore': 'SG',
                'Slovakia': 'SK',
                'Slovenia': 'SI',
                'Solomon Islands': 'SB',
                'Somalia': 'SO',
                'South Africa': 'ZA',
                'South Korea': 'KR',
                'South Sudan': 'SS',
                'Spain': 'ES',
                'Sri Lanka': 'LK',
                'Sudan': 'SD',
                'Suriname': 'SR',
                'Svalbard and Jan Mayen': 'SJ',
                'Swaziland': 'SZ',
                'Sweden': 'SE',
                'Switzerland': 'CH',
                'Syrian Arab Republic': 'SY',
                'Taiwan': 'TW',
                'Tajikistan': 'TJ',
                'Tanzania': 'TZ',
                'Thailand': 'TH',
                'Timor-Leste': 'TL',
                'Togo': 'TG',
                'Trinidad and Tobago': 'TT',
                'Tunisia': 'TN',
                'Turkey': 'TR',
                'Turkmenistan': 'TM',
                'UAE': 'AE',
                'Uganda': 'UG',
                'Ukraine': 'UA',
                'United Kingdom': 'GB',
                'Uruguay': 'UY',
                'USA': 'US',
                'Uzbekistan': 'UZ',
                'Vanuatu': 'VU',
                'Venezuela': 'VE',
                'Vietnam': 'VN',
                'Western Sahara': 'EH',
                'Yemen': 'YE',
                'Zambia': 'ZM',
                'Zimbabwe': 'ZW'}

OPTIONS = ['Afghanistan',
            'Albania',
            'Algeria',
            'Angola',
            'Argentina',
            'Armenia',
            'Australia',
            'Austria',
            'Azerbaijan',
            'Bahamas',
            'Bangladesh',
            'Belarus',
            'Belgium',
            'Belize',
            'Benin',
            'Bhutan',
            'Bolivia',
            'Bosnia and Herzegovina',
            'Botswana',
            'Brazil',
            'Brunei Darussalam',
            'Bulgaria',
            'Burkina Faso',
            'Burundi',
            'Cambodia',
            'Cameroon',
            'Canada',
            'Central African Republic',
            'Chad',
            'Chile',
            'China',
            'Colombia',
            'Congo',
            'Costa Rica',
            'Croatia',
            'Cuba',
            'Cyprus',
            'Czechia',
            'Democratic Republic of Congo',
            'Denmark',
            'Diamond Princess Cruise Ship',
            'Djibouti',
            'Dominican Republic',
            'Ecuador',
            'Egypt',
            'El Salvador',
            'Equatorial Guinea',
            'Eritrea',
            'Estonia',
            'Ethiopia',
            'Falkland Islands',
            'Fiji',
            'Finland',
            'France',
            'French Guiana',
            'French Southern Territories',
            'Gabon',
            'Gambia',
            'Georgia',
            'Germany',
            'Ghana',
            'Greece',
            'Greenland',
            'Guatemala',
            'Guinea',
            'Guinea-Bissau',
            'Guyana',
            'Haiti',
            'Honduras',
            'Hong Kong',
            'Hungary',
            'Iceland',
            'India',
            'Indonesia',
            'Iran',
            'Iraq',
            'Ireland',
            'Israel',
            'Italy',
            'Ivory Coast',
            'Jamaica',
            'Japan',
            'Jordan',
            'Kazakhstan',
            'Kenya',
            'Korea',
            'Kosovo',
            'Kuwait',
            'Kyrgyzstan',
            'Lao',
            'Latvia',
            'Lebanon',
            'Lesotho',
            'Liberia',
            'Libya',
            'Lithuania',
            'Luxembourg',
            'Macedonia',
            'Madagascar',
            'Malawi',
            'Malaysia',
            'Mali',
            'Mauritania',
            'Mexico',
            'Moldova',
            'Mongolia',
            'Montenegro',
            'Morocco',
            'Mozambique',
            'Myanmar',
            'Namibia',
            'Nepal',
            'Netherlands',
            'New Caledonia',
            'New Zealand',
            'Nicaragua',
            'Niger',
            'Nigeria',
            'North Korea',
            'Norway',
            'Oman',
            'Pakistan',
            'Palestine',
            'Panama',
            'Papua New Guinea',
            'Paraguay',
            'Peru',
            'Philippines',
            'Poland',
            'Portugal',
            'Puerto Rico',
            'Qatar',
            'Republic of Kosovo',
            'Romania',
            'Russia',
            'Rwanda',
            'Saudi Arabia',
            'Senegal',
            'Serbia',
            'Sierra Leone',
            'Singapore',
            'Slovakia',
            'Slovenia',
            'Solomon Islands',
            'Somalia',
            'South Africa',
            'South Korea',
            'South Sudan',
            'Spain',
            'Sri Lanka',
            'Sudan',
            'Suriname',
            'Svalbard and Jan Mayen',
            'Swaziland',
            'Sweden',
            'Switzerland',
            'Syrian Arab Republic',
            'Taiwan',
            'Tajikistan',
            'Tanzania',
            'Thailand',
            'Timor-Leste',
            'Togo',
            'Trinidad and Tobago',
            'Tunisia',
            'Turkey',
            'Turkmenistan',
            'UAE',
            'Uganda',
            'Ukraine',
            'United Kingdom',
            'Uruguay',
            'USA',
            'Uzbekistan',
            'Vanuatu',
            'Venezuela',
            'Vietnam',
            'Western Sahara',
            'Yemen',
            'Zambia',
            'Zimbabwe',]

OPTIONS_2 = [
            'new_daily_cases',
            'new_daily_deaths',
            'total_cases',
            'total_deaths'
            ]

mpl.rcParams['text.color'] = 'white'
mpl.rcParams['axes.labelcolor'] = 'white'
mpl.rcParams['xtick.color'] = 'white'
mpl.rcParams['ytick.color'] = 'white'

def getGlobalInfo():
    url = 'https://api.thevirustracker.com/free-api?global=stats'
    response = requests.request("GET", url, headers = [], data = [])
    diction = json.loads(response.text)
    out = {
        'Total Cases': diction['results'][0]['total_cases'],
        'Total Recovered': diction['results'][0]['total_recovered'],
        'Total Deaths': diction['results'][0]['total_deaths'],
        '# Of Affected Countries': diction['results'][0]['total_affected_countries']
        }
    return out

def getCountryInfo(country_code):
    url = f'https://api.thevirustracker.com/free-api?countryTotal={country_code}'
    response = requests.request("GET", url, headers = [], data = [])
    diction = json.loads(response.text)
    out = {
        'Total Cases': diction['countrydata'][0]['total_cases'],
        'Total Recovered': diction['countrydata'][0]['total_recovered'],
        'Total Deaths': diction['countrydata'][0]['total_deaths'],
        'New Cases Today': diction['countrydata'][0]['total_new_cases_today'],
        'Total Deaths Today': diction['countrydata'][0]['total_new_deaths_today'],
        '\"Danger Rank\"': diction['countrydata'][0]['total_danger_rank']
        }
    return out

def plotDates(x, y, title):
    fig = plt.figure()
    fig.patch.set_facecolor('#525252')
    ax = plt.gca(facecolor = '#525252')
    ysmoothed = gaussian_filter1d(y, sigma=1.5)
    plt.plot_date(
        x,
        ysmoothed,
        linestyle = 'solid',
        marker = None,
        linewidth = 5,
        color = 'xkcd:orangered',
        )
    plt.title(title)
    plt.tight_layout()
    plt.show()

def countryTimeline(country_code, which_y):
    url = f'https://api.thevirustracker.com/free-api?countryTimeline={country_code.upper()}'
    response = requests.request("GET", url, headers = [], data = [])
    diction = json.loads(response.text)
    dates = list(diction['timelineitems'][0].keys())[0:-1]
    new_daily_cases = np.array([diction['timelineitems'][0][i]['new_daily_cases'] for i in dates])
    new_daily_deaths = np.array([diction['timelineitems'][0][i]['new_daily_deaths'] for i in dates])
    total_cases = np.array([diction['timelineitems'][0][i]['total_cases'] for i in dates])
    total_deaths = np.array([diction['timelineitems'][0][i]['total_deaths'] for i in dates])

    x = [datetime.strptime(d,"%m/%d/%y") for d in dates]

    out = {
        'new_daily_cases': 'daily cases',
        'new_daily_deaths': 'daily deaths',
        'total_cases': 'total cases',
        'total_deaths': 'total deaths',
        }

    plotDates(x, which_y, out[str(which_y)])

    return out

def displayGlobal():
    out = getGlobalInfo()
    text = 'Total Cases: ' + str(out['Total Cases']) + '\nTotal Recoveries: ' + str(out['Total Recovered']) + '\nTotal Deaths: ' + str(out['Total Deaths']) + '\nNumber of Affected Countries: ' + str(out['# Of Affected Countries'])
    label = Label(root,
                  relief=FLAT,
                  font=(
                      'calibri',
                      12
                        ),
                  text=text)

# def displayCountry(country_code):
#         'New Cases Today': diction['countrydata'][0]['total_new_cases_today'],
#         'Total Deaths Today': diction['countrydata'][0]['total_new_deaths_today'],
#         '\"Danger Rank\"': diction['countrydata'][0]['total_danger_rank']
#         })
#     canvas1.create_window(200, 460, window=label)


root = Tk()

HEIGHT = 400
WIDTH = 750

canvas1 = Canvas(root, width=WIDTH, height=HEIGHT)
canvas1.pack()

background_image = PhotoImage(file=os.getcwd()+'\\landscape.png')
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

pre_entry1 = StringVar(root, value='Choose a Country')
entry1 = OptionMenu(root, pre_entry1, *OPTIONS)
canvas1.create_window(400, 238, window=entry1)

button1 = Button(
    text='Global Info',
    font=('calibri', 12),
    relief=FLAT,
    bg="#ff8967",
    activebackground="#ff8967",
    command=displayGlobal()
    )


canvas1.create_window(200, 180, window=button1)

root.mainloop()

