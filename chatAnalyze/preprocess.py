import re
import pandas as pd


def preprocess(data):
    # WhatsApp message date-time pattern
    pattern = r'\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}\s?[APap][Mm]\s-\s'

    # Extract messages and dates
    messages = re.split(pattern, data)[1:]  # First entry is usually empty, so we ignore it
    dates = re.findall(pattern, data)

    # If no messages found, return empty DataFrame
    if not messages or not dates:
        return pd.DataFrame(columns=['date', 'users', 'message', 'year', 'month', 'day', 'hour', 'minute'])

    # Clean the date format
    cleaned_dates = [date.strip(' - ') for date in dates]

    # Create DataFrame
    df = pd.DataFrame({'user_message': messages, 'date': cleaned_dates})

    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%y, %I:%M %p', errors='coerce')

    # Drop NaT values (invalid dates)
    df = df.dropna().reset_index(drop=True)

    # Extract user and messages
    users = []
    messages = []

    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message, maxsplit=1)
        if len(entry) > 2:  # If a username exists
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])

    # Add extracted data to DataFrame
    df['users'] = users
    df['message'] = messages

    # Drop old column
    df.drop(columns=['user_message'], inplace=True)

    # Extract additional time information
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df