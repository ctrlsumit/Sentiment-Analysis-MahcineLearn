from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections  import Counter
import emoji

extract = URLExtract()

def fetch_stats(user_selected , df):

    if user_selected != 'Overall':
        df = df[df['users'] == user_selected]

    #1 . fetch the number of messages
    num_messages = df.shape[0]

    # 2/ number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    #3. fetch number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    #4. fetch number of links share
    link = []

    for message in df['message']:
        link.extend(extract.find_urls(message))


    return num_messages , words , num_media_messages , len(link)


#Busy user
def most_busy_user(df):
    x = df['users'].value_counts().head()
    df = round((df['users'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percent'})
    return x , df ;

def create_wordcloud(user_selected, df):
    if user_selected != 'Overall':
        df = df[df['users'] == user_selected]

    if df.empty:  # Check if dataframe is empty after filtering
        return None

    temp = df[df['users'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')

    df_wc = wc.generate(temp['message'].dropna().str.cat(sep=" "))  # Drop NaN values
    return df_wc


def most_common_user(user_selected , df):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    if user_selected != 'Overall':
        df = df[df['users'] == user_selected]

    temp = df[df['users'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []

    for item in temp['message']:
        for word in item.lower().split():
            if word not in stop_words :
                words.extend(item.split())

    from collections import Counter
    return pd.DataFrame(Counter(words).most_common(20))

def most_common_emoji(user_selected , df):
    if user_selected != 'Overall':
        df = df[df['users'] == user_selected]

    emojis = []
    for message in df['message'].dropna():  # Drop NaN values to avoid errors
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

#Timeline
def monthly_timeline(user_selected , df):
    if user_selected != 'Overall':
        df = df[df['users'] == user_selected]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
    timeline['time'] = time

    return timeline

def daily_timeline(user_selected , df):
    if user_selected != 'Overall':
        df = df[df['users'] == user_selected]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline

def week_activity_map(user_selected , df):
    if user_selected != 'Overall':
        df = df[df['users'] == user_selected]

    return df['day_name'].value_counts()

def month_activity_map(user_selected , df):
    if user_selected != 'Overall':
        df = df[df['users'] == user_selected]

    return df['month'].value_counts()


def activity_heatmap(user_selected , df):
    if user_selected != 'Overall':
        df = df[df['users'] == user_selected]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return user_heatmap