"""
Text analysis for open-ended survey responses
"""

import pandas as pd
import numpy as np
import re
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Custom stopwords for church context
CUSTOM_STOPWORDS = set(stopwords.words('english')).union({
    'phcrc', 'church', 'would', 'think', 'people', 'one', 'like', 'also',
    'us', 'need', 'make', 'could', 'see', 'feel', 'want', 'get', 'know'
})

def extract_keywords(text_series, top_n=20):
    """Extract most common keywords from text responses"""
    all_words = []

    for text in text_series.dropna():
        # Convert to lowercase and tokenize
        text = str(text).lower()
        words = word_tokenize(text)

        # Filter: only words with 3+ chars, not stopwords, alphabetic
        words = [w for w in words if len(w) > 3 and w.isalpha() and w not in CUSTOM_STOPWORDS]
        all_words.extend(words)

    return Counter(all_words).most_common(top_n)

def generate_wordcloud(text_series, title, filename):
    """Generate and save word cloud from text responses"""
    # Combine all text
    all_text = ' '.join(text_series.dropna().astype(str))

    # Generate word cloud
    wordcloud = WordCloud(
        width=1200,
        height=600,
        background_color='white',
        stopwords=CUSTOM_STOPWORDS,
        colormap='viridis',
        max_words=100
    ).generate(all_text)

    # Plot
    plt.figure(figsize=(15, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title, fontsize=18, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(f'outputs/figures/{filename}', dpi=300, bbox_inches='tight')
    plt.close()

def analyze_worship_appreciation(df):
    """Analyze what people appreciate about worship"""
    col = "Please describe what you most appreciate about PHCRC's worship services."

    print("\n" + "=" * 80)
    print("WORSHIP APPRECIATION - KEY THEMES")
    print("=" * 80)

    keywords = extract_keywords(df[col], top_n=25)
    print("\nTop Keywords:")
    for word, count in keywords:
        print(f"  {word}: {count}")

    # Generate word cloud
    generate_wordcloud(df[col], "What People Appreciate About Worship", "worship_appreciation_wordcloud.png")

    return keywords

def analyze_worship_changes(df):
    """Analyze suggested changes to worship"""
    col = "What changes or additions, if any, would you suggest for our worship services to enhance your spiritual experience?"

    print("\n" + "=" * 80)
    print("WORSHIP CHANGES - KEY THEMES")
    print("=" * 80)

    keywords = extract_keywords(df[col], top_n=25)
    print("\nTop Keywords:")
    for word, count in keywords:
        print(f"  {word}: {count}")

    generate_wordcloud(df[col], "Suggested Worship Changes", "worship_changes_wordcloud.png")

    return keywords

def analyze_music_feedback(df):
    """Analyze feedback on music blend"""
    col = "Do you feel the current blend of traditional and occasional contemporary music in our services effectively meets your spiritual needs? Please explain."

    print("\n" + "=" * 80)
    print("MUSIC FEEDBACK - KEY THEMES")
    print("=" * 80)

    keywords = extract_keywords(df[col], top_n=25)
    print("\nTop Keywords:")
    for word, count in keywords:
        print(f"  {word}: {count}")

    generate_wordcloud(df[col], "Music Style Feedback", "music_feedback_wordcloud.png")

    return keywords

def analyze_spiritual_growth_suggestions(df):
    """Analyze suggestions for spiritual growth ministries"""
    col = "What new or expanded ministries for spiritual growth would you like to see for yourself or other age groups within the church?"

    print("\n" + "=" * 80)
    print("SPIRITUAL GROWTH SUGGESTIONS - KEY THEMES")
    print("=" * 80)

    keywords = extract_keywords(df[col], top_n=25)
    print("\nTop Keywords:")
    for word, count in keywords:
        print(f"  {word}: {count}")

    generate_wordcloud(df[col], "Spiritual Growth Ministry Suggestions", "spiritual_growth_wordcloud.png")

    return keywords

def analyze_belonging(df):
    """Analyze suggestions for fostering belonging"""
    col = 'How can PHCRC better foster a sense of belonging for members, especially those who may struggle with commitment beyond Sunday mornings?'

    print("\n" + "=" * 80)
    print("FOSTERING BELONGING - KEY THEMES")
    print("=" * 80)

    keywords = extract_keywords(df[col], top_n=25)
    print("\nTop Keywords:")
    for word, count in keywords:
        print(f"  {word}: {count}")

    generate_wordcloud(df[col], "Fostering Belonging Suggestions", "belonging_wordcloud.png")

    return keywords

def analyze_mission_statement_living(df):
    """Analyze how well church lives out mission statement"""
    col = 'How well do you believe PHCRC is currently living out its mission statement: "EQUIPPING DISCIPLES TO BECOME NEIGHBORS; INVITING NEIGHBORS TO BECOME DISCIPLES"? Please provide examples.'

    print("\n" + "=" * 80)
    print("LIVING OUT MISSION STATEMENT - KEY THEMES")
    print("=" * 80)

    keywords = extract_keywords(df[col], top_n=25)
    print("\nTop Keywords:")
    for word, count in keywords:
        print(f"  {word}: {count}")

    generate_wordcloud(df[col], "Living Out Mission Statement", "mission_statement_wordcloud.png")

    return keywords

def analyze_pastor_priorities(df):
    """Analyze priorities for new pastor's first year"""
    col = 'If you could identify one or two top priorities for our new pastor to focus on in their first year, what would they be? (e.g., fostering belonging, enhancing diversity, strengthening youth program...'

    print("\n" + "=" * 80)
    print("PASTOR'S FIRST YEAR PRIORITIES - KEY THEMES")
    print("=" * 80)

    # Show actual responses for this critical question
    print("\nActual Responses:")
    for idx, response in enumerate(df[col].dropna(), 1):
        print(f"\n{idx}. {response}")

    keywords = extract_keywords(df[col], top_n=30)
    print("\n\nTop Keywords:")
    for word, count in keywords:
        print(f"  {word}: {count}")

    generate_wordcloud(df[col], "Pastor's First Year Priorities", "pastor_priorities_wordcloud.png")

    return keywords

def analyze_pastor_qualities(df):
    """Analyze desired pastor qualities"""
    col = 'Beyond the general responsibilities of a Minister of Worship and Leadership, what specific gifts, skills, or personal characteristics are most important to you in our next pastor? (Consider how th...'

    print("\n" + "=" * 80)
    print("DESIRED PASTOR QUALITIES - KEY THEMES")
    print("=" * 80)

    # Show actual responses
    print("\nActual Responses:")
    for idx, response in enumerate(df[col].dropna(), 1):
        print(f"\n{idx}. {response}")

    keywords = extract_keywords(df[col], top_n=30)
    print("\n\nTop Keywords:")
    for word, count in keywords:
        print(f"  {word}: {count}")

    generate_wordcloud(df[col], "Desired Pastor Qualities", "pastor_qualities_wordcloud.png")

    return keywords

def analyze_reformed_identity(df):
    """Analyze what Reformed identity means to congregation"""
    col = 'What does being "Christians of Reformed accent" mean to you personally, and how do you see this reflected in our church life?'

    print("\n" + "=" * 80)
    print("REFORMED IDENTITY - KEY THEMES")
    print("=" * 80)

    keywords = extract_keywords(df[col], top_n=25)
    print("\nTop Keywords:")
    for word, count in keywords:
        print(f"  {word}: {count}")

    generate_wordcloud(df[col], "Reformed Identity Understanding", "reformed_identity_wordcloud.png")

    return keywords

def analyze_crc_relationship(df):
    """Analyze perspective on CRC denomination relationship"""
    col = "What is your perspective on PHCRC's relationship with the Christian Reformed denomination today?"

    print("\n" + "=" * 80)
    print("CRC RELATIONSHIP - KEY THEMES")
    print("=" * 80)

    # Show actual responses for this important question
    print("\nActual Responses:")
    for idx, response in enumerate(df[col].dropna(), 1):
        print(f"\n{idx}. {response}")

    keywords = extract_keywords(df[col], top_n=25)
    print("\n\nTop Keywords:")
    for word, count in keywords:
        print(f"  {word}: {count}")

    generate_wordcloud(df[col], "CRC Denomination Relationship", "crc_relationship_wordcloud.png")

    return keywords

def analyze_future_goals(df):
    """Analyze goals for next 3-5 years"""
    col = "What are the most important goals or opportunities you envision for PHCRC in the next 3-5 years? (Consider the stated goals: expanding kids/youth, expanding diversity, growing community outreach)."

    print("\n" + "=" * 80)
    print("3-5 YEAR GOALS - KEY THEMES")
    print("=" * 80)

    keywords = extract_keywords(df[col], top_n=30)
    print("\nTop Keywords:")
    for word, count in keywords:
        print(f"  {word}: {count}")

    generate_wordcloud(df[col], "Goals for Next 3-5 Years", "future_goals_wordcloud.png")

    return keywords

def main():
    """Main text analysis function"""
    print("\n" + "=" * 80)
    print("TEXT ANALYSIS - OPEN-ENDED RESPONSES")
    print("=" * 80)

    df = pd.read_csv('survey-answers.csv')

    # Analyze various open-ended questions
    analyze_worship_appreciation(df)
    analyze_worship_changes(df)
    analyze_music_feedback(df)
    analyze_spiritual_growth_suggestions(df)
    analyze_belonging(df)
    analyze_mission_statement_living(df)
    analyze_pastor_priorities(df)
    analyze_pastor_qualities(df)
    analyze_reformed_identity(df)
    analyze_crc_relationship(df)
    analyze_future_goals(df)

    print("\n" + "=" * 80)
    print("TEXT ANALYSIS COMPLETE - Word clouds saved to outputs/figures/")
    print("=" * 80)

if __name__ == "__main__":
    main()
