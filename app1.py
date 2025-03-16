import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def main():
    st.sidebar.title("📊 Chat Analyzer")

    # File Uploader
    uploaded_file = st.sidebar.file_uploader("Choose a file")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        data = bytes_data.decode("utf-8")

        df = preprocessor.preprocess(data)

        user_list = df['users'].unique().tolist()
        if 'group_notification' in user_list:
            user_list.remove('group_notification')
        user_list.sort()
        user_list.insert(0, "Overall")

        selected_user = st.sidebar.selectbox('Show analytics for', user_list)

        if st.sidebar.button("Show Analysis"):
            num_messages, words, num_media_messages, link = helper.fetch_stats(selected_user, df)

            st.title(f"📊 Analysis for {selected_user}")

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Messages", num_messages)
            with col2:
                st.metric("Total Words", len(words))
            with col3:
                st.metric("Media Shared", num_media_messages)
            with col4:
                st.metric("Links Shared", link)

            # Timeline Charts
            st.subheader("📅 Message Timeline")
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("📆 Monthly Timeline")
                timeline = helper.monthly_timeline(selected_user, df)

                if len(timeline['time']) == len(timeline['message']):
                    fig = px.line(timeline, x='time', y='message', title="Monthly Messages")
                    st.plotly_chart(fig)
                else:
                    st.error("⚠ Error: Timeline data size mismatch.")

            with col2:
                st.subheader("📅 Daily Timeline")
                daily_timeline = helper.daily_timeline(selected_user, df)

                if len(daily_timeline['only_date']) == len(daily_timeline['message']):
                    fig = px.area(daily_timeline, x='only_date', y='message', title="Daily Messages")
                    st.plotly_chart(fig)
                else:
                    st.error("⚠ Error: Daily timeline data size mismatch.")

            # Heatmap
            st.subheader("🔥 Weekly Activity Heatmap")

            user_heatmap = helper.activity_heatmap(selected_user, df)

            fig, ax = plt.subplots(figsize=(8, 6))  # Adjust width=8, height=6 as needed
            sns.heatmap(user_heatmap, ax=ax, cmap="coolwarm", )  # Add color and annotations if needed

            st.pyplot(fig)

            # Most Active Users (Only for 'Overall')
            if selected_user == 'Overall':
                st.subheader("👥 Most Active Users")
                x, new_df = helper.most_busy_user(df)

                col1, col2 = st.columns(2)
                with col1:
                    fig = px.bar(x=x.values[:10], y=x.index[:10], orientation='h', title="Top Users", color=x.values[:10])
                    st.plotly_chart(fig)
                with col2:
                    st.dataframe(new_df.style.background_gradient(cmap="Blues"))

            # Word Cloud
            st.subheader("🌥 Word Cloud")
            df_wc = helper.create_wordcloud(selected_user, df)

            fig, ax = plt.subplots(figsize=(10, 6))
            ax.imshow(df_wc, interpolation='bilinear')
            ax.axis('off')
            st.pyplot(fig)

            # Most Common Words
            st.subheader("🔤 Most Common Words")
            most_common_df = helper.most_common_user(selected_user, df)

            if len(most_common_df[0]) > 0:
                fig = px.bar(x=most_common_df[1][:15], y=most_common_df[0][:15], orientation='h', title="Most Used Words", color=most_common_df[1][:15])
                st.plotly_chart(fig)
            else:
                st.warning("No common words data available.")

            # Emoji Analysis
            st.subheader("😀 Emoji Analysis")
            emoji_df = helper.most_common_emoji(selected_user, df)

            if not emoji_df.empty:
                col1, col2 = st.columns(2)
                with col1:
                    st.dataframe(emoji_df.style.background_gradient(cmap="YlOrRd"))
                with col2:
                    fig = px.pie(values=emoji_df[1].head(8), names=emoji_df[0].head(8), hole=0.4, title="Top Emojis")
                    st.plotly_chart(fig)
            else:
                st.warning("No emoji data available.")
if __name__ == "__main__":
    main()