import streamlit as st
from IPython.core.pylabtools import figsize
# from sympy import rotations

import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.sidebar.title("Chat Analyzer")

    uploaded_file = st.sidebar.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        data = bytes_data.decode("utf-8")

        df = preprocessor.preprocess(data)

        # st.dataframe(df)

        # Fetch unique users
        user_list = df['users'].unique().tolist()
        user_list.remove('group_notification')
        user_list.sort()
        user_list.insert(0, "Overall")

        selected_user = st.sidebar.selectbox('Show analytics Wrt', user_list)

        if st.sidebar.button("Show Analysis"):
            num_messages, words, num_media_messages, link = helper.fetch_stats(selected_user, df)

            st.title(selected_user)

            st.title("Top Statistics")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.header("Total Message")
                st.title(num_messages)

            with col2:
                st.header("Total Words")
                st.title(len(words))

            with col3:
                st.header("Media Shared")
                st.title(num_media_messages)

            with col4:
                st.header("Link Shared")
                st.title(link)

            # Timeline
            col1, col2 = st.columns(2)
            # Monthly
            with col1:
                st.title("Monthly Timeline")
                timeline = helper.monthly_timeline(selected_user, df)

                fig, ax = plt.subplots(figsize=(10, 5))
                ax.plot(timeline['time'], timeline['message'], color='green')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            # Daily
            with col2:
                st.title("Daily Timeline")
                dail_timeline = helper.daily_timeline(selected_user, df)

                fig, ax = plt.subplots(figsize=(10, 6))
                ax.plot(dail_timeline['only_date'], dail_timeline['message'], color='green')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            # Activity map
            st.title("Activity Map")
            col1, col2 = st.columns(2)

            with col1:
                st.header("Most Active Day")
                busy_day = helper.week_activity_map(selected_user, df)
                fig, ax = plt.subplots(figsize=(10, 10))
                ax.bar(busy_day.index, busy_day.values, color='orange')
                st.pyplot(fig)

            with col2:
                st.header("Most Active Month")
                busy_week = helper.month_activity_map(selected_user, df)
                fig, ax = plt.subplots(figsize=(10, 10))
                ax.bar(busy_week.index, busy_week.values, color='red')
                st.pyplot(fig)

            user_heatmap = helper.activity_heatmap(selected_user, df)

            fig, ax = plt.subplots(figsize=(8, 6))  # Adjust width=8, height=6 as needed
            sns.heatmap(user_heatmap, ax=ax, cmap="coolwarm")  # Add color and annotations if needed
            st.pyplot(fig)

            # Finding the busiest users in the group (Group level)
            if selected_user == 'Overall':
                st.title('Most Active Users')
                x, new_df = helper.most_busy_user(df)
                fig, ax = plt.subplots()

                col1, col2 = st.columns(2)

                with col1:
                    ax.bar(x.index, x.values)
                    plt.xticks(rotation='vertical')
                    st.pyplot(fig)

                with col2:
                    st.dataframe(new_df)

            # WordCloud
            st.title("WordCloud")
            df_wc = helper.create_wordcloud(selected_user, df)
            fig, ax = plt.subplots()
            ax.imshow(df_wc)
            st.pyplot(fig)

            # Most common words
            most_common_df = helper.most_common_user(selected_user, df)

            fig, ax = plt.subplots()

            ax.barh(most_common_df[0], most_common_df[1])
            plt.xticks(rotation='vertical')
            st.title("Most Common Words")
            st.pyplot(fig)
            # st.dataframe(most_common_df)

            # Emoji Analysis
            emoji_df = helper.most_common_emoji(selected_user, df)
            st.title("Emoji Analysis")

            col1, col2 = st.columns(2)

            with col1:
                st.dataframe(emoji_df)

            with col2:
                fig, ax = plt.subplots()
                ax.pie(emoji_df[1].head(10), labels=emoji_df[0].head(10), autopct="%0.2f")
                st.pyplot(fig)

if __name__ == "__main__":
    main()